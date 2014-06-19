from twilio.rest import TwilioRestClient
from sys import argv 

script, to_number , sms_message = argv
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC771e2dd643d0c43e3fcf35374866404d"
auth_token  = "2a5d74b7b1aa24105d2533276b54221d"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body = sms_message,
    to= to_number ,    # Replace with your phone number
    from_="+13176718700") # Replace with your Twilio number
print message.sid