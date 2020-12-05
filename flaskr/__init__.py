from flask import Flask, render_template, g, request, Response, flash, redirect, url_for, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from flask_cors import CORS
from .models import setup_db, Fighter, Division, Event
from functools import wraps
import json
import babel
from babel.dates import format_date, format_datetime, format_time
import dateutil.parser
from os import environ as env
from werkzeug.exceptions import HTTPException

from dotenv import load_dotenv, find_dotenv
from authlib.integrations.flask_client import OAuth
from six.moves.urllib.parse import urlencode

from . import constants


ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

AUTH0_CALLBACK_URL = env.get(constants.AUTH0_CALLBACK_URL)
AUTH0_CLIENT_ID = env.get(constants.AUTH0_CLIENT_ID)
AUTH0_CLIENT_SECRET = env.get(constants.AUTH0_CLIENT_SECRET)
AUTH0_DOMAIN = env.get(constants.AUTH0_DOMAIN)
AUTH0_BASE_URL = 'https://' + AUTH0_DOMAIN
AUTH0_AUDIENCE = env.get(constants.AUTH0_AUDIENCE)

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__, instance_relative_config=True)
  setup_db(app)


  
  #This sets up CORS to Allow '*' for origins. 
  CORS(app)

  app.secret_key = constants.SECRET_KEY
  app.debug = True

  #----------------------------------------------------------------------------#
  # Filters.
  #----------------------------------------------------------------------------#
  # use a string for the value arg when calling this function
  def format_datetime(value, format='medium'):
    date = dateutil.parser.parse(value)
    if format == 'full':
      format="EEEE MMMM, d, y 'at' h:mma"
    elif format == 'medium':
      format="EE MM, dd, y h:mma"
    return babel.dates.format_datetime(date, format)
  
  app.jinja_env.filters['datetime'] = format_datetime
  
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response
   
  #This endpoint handles GET requests for categories
  @app.errorhandler(Exception)
  def handle_auth_error(ex):
    response = jsonify(message=str(ex))
    response.status_code = (ex.code if isinstance(ex, HTTPException) else 500)
    return response


  oauth = OAuth(app)

  auth0 = oauth.register(
    'auth0',
    client_id=AUTH0_CLIENT_ID,
    client_secret=AUTH0_CLIENT_SECRET,
    api_base_url=AUTH0_BASE_URL,
    access_token_url=AUTH0_BASE_URL + '/oauth/token',
    authorize_url=AUTH0_BASE_URL + '/authorize',
    client_kwargs={
        'scope': 'openid profile email',
    },
  )


  def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if constants.PROFILE_KEY not in session:
            return redirect('/')
        return f(*args, **kwargs)

    return decorated


    # Controllers API
  @app.route('/')
  def home():
        return render_template('home.html')


  @app.route('/callback')
  def callback_handling():
        auth0.authorize_access_token()
        resp = auth0.get('userinfo')
        userinfo = resp.json()

        session[constants.JWT_PAYLOAD] = userinfo
        session[constants.PROFILE_KEY] = {
            'user_id': userinfo['sub'],
            'name': userinfo['name'],
            'picture': userinfo['picture']
        }
        return redirect('/index')


  @app.route('/login')
  def login():
        return auth0.authorize_redirect(redirect_uri=AUTH0_CALLBACK_URL, audience=AUTH0_AUDIENCE)


  @app.route('/logout')
  def logout():
        session.clear()
        params = {'returnTo': url_for('home', _external=True), 'client_id': AUTH0_CLIENT_ID}
        return redirect(auth0.api_base_url + '/v2/logout?' + urlencode(params))


  @app.route('/index')
  @requires_auth
  def get_all_fighters():
    #Here I get all the fighters
    all_fighters = Fighter.query.all()

    data = []

    for item in all_fighters:
      data.append(item.format())
    
    event_info = []
    event_data = Event.query.order_by(Event.event_date.desc())
    
    for item in event_data:
      event_info.append(
        {
            'event_name':item.event_name, 
            'event_date':format_datetime(str(item.event_date)), 
            'division':item.division,
            'fighter_1':item.fighter_1,
            'fighter_2':item.fighter_2,
            'fighter_1_votes':item.fighter_1_votes,
            'fighter_2_votes':item.fighter_2_votes,
            'fight_order':item.fight_order
        }
      )

    return render_template('index.html',
                              userinfo=session[constants.PROFILE_KEY],
                              userinfo_pretty=json.dumps(session[constants.JWT_PAYLOAD], indent=4), fighters = data, events = event_info)

  @app.route('/division_fighters/<int:division_id>')
  @requires_auth
  def get_division_fighters(division_id):
    #Here I get all the fighters - questions = Question.query.filter(Question.category==category_id).all()
    division_fighters = Fighter.query.filter(Fighter.division == division_id).all()

    data = []

    for item in division_fighters:
      data.append(item.format())
    
    event_info = []
    #event_data = Event.query.filter(Event.division == division_id).order_by(Event.event_date.desc()).limit(1)
    #print(f'This is event_data - {event_data}')
    event_data = Event.query.order_by(Event.event_date.desc())


    for item in event_data:
      event_info.append(
        {
            'event_name':item.event_name, 
            'event_date':format_datetime(str(item.event_date)), 
            'division':item.division,
            'fighter_1':item.fighter_1,
            'fighter_2':item.fighter_2,
            'fighter_1_votes':item.fighter_1_votes,
            'fighter_2_votes':item.fighter_2_votes,
            'fight_order':item.fight_order
        }
      )

    return render_template('division_fighters.html',
                              userinfo=session[constants.PROFILE_KEY],
                              userinfo_pretty=json.dumps(session[constants.JWT_PAYLOAD], indent=4), fighters = data, events = event_info)
    


  
    
  return app

    