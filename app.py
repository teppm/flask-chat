import os 
from flask import Flask

app = Flask(__name__)

@app.route('/')


def index():

    """main page with instructions"""
    return "To send message use /USERNAME/MESSAGE"

app.route('/username')

def user(username):
    return "Hi" + username

app.route('/<username>/<message>')

def send_msg(username, message):
    """create a new message and redirect back to chat page""" 
    return "{0}:{1}".format(username, message)



app.run(host=os.getenv('IP'), port=(os.getenv('PORT')), debug=True)