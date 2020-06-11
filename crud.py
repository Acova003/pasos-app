"""CRUD operations."""
# from model import db, User, connect_to_db

from model import db, User, Trip, Location, Image, connect_to_db

def create_user(username, password):
    """Create and return a new user."""

    user = User(username=username, password=password)

    # user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    # username = db.Column(db.String, unique=True)
    # display_name = db.Column(db.String)
    # email = db.Column(db.String, unique=True)
    # password = db.Column(db.String)
    # step_count = db.Column(db.Integer)

    db.session.add(user)
    db.session.commit()

    return user

def get_users():
    """Return all users."""

    return User.query.all()

def get_trips():

    return Trip.query.all()

if __name__ == '__main__':
    from server import app
    connect_to_db(app)
