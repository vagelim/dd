#!/usr/bin/env python
from datadog import initialize, api
import code
import json
import os


def main(account=None):
    SETTINGS = os.environ['GET_SCREEN_CREDS']
    keys = json.load(open(SETTINGS, 'r'))

    if account is None:
        case = "prod"
    try:
        options = {
            'api_key': keys[case]['API'],
            'app_key': keys[case]['APP']
        }
    except KeyError:
        case = "prod"
    initialize(**options)
    print "DD account: " + case
    code.interact(local=dict(globals(), **locals()))



if __name__ == "__main__":
    try:
        main(sys.argv[1])
    except IndexError:
        main()