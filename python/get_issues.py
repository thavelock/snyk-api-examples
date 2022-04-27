import requests
import os
import json

from helpers import *

# verify environment before starting
checkEnv()

# retrieve user input
print('0: mature, 1: proof-of-concept, 2: no-known-exploit, 3: no-data')
maturity_num = input('Please input exploit maturity: ')

if (maturity_num == '0'):
    maturity = 'mature'
elif (maturity_num == '1'):
    maturity = 'proof-of-concept'
elif (maturity_num == '2'):
    maturity = 'no-known-exploit'
elif (maturity_num == '3'):
    maturity = 'no-data'
else:
    print('Invalid input!')
    sys.exit(0)

# create our headers for api request
headers = {
        'Content-Type': 'application/json',
        'Authorization': 'token {}'.format(os.getenv(SNYK_TOKEN))
    }

# create our body for api request
body = {
        'filters': {
            'orgs': [os.getenv(ORG_ID)],
            'exploitMaturity': [maturity],
            'types': ['vuln']
        }
    }

# make API request
response = json.loads(requests.post('{}/reporting/issues/latest'.format(BASE_URL), headers=headers, data=json.dumps(body)).content)

# list results
for result in response['results']:
    print('Issue: {}, Title: {}, Project: {}, Severity: {}'.format(result['issue']['id'], result['issue']['title'], result['project']['name'], result['issue']['severity']))