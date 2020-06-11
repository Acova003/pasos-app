"""Backend Flask Server for Pasos app."""

from flask import (Flask, request, flash, session, redirect, render_template)
from model import Trip, db, connect_to_db
# from flask_oauth import OAuth
import crud

from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
connect_to_db(app)

@app.route("/")
def index():
    trips = [Trip(title='123')]
    # trips = crud.get_trips()
    return render_template('index.html', trips=trips)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
