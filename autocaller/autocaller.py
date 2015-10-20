# app.py 

# Uses the Twilio API to instantiate a phone call, with call
# data retrieved from the VOICE_MSG_URL 

# import Flask - lightweight web framework
from flask import Flask
from flask import request

# Download the library from twilio.com/docs/libraries
from twilio.rest import TwilioRestClient


# This settings file includes all global variables used here
from settings import * 

# Declare and configure application
app = Flask(__name__, static_url_path='/static')
app.config.from_pyfile('settings.py')

# default route for debugging purposes
@app.route('/')
def index():
    return str("Twilio App - Online")

# Voice Request endpoint
@app.route('/call', methods=['POST'])
def call():
    # Create the twilio client object with the SID and Auth Token
    twilio_client = TwilioRestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    # Eexecute a call using the associated URL
    # The URL contains the call data/message
    twilio_client.calls.create(from_=TWILIO_NUMBER,
                               to=CALL_TO_NUMBER,
                               url=VOICE_MSG_URL,
                               ifmachine='Continue',)


