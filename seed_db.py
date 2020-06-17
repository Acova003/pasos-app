"""Script to seed database."""

import os
import json
import crud
import model
import server

from model import User, Trip, Location, Image
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


# def seed_locations():
# # Load location data from JSON file
#
#     with open('data/locations.json') as f:
#         location_data = json.loads(f.read())
#
#     # to create locations
#     for location in location_data:
#         trip_id = location['trip_id']
#         title = location['title']
#         step_count = location['step_count']
#         longitude = location['longitude']
#         latitude = location['latitude']
#         city_name = location['city_name']
#         body = location['body']
#         user_id = location['user_id']
#
#         trip = crud.get_trip_by_id(trip_id)
#         crud.create_location(trip, title, step_count, longitude, latitude,
#                             city_name, body, user_id)
#


    print('Success!')
