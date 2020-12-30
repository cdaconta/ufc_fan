from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import (StringField, FloatField,
                     SelectField, SelectMultipleField,
                     DateTimeField, BooleanField)
from wtforms.fields.core import IntegerField
from wtforms.validators import DataRequired, AnyOf, URL


class EventForm(FlaskForm):
    event_name = StringField(
        'event_name', validators=[DataRequired()]
    )
    event_date = DateTimeField(
        'event_date',
        validators=[DataRequired()],
        default=datetime.today()
    )
    location = StringField(
        'location', validators=[DataRequired()]
    )
    division = IntegerField(
        'division', validators=[DataRequired()]
    )
    fighter_1 = StringField(
        'fighter_1', validators=[DataRequired()]
    )
    fighter_2 = StringField(
        'fighter_2', validators=[DataRequired()]
    )
    fighter_1_odds = IntegerField(
        'fighter_1_odds', validators=[DataRequired()]
    )
    fighter_2_odds = IntegerField(
        'fighter_2_odds', validators=[DataRequired()]
    )

    fight_order = IntegerField(
        'fight_order', validators=[DataRequired()]
    )


class FighterForm(FlaskForm):
    first_name = StringField(
        'first_name', validators=[DataRequired()]
    )
    last_name = StringField(
        'last_name', validators=[DataRequired()]
    )
    age = IntegerField(
        'age',
        validators=[DataRequired()]
    )
    height = FloatField(
        'height', validators=[DataRequired()]
    )
    weight = FloatField(
        'weight', validators=[DataRequired()]
    )
    arm_reach = FloatField(
        'arm_reach', validators=[DataRequired()]
    )
    leg_reach = FloatField(
        'leg_reach', validators=[DataRequired()]
    )
    sex = StringField(
        'sex', validators=[DataRequired()]
    )
    win = IntegerField(
        'win', validators=[DataRequired()]
    )

    loss = IntegerField(
        'loss', validators=[DataRequired()]
    )
    draw = IntegerField(
        'draw', validators=[DataRequired()]
    )

    division = IntegerField(
        'division', validators=[DataRequired()]
    )
    rank = IntegerField(
        'rank', validators=[DataRequired()]
    )
