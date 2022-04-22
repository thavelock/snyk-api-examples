from unicodedata import name
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
    response = requests.delete('{}/org/{}/project/{}'.format(BASE_URL, os.getenv(ORG_ID), project['id']),
                            headers=headers)

    if response.status_code == 200:
        print('Successfully deleted {}'.format(project['name']))
    else:
        print('Could not delete project {}, reason: {}'.format(project['name'], response.status_code))