"""Backend Flask Server for Pasos app."""

from flask import (Flask, request, flash, session, redirect, render_template, url_for)
from model import Trip, db, connect_to_db
from flask_dance.contrib.google import make_google_blueprint, google
from werkzeug.contrib.fixers import ProxyFix
import dotenv
import os
import crud

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
connect_to_db(app)
app.wsgi_app = ProxyFix(app.wsgi_app)
app.secret_key = os.getenv('SECRET_KEY')
blueprint = make_google_blueprint(
    client_id=os.getenv('CLIENT_ID'),
    client_secret=os.getenv('CLIENT_SECRET'),
    scope=["profile", "email"]
)
app.register_blueprint(blueprint, url_prefix="/login")

@app.route("/")
def index():
    if not google.authorized:
        return redirect(url_for("google.login"))
    resp = google.get("/plus/v1/people/me")
    assert resp.ok, resp.text
    return "You are {email} on Google".format(email=resp.json()["emails"][0]["value"])

# @app.route("/")
# def index():
#     trips = [Trip(title='123')]
#     # trips = crud.get_trips()
#     return render_template('index.html', trips=trips)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
