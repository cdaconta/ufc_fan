from flask import Flask, render_template, g, abort, request, jsonify, Response, flash, redirect, url_for, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text, or_
from flask_cors import CORS
from .models import setup_db, db, Fighter, Division, Event
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
from .auth import AuthError, requires_auth

from . import constants
from .forms import EventForm, FighterForm
import html

#Authentication data variables
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
  # Filter
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
  #----------------------------------------------------------------------------#
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS,PATCH')
    return response
   
  @app.errorhandler(Exception)
  def handle_auth_error(ex):
    response = jsonify(message=str(ex))
    response.status_code = (ex.code if isinstance(ex, HTTPException) else 500)
    return response

  def login_address():
    address = 'https://'
    address += AUTH0_DOMAIN
    address += '/authorize?'
    address += 'audience=' + AUTH0_AUDIENCE + '&'
    address += 'response_type=token&'
    address += 'client_id=' + AUTH0_CLIENT_ID + '&'
    address += 'redirect_uri=' + AUTH0_CALLBACK_URL
    return address
  # add login_address function to jinja context
  app.jinja_env.globals.update(login_address=login_address)

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


  # Controllers API
  @app.route('/')
  def home():
        return render_template('home.html')


  @app.route('/callback')
  def callback_handling():
        token = auth0.authorize_access_token()
        resp = auth0.get('userinfo')
        userinfo = resp.json()
        
        session[constants.JWT_PAYLOAD] = userinfo
        session[constants.PROFILE_KEY] = {
            'user_id': userinfo['sub'],
            'name': userinfo['name'],
            'picture': userinfo['picture']
        }
        session[constants.JWT] = token['access_token']
        
        return redirect('/index')
       

  @app.route('/login')
  def login():
        return auth0.authorize_redirect(redirect_uri=AUTH0_CALLBACK_URL, audience=AUTH0_AUDIENCE)


  @app.route('/logout')
  def logout():
        session.clear()
        params = {'returnTo': url_for('home', _external=True), 'client_id': AUTH0_CLIENT_ID}
        return redirect(auth0.api_base_url + '/v2/logout?' + urlencode(params))

  @app.route('/api-key')
  def get_api_key():
    return render_template('api_key.html')

  @app.route('/index')
  def get_all_fighters():

      session['Admin'] = env.get('APP_ADMIN')
      session['Event Editor'] = env.get('EVENT_EDITOR')

      #Here I get all the fighter by division
      div_1 = Fighter.query.filter(Fighter.division == 1).order_by(Fighter.rank).all()
      div_1_data = [item.format() for item in div_1]

      div_2 = Fighter.query.filter(Fighter.division == 2).order_by(Fighter.rank).all()
      div_2_data = [item.format() for item in div_2]

      div_3 = Fighter.query.filter(Fighter.division == 3).order_by(Fighter.rank).all()
      div_3_data = [item.format() for item in div_3]

      div_4 = Fighter.query.filter(Fighter.division == 4).order_by(Fighter.rank).all()
      div_4_data = [item.format() for item in div_4]

      div_5 = Fighter.query.filter(Fighter.division == 5).order_by(Fighter.rank).all()
      div_5_data = [item.format() for item in div_5]

      div_6 = Fighter.query.filter(Fighter.division == 6).order_by(Fighter.rank).all()
      div_6_data = [item.format() for item in div_6]

      div_7 = Fighter.query.filter(Fighter.division == 7).order_by(Fighter.rank).all()
      div_7_data = [item.format() for item in div_7]

      div_8 = Fighter.query.filter(Fighter.division == 8).order_by(Fighter.rank).all()
      div_8_data = [item.format() for item in div_8]

      div_9 = Fighter.query.filter(Fighter.division == 9).order_by(Fighter.rank).all()
      div_9_data = [item.format() for item in div_9]

      div_10 = Fighter.query.filter(Fighter.division == 10).order_by(Fighter.rank).all()
      div_10_data = [item.format() for item in div_10]

      div_11 = Fighter.query.filter(Fighter.division == 11).order_by(Fighter.rank).all()
      div_11_data = [item.format() for item in div_11]

      div_12 = Fighter.query.filter(Fighter.division == 12).order_by(Fighter.rank).all()
      div_12_data = [item.format() for item in div_12]
      
      event_info = []
      event_data = Event.query.order_by(Event.event_date.desc()).limit(1)
      
      event_info.append(
          {
              'event_name':event_data[0].event_name, 
              'event_date':format_datetime(str(event_data[0].event_date)), 
              'location':event_data[0].location,         
          }
        )
      session['Upcoming Event'] = '/event/' + format_datetime(str(event_data[0].event_date))
      return render_template('index.html',
                                userinfo=session[constants.PROFILE_KEY],
                                userinfo_pretty=json.dumps(session[constants.JWT_PAYLOAD], indent=4), events = event_info, div_1 = div_1_data, div_2 = div_2_data, div_3 = div_3_data, div_4 = div_4_data, div_5 = div_5_data, div_6 = div_6_data, div_7 = div_7_data, div_8 = div_8_data, div_9 = div_9_data, div_10 = div_10_data, div_11 = div_11_data, div_12 = div_12_data)

  @app.route('/knockouts')
  def get_knockout_page():
    return render_template('knockouts.html',  userinfo=session[constants.PROFILE_KEY])

  @app.route('/division_fighters/<int:division_id>')
  def get_division_fighters(division_id):
    #Here I join Fighters and Divisions Tables
    division_fighters = db.session.query(Fighter,Division).join(Division).filter(Fighter.division == division_id).all()

    data = []

    for fighter, division in division_fighters:
      data.append({
                  'id':fighter.id,
                  'first_name':fighter.first_name,
                  'last_name':fighter.last_name,
                  'age':fighter.age,
                  'height':fighter.height,
                  'weight':fighter.weight,
                  'arm_reach':fighter.arm_reach,
                  'leg_reach':fighter.leg_reach,
                  'sex':fighter.sex,
                  'win':fighter.win,
                  'loss':fighter.loss,
                  'draw':fighter.draw,
                  'division':fighter.division,
                  'rank':fighter.rank,
                  'div_id':division.id,
                  'div_name':division.name,
                  }
                )
    return render_template('division_fighters.html',
                              userinfo=session[constants.PROFILE_KEY],
                              userinfo_pretty=json.dumps(session[constants.JWT_PAYLOAD], indent=4), fighters = data) 
  
  @app.route('/event/<date>')
  def get_event(date):
    clean_date = html.unescape(date)
    event_info = []
    #event_data = Event.query.order_by(Event.event_date.desc()).limit(6)
    event_data = Event.query.filter(Event.event_date == clean_date).order_by(Event.fight_order)
   
    for item in event_data:
        event_info.append(
          {
              'event_name':item.event_name, 
              'event_date':format_datetime(str(item.event_date)),
              'location':item.location, 
              'division':item.division,
              'fighter_1':item.fighter_1,
              'fighter_2':item.fighter_2,
              'fighter_1_votes':item.fighter_1_votes,
              'fighter_2_votes':item.fighter_2_votes,
              'fighter_1_odds':item.fighter_1_odds,
              'fighter_2_odds':item.fighter_2_odds,
              'fight_order':item.fight_order
          }
        )
    division_info = []
    division_data = Division.query.with_entities(Division.id, Division.name).all()
    for item in division_data:
      division_info.append({
        'id':item.id,
        'name':item.name
      })
    return render_template('event.html',
                                userinfo=session[constants.PROFILE_KEY],
                                userinfo_pretty=json.dumps(session[constants.JWT_PAYLOAD], indent=4), events = event_info, divisions = division_info)
 
  @app.route('/event-create', methods=['GET']) 
  @requires_auth('get:event-create')
  def create_event_form(token):
    form = EventForm()
    return render_template('forms/new_event.html', form=form, userinfo=session[constants.PROFILE_KEY])
  
  @app.route('/event-create', methods=['POST'])
  @requires_auth('post:event-create')
  def create_event(token):
    try:
      # get form data and create 
      form = EventForm()
      #print(f'This is form: {form}')
      form_event = Event(
      event_name = form.event_name.data, 
      event_date = form.event_date.data,
      location = form.location.data,
      division = form.division.data,
      fighter_1 = form.fighter_1.data, 
      fighter_2 = form.fighter_2.data,  
      fighter_1_votes = 0,
      fighter_2_votes = 0,
      fighter_1_odds = form.fighter_1_odds.data,
      fighter_2_odds = form.fighter_2_odds.data,
      fight_order = form.fight_order.data, 
        )
      
      # commit session to database
      db.session.add(form_event)
      db.session.commit()
     
      flash('Event ' + request.form['event_name'] + ' was successfully listed!')
    except:
      db.session.rollback()
      #flash failure
      flash('An error occurred. Event ' + request.form['event_name'] + ' could not be listed.')
    finally:
      db.session.close()
    #return render_template('index.html', userinfo=session[constants.PROFILE_KEY])
    return redirect(url_for('create_event_form'))

  @app.route('/event/plus/<name>/<number>', methods=['PATCH'])
  def get_event_fighter_votes(name, number):
      #print(html.unescape(name))
      clean_name = html.unescape(name)
      fighter_number = number

      if(fighter_number == '1'):
          #event_data
          event_data = Event.query.filter(Event.fighter_1 == clean_name).order_by(Event.event_date.desc()).limit(1)
          #print(f'Event data is {event_data[0].fighter_1_votes}')
          vote_number = event_data[0].fighter_1_votes + 1
          #print(f'This is vote num - {vote_number}')
          event_data[0].fighter_1_votes = vote_number
          db.session.commit()
          
          data = []
          for item in event_data:
            data.append( {
                  'fighter_number':1,     
                  'fighter_1_votes':item.fighter_1_votes,
              })
            return jsonify({
            'success':True,
            'fighter_votes':data,
            }), 200
      else:
          event_data = Event.query.filter(Event.fighter_2 == clean_name).order_by(Event.event_date.desc()).limit(1)
          vote_number = event_data[0].fighter_2_votes + 1
          #print(f'This is vote num - {vote_number}')
          event_data[0].fighter_2_votes = vote_number
          db.session.commit()

          data = []
          for item in event_data:
                data.append( {  
                  'fighter_number':2,   
                  'fighter_2_votes':item.fighter_2_votes, 
                  })
            
                return jsonify({
                  'success':True,
                  'fighter_votes':data,
                }), 200

  @app.route('/event-delete/<date>', methods=['GET']) 
  @requires_auth('get:event-delete')
  def edit_event_form(token, date):
    clean_date = html.unescape(date)
    events = Event.query.filter(Event.event_date == clean_date).all()
    events_data = [item.format() for item in events]
    #form = EventForm()
    return render_template('delete_event.html', events = events_data, userinfo=session[constants.PROFILE_KEY])
  

  @app.route('/event-delete/<date>', methods=['DELETE'])
  @requires_auth('delete:event-delete')
  def delete_event(token, date):
    clean_date = html.unescape(date)
    events = Event.query.filter(Event.event_date == clean_date).all()
    if (len(events) == 0):
            abort(404)
    
    [item.delete() for item in events]
    
    
    return jsonify({
      'success': True,
      'deleted': date,
    }), 200 
   
  @app.route('/event-delete/<int:id>', methods=['DELETE'])
  @requires_auth('delete:event-delete')
  def delete_event_id(token, id):
    
    event = Event.query.filter(Event.id == id).one_or_none()
    if event is None:
      abort(404)
    
    event.delete()
    
    
    return jsonify({
      'success': True,
      'deleted': id,
    }), 200 

  @app.route('/fighter-edit/<int:fighter_id>', methods=['GET']) 
  @requires_auth('get:fighter-edit')
  def fighter_edit_form(token, fighter_id):
    
    fighter = Fighter.query.get(fighter_id)
    #fighter_details = Fighter.format(fighter)
    fighter_details = fighter.format()
    
    #Here we populate the form from the database
    form = FighterForm(obj = fighter) #was fighter_detail

    return render_template('forms/edit_fighter.html', form=form, fighter = fighter_details, userinfo=session[constants.PROFILE_KEY])
  
  @app.route('/fighter-edit/<int:fighter_id>', methods=['POST'])
  @requires_auth('get:fighter-edit')
  def edit_fighters(token, fighter_id):
      fighter_division = 0
      try:
        fighter = Fighter.query.filter(Fighter.id == fighter_id).one_or_none()
        #fighter_details = Fighter.format(fighter)
        print(f'This is fighter -- {fighter.division}')
        fighter_division = fighter.division

        if fighter is None:
          abort(404)
        form = FighterForm(obj = fighter)
   
        form.populate_obj(fighter)
        db.session.commit()
      
        #flash('Event ' + request.form['first_name'] + ' was successfully listed!')
      except:
        db.session.rollback()
        #flash failure
        #flash('An error occurred. Event ' + request.form['first_name'] + ' could not be listed.')
      finally:
        db.session.close()
      #return render_template('index.html', userinfo=session[constants.PROFILE_KEY])
      return redirect(url_for('get_division_fighters', division_id = fighter_division))

  

  @app.errorhandler(404)
  def resource_not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

  @app.errorhandler(401)
  def unauthorized(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": "You are NOT Authorized!"
        }), 401
  

  return app

    