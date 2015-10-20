AUTOCALLER

Author: Nolan Karpinski
Last Edit: 10/19/2015

Functionality: 
This project uses the Twilio API to send automated phone calls
with user-specified voice messages. 


Implementation:
The current setup calls the phone number specified in autocaller/app.py 
with an automated message structured by the TwiML app in voice.py 
(currently hosted on Heroku). 

Voice.py (TwiML app) calls the Python API Wrapper and retrieves the top 
headline from the front page of Reddit and creates/returns an XML object, 
available to the public web, which is ultimately called by the Twilio App to 
direct what the automated call should do when initiated, using the "say" verb

Additional necessary files:
A settings.py file is needed locally to specify:
	TWILIO_ACCOUNT_SID
	TWILIO_AUTH_TOKEN 
	TWILIO_NUMBER
	CALL_TO_NUMBER 
	VOICE_MSG_URL

