"""Models for Pasos app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    given_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    # step_count = db.Column(db.Integer)

    def __repr__(self):
        return f'<User user_id={self.user_id} given_name={self.given_name} email={self.email}>'

class Step(db.Model):
    "A steps"

    __tablename__ = 'steps'

    step_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    date = db.Column(db.Date)
    num_steps = db.Column(db.Integer, nullable=False)

    user = db.relationship('User', backref='steps')

    def __repr__(self):
        return f'<Step step_id={self.step_id} user_id={self.user_id} date={self.date} num_steps={self.num_steps}>'

class Location(db.Model):
    """A pin location."""

    __tablename__ = 'locations'

    pin_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    distance_in = db.Column(db.Float)

    def __repr__(self):
        return f'<Location pin_id={self.pin_id} latitude={self.latitude} longitude={self.longitude} distance_in={self.distance_in}>'

#location_id, distance from the start, lon, lat, city name
# list
#query list of locations passed



def connect_to_db(flask_app):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'postgresql:///pasos')
    flask_app.config['SQLALCHEMY_ECHO'] = os.getenv('SQLALCHEMY_ECHO', false)
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the db!')
    print('ModelPy')



if __name__ == '__main__':
    from server import app

    connect_to_db(app)
