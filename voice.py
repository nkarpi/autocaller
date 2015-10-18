from flask import Flask
import twilio.twiml
import praw
from settings import *
 
app = Flask(__name__)
 
@app.route("/", methods=['GET', 'POST'])
def message():

    resp = twilio.twiml.Response()

    r = praw.Reddit(user_agent='web:autocaller:v1.0 (by nkarpi)')
    posts_generator = r.get_content(REDDIT_URL)
    posts = list(posts_generator)
    top_post = posts[0]

    resp.say("Nolan Karpinski " + str(top_post).split('::')[1],
                 voice='alice')

    return str(resp)
 
if __name__ == "__main__":
    app.run(debug=True)
