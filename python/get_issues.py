import requests
import os
import json

from helpers import *

# verify environment before starting
checkEnv()

# create our headers for api request
headers = {
        'Content-Type': 'application/json',
        'Authorization': 'token {}'.format(os.getenv(SNYK_TOKEN))
    }

# create our body for api request
body = {
        'filters': {
            'orgs': [os.getenv(ORG_ID)],
            'exploitMaturity': ['mature'],
            'types': ['vuln']
        }
    }

# make API request
response = json.loads(requests.post('{}/reporting/issues/latest'.format(BASE_URL), headers=headers, data=json.dumps(body)).content)

# print(response_json)

for result in response['results']:
    print('Issue: {}, Title: {}, Project: {}, Severity: {}'.format(result['issue']['id'], result['issue']['title'], result['project']['name'], result['issue']['severity']))