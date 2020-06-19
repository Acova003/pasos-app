"""Script to seed database."""

import os
import json
import crud
import model
import server

from model import User, Step, Location
from model import connect_to_db, db
from server import app

os.system('dropdb pasos')
os.system('createdb pasos')

model.connect_to_db(server.app)
model.db.create_all()

def seed_users():
# Load location data from JSON file
    with open('data/users.json') as f:
        user_data = json.loads(f.read())

    # to create locations
    print(user_data)
    for user in user_data:
        given_name, email = (user['given_name'],
                                        user['email'])

        crud.create_user(given_name, email)

def seed_steps():
# Load location data from JSON file

    with open('data/steps.json') as f:
        step_data = json.loads(f.read())

    # to create locations
    for step in step_data:
        user_id, date, num_steps = (step['user_id'], step['date'], step['num_steps'])

        user = crud.get_user_by_id(user_id)
        print(user)
        crud.create_trip(user, date, num_steps)


def seed_locations():
# Load location data from JSON file

    with open('data/locations.json') as f:
        location_data = json.loads(f.read())

    # to create locations
    for distance,location in location_data.items():
        latitude = location['lat']
        longitude = location['lon']

        crud.create_location(latitude, longitude, float(distance))



    print('Success!')
