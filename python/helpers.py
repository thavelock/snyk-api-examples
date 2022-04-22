import sys
import os

# ========== CONSTANTS ==========

BASE_URL    = 'https://snyk.io/api/v1'
SNYK_TOKEN  = 'SNYK_TOKEN'
ORG_ID      = 'ORG_ID'

# ========== FUNCTIONS ==========

"""Ensure the environment has necessary environment variables"""
def checkEnv():
    # ensure we have SNYK_CODE environment variable set
    if (os.getenv('SNYK_TOKEN') is None):
        print('Please set SNYK_TOKEN:')
        print()
        print('\texport SNYK_TOKEN=<API TOKEN>')
        sys.exit(0)

    # ensure we have ORG_ID environment variable set
    if (os.getenv('ORG_ID') is None):
        print('Please set ORG_ID:')
        print()
        print('\texport ORG_ID=<ORG ID>')
        sys.exit(0)