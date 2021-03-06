import os
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


database_name = "ufcfan"

# Here we connect to Heroku database
database_path = os.environ.get('DATABASE_URL')

db = SQLAlchemy()
migrate = Migrate()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    moment = Moment(app)
    db.app = app
    db.init_app(app)
    migrate.init_app(app, db)

# Used in Multiple inheritance
class CrudHelper:
    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def rollback(self):
        db.session.rollback()

    def close(self):
        db.session.close()


# Creating the debatase for Actors
class Fighter(db.Model, CrudHelper):
    __tablename__ = 'fighters'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    age = db.Column(db.Integer)
    height = db.Column(db.Float)
    weight = db.Column(db.Float)
    arm_reach = db.Column(db.Float)
    leg_reach = db.Column(db.Float)
    sex = db.Column(db.String(1))
    win = db.Column(db.Integer)
    loss = db.Column(db.Integer)
    draw = db.Column(db.Integer)
    division = db.Column(db.Integer, db.ForeignKey('divisions.id'))
    rank = db.Column(db.Integer)

    def __repr__(self):
        return f"<Fighter id='{self.id}' first_name='{self.first_name}' \
                last_name='{self.last_name}' age='{self.age}'\
                height='{self.height}' weight='{self.weight}' \
                arm_reach='{self.arm_reach}' leg_reach='{self.leg_reach}' \
                sex='{self.sex}' win='{self.win}' loss='{self.loss}' \
                draw='{self.draw}' division = '{self.division}' \
                rank='{self.rank}'>"

    def __init__(self, first_name, last_name, age, height, weight,
                 arm_reach, leg_reach, sex, win, loss, draw, division, rank):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height
        self.weight = weight
        self.arm_reach = arm_reach
        self.leg_reach = leg_reach
        self.sex = sex
        self.win = win
        self.loss = loss
        self.draw = draw
        self.division = division
        self.rank = rank

    def format(self):
        return{
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age,
            'height': self.height,
            'weight': self.weight,
            'arm_reach': self.arm_reach,
            'leg_reach': self.leg_reach,
            'sex': self.sex,
            'win': self.win,
            'loss': self.loss,
            'draw': self.draw,
            'division': self.division,
            'rank': self.rank,
        }


class Division(db.Model, CrudHelper):
    __tablename__ = 'divisions'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    weight = db.Column(db.Integer)
    fighters = db.relationship('Fighter', backref='division_f',
                               lazy='select', cascade='all, delete-orphan')
    events = db.relationship('Event', backref='division_e', lazy='select',
                             cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Division id='{self.id}' name='{self.name}' \
                weight='{self.weight}' >"

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def format(self):
        return{
            'id': self.id,
            "name": self.name,
            "weight": self.weight,
        }


class Event(db.Model, CrudHelper):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String)
    event_date = db.Column(db.DateTime)
    location = db.Column(db.String)
    division = db.Column(db.Integer, db.ForeignKey('divisions.id'))
    fighter_1 = db.Column(db.String)
    fighter_2 = db.Column(db.String)
    fighter_1_votes = db.Column(db.Integer, default=0)
    fighter_2_votes = db.Column(db.Integer, default=0)
    fighter_1_odds = db.Column(db.Integer, default=0)
    fighter_2_odds = db.Column(db.Integer, default=0)
    fight_order = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f"<Event id='{self.id}' event_name='{self.event_name}' \
                event_date='{self.event_date}' location='{self.location}'\
                division='{self.division}' fighter_1='{self.fighter_1}' \
                fighter_2='{self.fighter_2}' \
                fighter_1_votes='{self.fighter_1_votes}' \
                fighter_2_votes='{self.fighter_2_votes}' \
                fighter_1_odds = '{self.fighter_1_odds}' \
                fighter_2_odds = '{self.fighter_2_odds}' \
                fight_order='{self.fight_order}' >"

    def __init__(self, event_name, event_date, location, division,
                 fighter_1, fighter_2, fighter_1_votes, fighter_2_votes,
                 fighter_1_odds, fighter_2_odds, fight_order) -> None:
        self.event_name = event_name
        self.event_date = event_date
        self.location = location
        self.division = division
        self.fighter_1 = fighter_1
        self.fighter_2 = fighter_2
        self.fighter_1_votes = fighter_1_votes
        self.fighter_2_votes = fighter_2_votes
        self.fighter_1_odds = fighter_1_odds
        self.fighter_2_odds = fighter_2_odds
        self.fight_order = fight_order

    def format(self):
        return {
            'id': self.id,
            'event_name': self.event_name,
            'event_date': self.event_date,
            'location': self.location,
            'division': self.division,
            'fighter_1': self.fighter_1,
            'fighter_2': self.fighter_2,
            'fighter_1_votes': self.fighter_1_votes,
            'fighter_2_votes': self.fighter_2_votes,
            'fighter_1_odds': self.fighter_1_odds,
            'fighter_2_odds': self.fighter_2_odds,
            'fight_order': self.fight_order
        }
