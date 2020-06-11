"""Models for Pasos app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String, nullable=False, unique=True)
    display_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String)
    step_count = db.Column(db.Integer)

    def __repr__(self):
        return f'<User user_id={self.user_id} username={self.username} step_count={self.step_count}>'


class Trip(db.Model):
    """A trip."""

    __tablename__ = 'trips'

    trip_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    title = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f'<Trip trip_id={self.trip_id} user_id={self.user_id} title={self.title}>'


class Location(db.Model):
    """A pin location."""

    __tablename__ = 'locations'

    pin_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    trip_id = db.Column(db.Integer, db.ForeignKey('trips.trip_id'))
    title = db.Column(db.String)
    longitude = db.Column(db.Float)
    latitude = db.Column(db.Float)
    city_name = db.Column(db.String)
    body = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))


    trip = db.relationship('Trip', backref='locations')
    user = db.relationship('User', backref='locations')

    def __repr__(self):
        return f'<Location pin_id={self.pin_id} title={self.title}>'

class Image(db.Model):
    """A pin location."""

    __tablename__ = 'images'

    image_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    pin_id = db.Column(db.Integer, db.ForeignKey('locations.pin_id'))
    trip_id = db.Column(db.Integer, db.ForeignKey('trips.trip_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    name = db.Column(db.String, nullable=False)
    path = db.Column(db.String, nullable=False)

    location = db.relationship('Location', backref='images')
    trip = db.relationship('Trip', backref='images')
    user = db.relationship('User', backref='images')

    def __repr__(self):
        return f'<Image image_id={self.image_id} name={self.name}>'


def connect_to_db(flask_app, db_uri='postgresql:///pasos', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')



if __name__ == '__main__':
    from server import app

    connect_to_db(app)
