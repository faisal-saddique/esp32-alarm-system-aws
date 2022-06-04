# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import time

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "AC24c266cc092bc5f83e6ec5337b326495"
auth_token = "bac653544efe59efe1cb49d80c74b2c4"
client = Client(account_sid, auth_token)

for i in range(0, 5):
    call = client.calls.create(
        url='http://demo.twilio.com/docs/voice.xml',
        to='+923350584458',
        from_='+15706168944'
    )
    time.sleep(3)

print(call.sid)
