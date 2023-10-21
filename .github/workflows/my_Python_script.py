import requests
import os
import json
# print(os.__dict__)
# print(os.environ['git_url'])
url = f"{os.environ['GITHUB_SERVER_URL']}/{os.environ['GITHUB_REPOSITORY']}"
data = {
  "url" : url
}
print(data)
 #this is actual url
#url = requests.post(url="http://13.233.5.47:8000/trigger-script",json=data)
url = requests.post(url="https://13.233.5.47:8000/trigger-script",json=data)
print(url.text)
print("hello")




