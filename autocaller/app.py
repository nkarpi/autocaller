# Download the library from twilio.com/docs/libraries

from flask import Flask
from flask import request
from flask import url_for

from twilio import twiml
import twilio.twiml
from twilio.rest import TwilioRestClient

import praw
from settings import * 

# Declare and configure application
app = Flask(__name__, static_url_path='/static')
app.config.from_pyfile('settings.py')

# default route
# @app.route('/')
# def index():
#     return str("Hello World foobar")

# Voice Request URL
@app.route('/call', methods=['POST'])
def call():
    # Get phone number we need to call

    twilio_client = TwilioRestClient(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    
    twilio_client.calls.create(from_=TWILIO_NUMBER,
                               to=CALL_TO_NUMBER,
                               url='localhost:5000/message')


@app.route('/message', methods=['GET','POST'])
def message():

    resp = twilio.twiml.Response()

    r = praw.Reddit(user_agent='web:autocaller:v1.0 (by nkarpi)')
    posts_generator = r.get_content(REDDIT_URL)
    posts = list(posts_generator)
    top_post = posts[0]

    resp.say("Nolan Karpinski " + str(top_post).split('::')[1],
                 voice='alice')

    return str(resp)

