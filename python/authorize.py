import requests
import os
import json

from python.helpers import *

# verify environment before starting
checkEnv()

# create our headers for api request
headers = {'Authorization': 'token {}'.format(os.getenv(SNYK_TOKEN))}

# make API request
response = requests.get('{}'.format(BASE_URL), headers=headers)

# dump json results to dict
response_json = json.loads(response.content)

# print response dict
print(response_json)