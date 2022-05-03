# Fill in this file with the authentication code from the Webex Teams exercise
import requests
import json
access_token = 'YjhlYjQyZDAtNWJiZS00MmY1LWFjZmUtNTE4NzcyY2I3ZGIwYmVkZGIzYzAtNWNi_PE93_9423ebf1-df21-4e89-8049-a08f8e9c5998'
url = 'https://webexapis.com/v1/people/me'
headers = {
 'Authorization': 'Bearer {}'.format(access_token)
}
res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))
