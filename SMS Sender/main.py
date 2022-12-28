# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
client = Client(account_sid, auth_token)

message = client.messages.create(
    body="Hello from Twilio", from_=os.getenv("FROM_PHONE_NUMBER"), to=os.getenv("TO_PHONE_NUMBER")
)

print(message.sid)
