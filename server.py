"""Backend Flask Server for Pasos app."""

from flask import (Flask, request, flash, session, redirect, render_template, url_for)
from model import Trip, db, connect_to_db
from flask_dance.contrib.google import make_google_blueprint, google
from oauthlib.oauth2.rfc6749.errors import TokenExpiredError
from werkzeug.contrib.fixers import ProxyFix
from jinja2 import StrictUndefined
from google.oauth2.credentials import Credentials
from google.auth.transport.urllib3 import AuthorizedHttp

import os
import crud
import google_auth_httplib2
import httplib2

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
connect_to_db(app)
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
    ],
)
app.register_blueprint(blueprint, url_prefix="/login")

@app.route("/")
def index():
    if not google.authorized:
        return redirect(url_for("google.login"))

    creds = Credentials(google.token['access_token'])
    print(google.token)
    http = AuthorizedHttp(creds)

    try:
        response = http.request('GET', 'https://people.googleapis.com/v1/people/me?personFields=names')
    except:
        return redirect(url_for('google.login'))

    print(response.data)
    print(response.status)
    return response.data


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
