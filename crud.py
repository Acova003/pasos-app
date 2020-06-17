"""CRUD operations."""
# from model import db, User, connect_to_db

from model import db, User, Step, connect_to_db

def create_user(given_name, email):
    """Create and return a new user."""

    user = User(given_name=given_name, email=email)

    db.session.add(user)
    db.session.commit()
    print(user)
    return user

def get_users():
    """Return all users."""

    return User.query.all()

def get_user_by_id(user_id):
    """Return a user by primary key."""

    return User.query.get(user_id)

def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()

def create_step(user, title):
    """Create and return a new step."""

    step = Step(user=user, date=date, num_steps=num_steps)

    db.session.add(step)
    db.session.commit()

    return step
def find_steps_for_user(user, date):

    return Step.query.filter(Step.user == user, Step.date == date).first()

def count_steps_for_user(user):
    # 1. find all steps for this user
    # 2. add up in python
    #
    # 1. make query to ask DB to sum steps for user
    # Step.query.all()

    q = db.session.query(db.func.sum(Step.num_steps).label("total_steps")).filter(Step.user == user)
    return q.all()[0][0]

def create_steps_for_user(user, date, num_steps):
    step = Step(user=user, date=date, num_steps=num_steps)

    db.session.add(step)
    db.session.commit()

    return step
def update_num_steps(steps, new_num):
    steps.num_steps = new_num
    db.session.commit()
    return steps

def get_trips():

    return Trip.query.all()

def get_trip_by_id(trip_id):
    """Return a trip by primary key."""

    return Trip.query.get(trip_id)

def create_location(trip, title, longitude, latitude, city_name, body):
    """Create and return a new location."""

    location = Location(trip=trip, title=title, longitude=longitude,
    latitude=latitude, city_name=city_name, body=body)

    db.session.add(location)
    db.session.commit()

    return location

def get_locations():

    return Location.query.all()

def get_location_by_id(pin_id):
    """Return a location by primary key."""

    return Trip.query.get(trip_id)

def create_image(location, name, path):
    """Create and return a new image."""

    image = Image(location=location, name=name, path=path)

    db.session.add(image)
    db.session.commit()

    return image

def get_images():

    return Image.query.all()

def get_image_by_id(image_id):
    """Return a location by primary key."""

    return Image.query.get(image_id)

# def calculate_location()

if __name__ == '__main__':
    from server import app
    connect_to_db(app)
