from flask_dance.contrib.google import make_google_blueprint, google
from google.oauth2.credentials import Credentials
from google.auth.transport.urllib3 import AuthorizedHttp
from flask import (Flask, request, flash, session, redirect, render_template, url_for)
import crud
from google_fit_steps import get_steps_from_api
from model import Location
from datetime import datetime
import os
import json


def get_location(distance_in):


    # to create locations
    #query to match distances less than distance traveled
    return Location.query.filter(Location.distance_in <= distance_in).order_by(Location.distance_in.desc()).first()

            # latitude = location['lat']
            # longitude = location['lon']

        # print(distance)
        #write sql query to get list of distance
    # geolocation = [latitude, longitude]
    # print(geolocation)

def handling_authorization(creds, response):
    print(response.data)
    response_json = json.loads(response.data)
    print('{{{{{{{{{{{{{{{{{{{{}}}}}}}}}}}}}}}}}}}}')
    email_address = response_json["emailAddresses"][0]['value']
    print(response_json)

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
    google_url = os.environ.get('GOOGLE_URL')
    print({given_name: given_name, num_steps: num_steps, new_steps: new_steps, location: location,
     distance_to_santiago: distance_to_santiago, google_url: google_url})
    print("************")

    return {"given_name": given_name, "num_steps": num_steps, "new_steps": new_steps, "location": location,
     "distance_to_santiago": distance_to_santiago, "google_url": google_url}
