from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SelectMultipleField, DateTimeField, BooleanField
from wtforms.fields.core import IntegerField 
from wtforms.validators import DataRequired, AnyOf, URL

class EventForm(FlaskForm):
    event_name = StringField(
        'event_name', validators=[DataRequired()]
    )
    event_date = DateTimeField(
        'event_date',
        validators=[DataRequired()],
        default= datetime.today()
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
        