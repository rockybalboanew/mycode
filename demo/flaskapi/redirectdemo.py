#!/usr/bin/python3
"""Alta3 Research
Example of applying limiting to our flask APIs using Flask-Limiter"""

# NEW
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from flask import Flask
from flask import redirect
from flask import url_for
from flask import render_template
from flask import request
from flask import abort

app = Flask(__name__)

pic_location= "https://static.alta3.com/courses/api/lec_flaskcontrol_python/dont-panic.png"

# create a limiter object from Limiter
# limits are being performed by tracking the
# REMOTE ADDRESS of the clients
limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

# if user sends GET to / (root)
@app.route("/")
def index():
    return render_template("towel.html", pic= pic_location)   # found in templates/

# if user sends GET or POST to /login
@app.route("/login", methods = ["POST", "GET"])
@limiter.limit("3 per day")
def login():
    # if user sent a POST
    if request.method == "POST":
        # if the POST contains '42' as the value for 'answer'
        if request.form["answer"] == "42" :
            return redirect(url_for("success")) # return a 302 redirect to /success
        else:
            return redirect(url_for("fail"))    # return a 302 redirect to /fail
    elif request.method == "GET":
        return redirect(url_for("index")) # if they sent a GET to /login send 302 redirect to /

@app.route("/httpfail")
def httpfail():
    abort(406)  # send back a HTTP failure

@app.route("/fail")
def fail():
    return "That was not correct." # nothing wrong with HTTP layer, we just indicating that the user responded incorrectly

@app.route("/success")
def success():
    return "Correct!"

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224)
















































