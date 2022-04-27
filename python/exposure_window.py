import requests
import json
import os
from helpers import *
from datetime import datetime

# Checking Environment for API token 
checkEnv()

start_date = input("Start Date: ")
end_date = input("End Date: ")
CVE_CWE = input("Enter a CVE or CWE: ")

# header for API request 
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'token {}'.format(os.getenv(SNYK_TOKEN))
}
# body for API request 
values = f"""
{{
    "filters": {{
        "orgs": [<OrgID>], ##Input your orgID here
        "severity": [
        "critical",
        "high",
        "medium",
        "low"
        ],
        "exploitMaturity": [
        "mature",
        "proof-of-concept",
        "no-known-exploit",
        "no-data"
        ],
        "types": [
        "vuln",
        "license",
        "configuration"
        ],
        "projects": [],
        "issues": [],
        "identifier": "{CVE_CWE}",
        "ignored": false,
        "priorityScore": {{
        "min": 0,
        "max": 1000
        }}
    }}
}}
"""

# Make API request 
reponse = json.loads(requests.post("{}/reporting/issues/?from=".format(BASE_URL) + start_date + "&to=" + end_date, data=values, headers=headers).content)

# Print issues with exposure window
delta=0
for result in reponse['results']:
    if result['isFixed'] == False:
        print('Issue: {}, Title: {}, Project: {}, Severity: {}, Exposed Since: {}\n'.format(result['issue']['id'], result['issue']['title'], result['project']['name'], result['issue']['severity'],result["introducedDate"]))
    else:
        delta = (abs((datetime.strptime(result["fixedDate"], '%Y-%m-%d'))-(datetime.strptime(result["introducedDate"], '%Y-%m-%d'))))
        print('Issue: {}, Title: {}, Project: {}, Severity: {}'.format(result['issue']['id'], result['issue']['title'], result['project']['name'], result['issue']['severity']) +", Exposure Window: " +str(delta) +"\n")
