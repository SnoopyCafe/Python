
from twilio.rest import TwilioRestClient

account_sid = "AC88b1314dc3d84307f3fc145bd8c9297c"
auth_token = "0b5f926fe09a6c4bf79e739880cd5d73"
client = TwilioRestClient(account_sid, auth_token)

message = client.sms.messages.create(
    body="Lucy please!  Don't take the ball away",
    to="15612857997",
    from_="15615134170"
)

print message.sid