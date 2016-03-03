#!/usr/bin/env python

from datadog import initialize, api
import json
import sys
import os

    
def main(board_id):
    #Configure keys in settings.json
    try:
        SETTINGS = os.environ['GET_SCREEN_CREDS']
    except:
        SETTINGS = "settings.json"
    keys = json.load(open(SETTINGS, 'r'))

    #List keys and wait for input:
    case = raw_input("Put it in [ " + " ".join(keys.keys()) + " ]: ")

    try:
        options = {
            'api_key': keys[case]['API'],
            'app_key': keys[case]['APP']
        }
    except KeyError:
        print "Invalid key"
        return -1
   
    try:
        screen = json.load(open(board_id + '_screen.txt'))
    except IOError:
        from getScreen import get
        screen = json.loads(get(board_id, IO=False))

    initialize(**options) 
    
    board_title = screen['board_title']
    description = "Copy of " + board_title
    width = screen['width']
    height = screen['height']
    widgets = screen['widgets']
    template_variables = screen['template_variables']

    result = api.Screenboard.create(board_title=board_title, description=description,
  widgets=widgets, template_variables=template_variables, width=width, height=height)        
    if 'errors' in result:
        print "\nInvalid board id. Maybe try a different account?\nQuitting..."
        return -1
    print "Cloned board URL: https://app.datadoghq.com/screen/" + str(result['id'])
        
if __name__ == '__main__':
    if len(sys.argv) < 2:
        board_id = raw_input("Which board?: ")
    else:
        board_id = sys.argv[1]
    main(board_id)
