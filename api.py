#!/usr/bin/env python
from datadog import initialize, api
import code
import json
import os
import sys


def main(case=None):

    options = {'api_key': '', 'app_key': ''}
    # Get the settings from a settings file
    if os.environ.get('GET_SCREEN_CREDS', None):
        keys = json.load(open(os.environ['GET_SCREEN_CREDS'], 'r'))

        if case is None:
            case = "prod"
        try:
            options = {
                'api_key': keys[case]['API'],
                'app_key': keys[case]['APP']
            }
        except KeyError:
            print "Keys for {} not found".format(case)
            return -1

    elif os.environ.get('DD_API', None):
        case = "default"
        options['api_key'] = os.environ['DD_API']
        options['app_key'] = os.environ['DD_APP']

    initialize(**options)

    event = api.Event.create
    post = api.Metric.send
    search = api.Infrastructure.search
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
