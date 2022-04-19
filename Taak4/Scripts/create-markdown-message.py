# Fill in this file with the messages code from the Webex Teams exercise
import requests
access_token = 'YjhlYjQyZDAtNWJiZS00MmY1LWFjZmUtNTE4NzcyY2I3ZGIwYmVkZGIzYzAtNWNi_PE93_9423ebf1-df21-4e89-8049-a08f8e9c5998'
room_id = 'Y2lzY29zcGFyazovL3VybjpURUFNOmV1LWNlbnRyYWwtMV9rL1JPT00vMjU1ZWRkZDAtYmZiNi0xMWVjLWJmY2ItYjNlODdhZWRhZTk1'
message = 'Hier zijn mijn schermafbeeldingen van EN2_Devasc_2SNE-taken'
url = 'https://webexapis.com/v1/messages'
headers = {
 'Authorization': 'Bearer {}'.format(access_token),
 'Content-Type': 'application/json'
}
params = {'roomId': room_id, 'markdown': message}
res = requests.post(url, headers=headers, json=params)
print(res.json())
