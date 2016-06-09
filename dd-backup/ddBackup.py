from datadog import initialize, api
import json
import os
import sys

def auth(account=None):
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

    initialize(**options)

def main(account=None):
    auth(account)
    screens = api.Screenboard.get_all()
    for each in screens['screenboards']:
        result = api.Screenboard.get(each['id'])
        with open(str(each['id']) + '.txt', 'w') as f:
            f.write(json.dumps(result))
        print "Screen " + str(each['id']) + " saved"

    dash = api.Timeboard.get_all()
    for each in dash['dashes']:
        result = api.Timeboard.get(each['id'])
        with open(str(each['id']) + '.txt', 'w') as f:
            f.write(json.dumps(result))
        print "Dash " + str(each['id']) + " saved"

if __name__ == "__main__":
    main()
