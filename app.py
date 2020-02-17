import os 
from datetime import datetime
from flask import Flask, redirect, render_template, request, session


app = Flask(_name_)

app.secret_key = "1secret2key"

message = []

def add_messages(username, message):
    """Add messages to messages list """ 
    now = datetime.now().strftime("%H:%M:%S")
    message.append("({}){}:{}".format(now, username, message))


def get_all_message():
    """Get all message and separate with br"""

    return "<br>".join(message)


@app.route('/', methods=["GET", "POST"])

def index():

    """main page with instructions"""
    if request.method == "POST":
        session["username"] = request.form["username"]

    if "username" in session:
        return redirect(session["username"])

    return render_template("index.html")

app.route('/<username>')

def user(username):
    """Display chat messages""" 

    return "<h1>Welcome!</h1>, {0}</h1>,{1}".format(username, get_all_message())

app.route('/<username>/<message>')


def send_msg(username, message):
    """create a new message and redirect back to chat page""" 

    add_messages(username, message)
    return redirect("/" + username)



app.run(host=os.getenv('IP'), port=os.getenv('PORT'), debug=True)