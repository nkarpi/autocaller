# import flask - lightweight web framework
from flask import Flask
# import twiml - a twilio app for making the voice message
import twilio.twiml
# import praw - Python Reddit API Wrapper
import praw
 
app = Flask(__name__)

REDDIT_URL='https://www.reddit.com/'
 
@app.route("/message", methods=['GET', 'POST'])
def message():

	# instantiate a praw object and retrieve the top posts
	# parse the top posts to get the #1 headline w/out associated score
    r = praw.Reddit(user_agent='web:autocaller:v1.0 (by nkarpi)')
    posts_generator = r.get_content(REDDIT_URL)
    top_post = list(posts_generator)[0]
    headline = str(top_post).split('::')[1]

    # instantiate a twiml respoonse obj. 
    # Use the "say" verb to create XLM response
    resp = twilio.twiml.Response()
    resp.say("Nolan Karpinski " + headline,
                 voice='alice')

    return str(resp)
 

if __name__ == "__main__":
    app.run(debug=True, port=4000)