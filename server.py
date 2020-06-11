"""Backend Flask Server for Pasos app."""

import time
from flask import (Flask, request, flash, session, redirect, render_template)
from model import Trip, db, connect_to_db
# from flask_oauth import OAuth
import crud

app = Flask(__name__)

@app.route('/time')
def get_current_time():
    print('test')
    return {'time': time.time()}

@app.route("/")
def hello():
    trips = crud.get_trips()
    return render_template('index.html', trips=trips)


# @app.route('/index.html')
# def index():
#     pass
#     # read index.html into memory
#     # send it down the network
#
# @app.route('/app.js')
# def index():
#     pass
#     # read app.js into memory
#     # send it down the network



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
