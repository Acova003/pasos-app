"""Backend Flask Server for Pasos app."""

from flask import (Flask, request, flash, session, redirect, render_template, url_for)
from model import db, connect_to_db
from flask_dance.contrib.google import make_google_blueprint, google
from oauthlib.oauth2.rfc6749.errors import TokenExpiredError
from werkzeug.contrib.fixers import ProxyFix
from jinja2 import StrictUndefined
from google.oauth2.credentials import Credentials
from google.auth.transport.urllib3 import AuthorizedHttp
from datetime import datetime
from google_fit_steps import get_steps_from_api
from helpers import get_location


import os
import crud
import google_auth_httplib2
import httplib2
import json

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.wsgi_app = ProxyFix(app.wsgi_app)
app.secret_key = os.environ.get('SECRET_KEY')
blueprint = make_google_blueprint(
    client_id=os.environ.get('CLIENT_ID'),
    client_secret=os.environ.get('CLIENT_SECRET'),
    scope=[
        "openid",
        "https://www.googleapis.com/auth/userinfo.email",
        "https://www.googleapis.com/auth/userinfo.profile",
        "https://www.googleapis.com/auth/fitness.activity.read",
    ],
)
app.register_blueprint(blueprint, url_prefix="/login")

@app.route("/test")
def test():
    given_name = "Amee"
    num_steps = 1300
    new_steps = 250
    kms = num_steps * 0.008
    distance_to_santiago = int(780 - kms)
    location = get_location(kms)

    return render_trip(given_name, num_steps, new_steps, location, distance_to_santiago)

@app.route("/")
def index():
    if not google.authorized:
        return redirect(url_for("google.login"))

    creds = Credentials(google.token['access_token'])
    print(google.token)
    http = AuthorizedHttp(creds)

    try:
        response = http.request('GET', 'https://people.googleapis.com/v1/people/me?personFields=names,emailAddresses')

    except:
        return redirect(url_for('google.login'))

    print(response.data)
    response_json = json.loads(response.data)
    email_address = response_json["emailAddresses"][0]['value']
    given_name = response_json["names"][0]['givenName']
    user_matched = crud.get_user_by_email(email_address)
    # step_count = user_matched.step_count
    # if user_matched isn't in db, call people api, get given name. Use given_name, email_address and step count
    # to initialize new user at 0 steps
    if user_matched is None:
        user_matched = crud.create_user(given_name, email_address)
        # value = "Buen Camino, peregrino! Welcome to Pasos"

    new_steps = get_steps_from_api(creds)

    date = datetime.today().date()
    steps = crud.find_steps_for_user(user_matched, date)
    if steps is None:
        steps = crud.create_steps_for_user(user_matched, date, new_steps)
    else:
        steps = crud.update_num_steps(steps, new_steps)

    num_steps = crud.count_steps_for_user(user_matched)
    kms = num_steps * 0.008
    location = get_location(kms)
    kms_traveled = location.distance_in
    #display rounded during deployment
    distance_to_santiago = int(780 - kms_traveled)

    return render_trip(given_name, num_steps, new_steps, location, distance_to_santiago)

def render_trip(name, num_steps, new_steps, location, distance_to_santiago):
    return render_template("trip.html", given_name=name, step_count=num_steps,\
        today_steps=new_steps, location=location, distance_to_santiago=distance_to_santiago)


# profile page route
#2,435 steps per mile
#1,550 steps per km
if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
