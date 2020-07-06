"""Backend Flask Server for Pasos app."""

from flask import (Flask, request, flash, session, redirect, render_template, url_for)
from model import db, connect_to_db
from flask_dance.contrib.google import make_google_blueprint, google
from flask_login import logout_user
from oauthlib.oauth2.rfc6749.errors import TokenExpiredError
from werkzeug.middleware.proxy_fix import ProxyFix
from jinja2 import StrictUndefined
from google.oauth2.credentials import Credentials
from google.auth.transport.urllib3 import AuthorizedHttp
from datetime import datetime
from google_fit_steps import get_steps_from_api
import helpers
import traceback


import os
import sys
import crud
import google_auth_httplib2
import httplib2
import json

from dotenv import load_dotenv
load_dotenv()

redirect_url = os.environ.get("REDIRECT_URL", "http://localhost:5002/trip")

app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.wsgi_app = ProxyFix(app.wsgi_app)
app.secret_key = os.environ.get('SECRET_KEY')
blueprint = make_google_blueprint(
    client_id=os.environ.get('CLIENT_ID'),
    client_secret=os.environ.get('CLIENT_SECRET'),
    redirect_url=redirect_url,
    scope=[
        "openid",
        "https://www.googleapis.com/auth/userinfo.email",
        "https://www.googleapis.com/auth/userinfo.profile",
        "https://www.googleapis.com/auth/fitness.activity.read",
    ],
)
app.register_blueprint(blueprint, url_prefix="/login")

@app.route("/juliana")
def user_1():
    # given_name = "Amee"
    # num_steps = 15000
    # new_steps = 250
    # kms = num_steps * 0.00076
    # distance_to_santiago = int(807 - kms)
    # location = helpers.get_location(800)
    # # location = get_location(kms)
    # google_url = os.environ.get('GOOGLE_URL')
    info_dict = {"given_name": "Juliana",
    "num_steps": 0,
    "new_steps": 250,
    "location": helpers.get_location(0),
    "distance_to_santiago": int(807 - (0 * 0.00076)),
    "google_url": os.environ.get('GOOGLE_URL')
    }

    return render_trip(info_dict)

@app.route("/francisco")
def user_2():
    # given_name = "Amee"
    # num_steps = 15000
    # new_steps = 250
    # kms = num_steps * 0.00076
    # distance_to_santiago = int(807 - kms)
    # location = helpers.get_location(800)
    # # location = get_location(kms)
    # google_url = os.environ.get('GOOGLE_URL')
    info_dict = {"given_name": "Francisco",
    "num_steps": 300000,
    "new_steps": 250,
    "location": helpers.get_location(579),
    "distance_to_santiago": int(807 - (300000 * 0.00076)),
    "google_url": os.environ.get('GOOGLE_URL')
    }

    return render_trip(info_dict)

@app.route("/hannah")
def user_3():
    # given_name = "Amee"
    # num_steps = 15000
    # new_steps = 250
    # kms = num_steps * 0.00076
    # distance_to_santiago = int(807 - kms)
    # location = helpers.get_location(800)
    # # location = get_location(kms)
    # google_url = os.environ.get('GOOGLE_URL')
    info_dict = {"given_name": "Hannah",
    "num_steps": 104000,
    "new_steps": 250,
    "location": helpers.get_location(808),
    "distance_to_santiago": 0,
    "google_url": os.environ.get('GOOGLE_URL')
    }

    return render_trip(info_dict)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/trip")
def trip():
    # helpers.handling_authorization()

    if not google.authorized:
        return redirect(url_for('google.login'))
    creds = Credentials(google.token['access_token'])
    print(google.token)
    http = AuthorizedHttp(creds)

    try:
        response = http.request('GET', 'https://people.googleapis.com/v1/people/me?personFields=names,emailAddresses')
        auth = helpers.handling_authorization(creds, response)
        return render_trip(auth)

    except Exception as e:
        print("Exception in auth:")
        print(repr(e))
        return redirect(url_for('google.login'))

@app.route("/logout")
def logout():
    token = blueprint.token["access_token"]
    resp = google.post(
        "https://accounts.google.com/o/oauth2/revoke",
        params={"token": token},
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    assert resp.ok, resp.text
    del blueprint.token  # Delete OAuth token from storage
    return redirect("/")

@app.route("/draft")
def draft():
    return render_template("draft.html")

def render_trip(info_dict):
    return render_template("trip.html", given_name=info_dict["given_name"], step_count=info_dict["num_steps"],\
        today_steps=info_dict["new_steps"], location=info_dict["location"], distance_to_santiago=info_dict["distance_to_santiago"],\
        GOOGLE_URL=info_dict["google_url"])


# profile page route
#2,435 steps per mile
#1,550 steps per km
if __name__ == '__main__':
    connect_to_db(app)
    port = os.getenv('PORT', '5000')
    app.run(host='0.0.0.0', port=port, debug=True)
