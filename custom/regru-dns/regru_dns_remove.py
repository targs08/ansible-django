#!/usr/bin/python3

import requests
import json
import sys
import getopt


import getopt
import sys

username = 'test'
password = 'test'
domain = 'test.ru'
subdomain = 'test'

try:
    options, remainder = getopt.getopt(sys.argv[1:], 'vu:p:d:s:', ['username=',
                                                         'password=',
                                                         'domain='
                                                         'subdomain=',
                                                         ])
except getopt.GetoptError as err:
    print('ERROR:', err)
    sys.exit(1)

for opt, arg in options:
    if opt in ('-u', '--username'):
        username = arg
    elif opt in ('-p', '--password'):
        password = arg
    elif opt in ('-d', '--domain'):
        domain = arg
    elif opt in ('-s', '--subdomain'):
        subdomain = arg

#sys.exit()

apiUrl = "https://api.reg.ru/api/regru2/zone/remove_record"

parameters = {
    'username': username,
    'password': password,
    'domains': [
        { "dname": domain  }
    ],
    'subdomain': subdomain,
    'record_type': "A",
    'output_content_type': "plain"
}

r = requests.post(apiUrl, data = {'input_data': json.dumps(parameters), 'input_format': 'json'})
print(r.text)
