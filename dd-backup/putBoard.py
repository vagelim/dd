#!/usr/bin/env python
from datadog import initialize, api
import json
import sys
import os

# Takes a board's JSON and uploads it as a new screen

def main(board_id):
    #  Configure keys in settings.json

    try:
        API_KEY = os.environ['DD_API']
        APP_KEY = os.environ['DD_APP']
    except:
        API_KEY = raw_input("API_KEY: ")
        APP_KEY = raw_input("APP_KEY: ")

        options = {
            'api_key': API_KEY,
            'app_key': APP_KEY
        }

    try:
        screen = json.load(open(board_id + '.txt'))

    except IOError:
        print "File not found"

    initialize(**options)

    try:  # If it's a screenboard
        board_title = screen['board_title']
        description = "Copy of " + board_title
        width = screen['width']
        height = screen['height']
        widgets = screen['widgets']
        template_variables = screen['template_variables']

        result = api.Screenboard.create(board_title=board_title,
                 description=description, widgets=widgets,
                 template_variables=template_variables,
                 width=width, height=height)

        if 'errors' in result:
            print "\nInvalid board id. Maybe try a different account?\nQuitting..."
            return -1
        print "Cloned board URL: https://app.datadoghq.com/screen/" + str(result['id'])

    except KeyError:  # It's a dashboard
        print "Dashboard detected"
        board_title = screen['dash']['title']
        description = "Copy of " + board_title
        graphs = screen['dash']['graphs']

        try:  # Get the template variables, if any
            template_variables = screen['dash']['tempate_variables']
        except:
            template_variables = []

        result = api.Timeboard.create(title=board_title,
                 description=description,
                 graphs=graphs, template_variables=template_variables)

        if 'errors' in result:
            print "\nInvalid board id. Maybe try a different account?\nQuitting..."
            return -1
        print "Cloned board URL: https://app.datadoghq.com/dash/" + str(result['dash']['id'])

if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(board_id)
    else:
        print "Usage:\n     " + sys.argv[0] + " <board_id>"
