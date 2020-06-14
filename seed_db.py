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
        given_name, email, step_count = (user['given_name'],
                                        user['email'],
                                        user['step_count'])

        crud.create_user(given_name, email, step_count)

def seed_trips():
# Load location data from JSON file
    # seed_users()

    with open('data/trips.json') as f:
        trip_data = json.loads(f.read())

    # to create locations
    for trip in trip_data:
        user_id, title = (trip['user_id'], trip['title'])

        user = crud.get_user_by_id(user_id)
        print(user)
        crud.create_trip(user, title)

def seed_locations():
# Load location data from JSON file
    # seed_trips()

    with open('data/locations.json') as f:
        location_data = json.loads(f.read())

    # to create locations
    for location in location_data:
        trip_id = location['trip_id']
        title = location['title']
        step_count = location['step_count']
        longitude = location['longitude']
        latitude = location['latitude']
        city_name = location['city_name']
        body = location['body']
        user_id = location['user_id']

        trip = crud.get_trip_by_id(trip_id)
        crud.create_location(trip, title, step_count, longitude, latitude,
                            city_name, body, user_id)

def seed_images():
    # Load image data from JSON file
    seed_locations()

    with open('data/images.json') as f:
        image_data = json.loads(f.read())

    # to create locations
    for image in image_data:
        pin_id = image['pin_id']
        trip_id = image['trip_id']
        user_id = image['user_id']
        name = image['name']
        path = image['path']

        location = crud.get_location_by_id(pin_id)
        crud.create_image(location, title, trip_id, user_id, name, path)

    print('Success!')
