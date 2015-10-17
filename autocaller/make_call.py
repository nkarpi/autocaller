# Download the library from twilio.com/docs/libraries
from twilio.rest import TwilioRestClient
import praw
import tokens

# app = Flask(__name__)
 
# account_sid = "ACXXXXXXXXXXXXXXXXX"
# auth_token = "YYYYYYYYYYYYYYYYYY"
# client = TwilioRestClient(account_sid, auth_token)
 
# # Make the call
# call = client.calls.create(to="+14085551234",  # call this number
#                            from_="+12125551234", # call from this number
#                            url="http://twimlets.com/holdmusic?Bucket=com.twilio.music.ambient")

r = praw.Reddit(user_agent='web:autocaller:v1.0 (by nkarpi)')

posts_generator = r.get_content('https://www.reddit.com/')
posts = list(posts_generator)
top_post = posts[0]
print top_post


# @app.route("/")
# def hello():
#     return "posts"
 
# if __name__ == "__main__":
#     app.run(debug=True)