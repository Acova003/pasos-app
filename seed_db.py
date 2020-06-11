"""Script to seed database."""

import os
import json
import crud

from model import User, Trip, Location, Image
from model import connect_to_db, db
from api import app

os.system('dropdb pasos')
os.system('createdb pasos')

model.connect_to_db(api.app)
model.db.create_all()

def seed_users():
# Load location data from JSON file
    with open('data/users.json') as f:
        user_data = json.loads(f.read())

    # to create locations
    for user in user_data:
        title, overview, poster_path = (movie['title'],
                                        movie['overview'],
                                        movie['poster_path'])
        release_date = datetime.strptime(movie['release_date'], '%Y-%m-%d')

        db_movie = crud.create_movie(title,
                                     overview,
                                     release_date,
                                     poster_path)
        movies_in_db.append(db_movie)

def seed_locations():
# Load location data from JSON file
    with open('data/locations.json') as f:
        location_data = json.loads(f.read())

    # to create locations
    for location in location_data:
        title, overview, poster_path = (movie['title'],
                                        movie['overview'],
                                        movie['poster_path'])
        release_date = datetime.strptime(movie['release_date'], '%Y-%m-%d')

        db_movie = crud.create_movie(title,
                                     overview,
                                     release_date,
                                     poster_path)
        movies_in_db.append(db_movie)

# Create 10 users; each user will make 10 ratings
for n in range(10):
    email = f'user{n}@test.com'  # Voila! A unique email!
    password = 'test'

    user = crud.create_user(email, password)

    for _ in range(10):
        random_movie = choice(movies_in_db)
        score = randint(1, 5)

        crud.create_rating(user, random_movie, score)
