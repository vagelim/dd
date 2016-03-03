#!/usr/bin/env python

from datadog import initialize, api
import json
import sys
import os

    
def get(board_id, IO=True):
    #Configure keys in settings.json

    try:
        SETTINGS = os.environ['GET_SCREEN_CREDS']
    except:
        SETTINGS = "settings.json"
    keys = json.load(open(SETTINGS, 'r'))

    #List keys and wait for input:
    case = raw_input("Get board from [ " + " ".join(keys.keys()) + " ]: ")

    try:
        options = {
            'api_key': keys[case]['API'],
            'app_key': keys[case]['APP']
        }
    except KeyError:
        print "Invalid key"
        return -1

    initialize(**options)    

    try:
        result = api.Screenboard.get(board_id)
    except:
        print "Not a screenboard, trying timeboard"
        try:
            result = api.Timeboard.get(board_id)
        except:
            print "Board not found."
            return -1

    
    if 'errors' in result:
        print "\nInvalid board id. Maybe try a different account?\nQuitting..."
        return -1

    if IO is True:     
        with open( str(board_id) + '_' + case + '.txt', 'w') as f:
            f.write(json.dumps(result))
        print "Board " + str(board_id) + " saved"
    else:
        return json.dumps(result)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        board_id = raw_input("board ID: ")
    else:
        board_id = sys.argv[1]
    get(board_id)
