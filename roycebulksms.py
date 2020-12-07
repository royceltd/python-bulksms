import requests

endpoint = "https://bulksms.roycetechnologies.co.ke/api/sendmessage"
data = {"ip": "1.1.2.3", 'sender_id': 'RoyceLtd', 'text_message': 'Hello world',
        'phone_number': '0713727937'}
headers = {
    "Authorization": "Bearer 11|xkBZ1pYwgifU2fR1rZ5iBsjwxrlxbG1TtR0StTYx"}
requests.post(endpoint, data=data, headers=headers)
