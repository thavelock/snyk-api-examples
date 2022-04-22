import requests
import os
import json

from helpers import *

# verify environment before starting
checkEnv()

# create our headers for api request
headers = {'Authorization': 'token {}'.format(os.getenv(SNYK_TOKEN))}

# make API request
response = requests.get('{}/org/{}/projects'.format(BASE_URL, os.getenv(ORG_ID)), headers=headers)

# dump json results to dict
response_json = json.loads(response.content)

# print project names
for project in response_json['projects']:
    print(project['name'])