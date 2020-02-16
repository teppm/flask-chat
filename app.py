import os 
from flask import Flask, redirect

app = Flask(__name__)
message = []

def add_messages(username, message):
    """Add messages to messages list """ 

    message.append("{}:{}".format(username, message))


def get_all_message():
    """Get all message and separate with br"""

    return "<br>".join(message)


@app.route('/')

def index():

    """main page with instructions"""
    return "To send message use /USERNAME/MESSAGE"

app.route('/<username>')

def user(username):
    """Display chat messages""" 

    return "<h1>Welcom</h1>, {0}</h1>,{1}".format(username, get_all_message())

app.route('/<username>/<message>')


def send_msg(username, message):
    """create a new message and redirect back to chat page""" 

    add_messages(username, message)
    return redirect("/" + username)



app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)