#!/usr/bin/env python
from datadog import initialize, api
import code
import json
import os
import sys

def main(case=None):
    SETTINGS = os.environ['GET_SCREEN_CREDS']
    keys = json.load(open(SETTINGS, 'r'))

    if case is None:
        case = "prod"
    try:
        options = {
            'api_key': keys[case]['API'],
            'app_key': keys[case]['APP']
        }
    except KeyError:
        case = "prod"
    initialize(**options)
    
    TAGS = api.Tag.get_all()['tags']
    HOSTS = api.Infrastructure.search(q='hosts:')['results']['hosts']
    print "====================="
    print "DD account: " + case
    print "Local variables: "
    print locals().keys()
    print "=========================================="
    code.interact(local=dict(globals(), **locals()))



if __name__ == "__main__":
    try:
        main(sys.argv[1])
    except IndexError:
        main()
