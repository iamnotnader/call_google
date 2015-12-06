# Download the library from twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

# Get these credentials from http://twilio.com/user/account
account_sid = "ACb7e61b6a71a6ac077aefe47059f1fd40"
auth_token = "123f0c65706b5b44bed4dd1289095b4e"
client = TwilioRestClient(account_sid, auth_token)

# Make the call
call = client.calls.create(to="+16504403103",  # Any phone number
                           from_="+12127296389",  # Must be a valid Twilio number
                           url="http://ec2-52-89-135-84.us-west-2.compute.amazonaws.com:5000")
print call.sid
