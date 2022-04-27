import requests
import os
import json

from helpers import *

# verify environment before starting
checkEnv()

# create our headers for api request
headers = {
    'Authorization': 'token {}'.format(os.getenv(SNYK_TOKEN)),
    'Content-Type': 'application/json'
    }


# Specify dependency details
package_mgr = 'npm'
package_name = 'express-jwt'
package_version = '0.1.3'

# make API request to get issues
response = requests.get('{}/test/{}/{}/{}'.format(BASE_URL, package_mgr, package_name, package_version), headers=headers)

# dump json results with issues to dict
issues_response_json = json.loads(response.content)
issues_dict = issues_response_json['issues']['vulnerabilities']

# Specify jira ticket details
jira_project_key = 'GOOF' # Specify a project in your Jira org
jira_issue_type = 'Task' # Specify an issue type (e.g., Task or Epic) 
project_id = 'bc498bb1-1c46-4ad8-b5c7-2ad7bdeafb39' #Specify a Snyk project ID
issue_id = 'SNYK-JAVA-COMFASTERXMLJACKSONCORE-31520'

description = ""

for issue in issues_dict:
    description+=issue['id']+"\n"+issue['url']
    description += '\n\n'

body = {
        'fields': {
            'project': {
                'key': jira_project_key
            },
            'issuetype': {
                'name': jira_issue_type
            },
            'summary': 'Direct and/or transitive issues identified for {}@{}'.format(package_name, package_version),
            'description': description
        }
    }

#body = f""" 
#    {{
#        "fields": {{
#            "project": {{
#                "key": "{jira_project_key}"
#            }},
#            "issuetype": {{
#                "name": "{jira_issue_type}"
#            }},
#            "summary": "Direct and/or transitive issues identified for {package_name}@{package_version}",
#            "description": "test"
#        }}
#    }}
#"""

print(json.dumps(body))
response = requests.post('{}/org/{}/project/{}/issue/{}/jira-issue'.format(BASE_URL, os.getenv(ORG_ID), project_id, issue_id), headers=headers, data=json.dumps(body))
print(response.content)


