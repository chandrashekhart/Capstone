
import os
import requests

api_url = os.environ.get('API_URL')
repository_url = os.popen('git config --get remote.origin.url').read().strip()

payload = {
    'repository_url': repository_url
}

headers = {
    'Content-Type': 'application/json',
    # Add any other headers as needed
}

response = requests.post(api_url, json=payload, headers=headers)

if response.status_code == 200:
    print("API request was successful.")
else:
    print(f"API request failed with status code {response.status_code}.")
    print(response.text)
