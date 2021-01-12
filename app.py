from flask import (
    Flask, render_template, g, abort,
    request, jsonify, Response, flash,
    redirect, url_for, session, jsonify)
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text, or_
from flask_cors import CORS
from models import setup_db, db, Fighter, Division, Event
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
from auth import AuthError, requires_auth
import constants
from forms import EventForm, FighterForm
import html

# Authentication data variables
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

    # This sets up CORS to Allow '*' for origins.
    CORS(app)

    app.secret_key = constants.SECRET_KEY
    app.debug = True

    # --------------------------------------------------------#
    # Filter
    # --------------------------------------------------------#
    # use a string for the value arg when calling this function
    def format_datetime(value, format='full'):
        date = dateutil.parser.parse(value)
        if format == 'full':
            format = "EEEE MMMM, d, y 'at' h:mma"
        elif format == 'medium':
            format = "EE MM, dd, y h:mma"
        return babel.dates.format_datetime(date, format)

    app.jinja_env.filters['datetime'] = format_datetime
    # -----------------------------------------------------------#

    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET,PUT,POST,DELETE,OPTIONS,PATCH')
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
    # adds login_address function to jinja context
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

    # Endpoints

    @app.route('/')
    def home():
        return render_template('/home.html')

    @app.route('/callback')
    def callback_handling():
        token = auth0.authorize_access_token()
        resp = auth0.get('userinfo')
        userinfo = resp.json()
        # Here we set session variables associated with logged in user
        session[constants.JWT_PAYLOAD] = userinfo
        session[constants.PROFILE_KEY] = {
            'user_id': userinfo['sub'],
            'name': userinfo['name'],
            'picture': userinfo['picture']
        }
        session[constants.SESSION_NAME] = userinfo['name']
        session[constants.JWT] = token['access_token']

        return redirect('/index')

    @app.route('/login')
    def login():
        return auth0.authorize_redirect(redirect_uri=AUTH0_CALLBACK_URL,
                                        audience=AUTH0_AUDIENCE)

    @app.route('/logout')
    def logout():
        session.clear()
        params = {'returnTo': url_for(
            'home', _external=True), 'client_id': AUTH0_CLIENT_ID}
        return redirect(auth0.api_base_url + '/v2/logout?' + urlencode(params))

    @app.route('/api-key')
    def get_api_key():
        return render_template('api_key.html'), 200

    @app.route('/index')
    def get_all_fighters():
        session['Admin'] = env.get('APP_ADMIN')
        session['Event Editor'] = env.get('EVENT_EDITOR')
        # Here I call the api function and use it on render_template
        response = get_all_fighters_api()
        data = json.loads(response)
        div_data = data["div_data"]
        events = data["events"]

        return render_template('index.html',
                               userinfo=session[constants.PROFILE_KEY],
                               userinfo_pretty=json.dumps(
                                   session[constants.JWT_PAYLOAD], indent=4),
                               events=events, div_data=div_data), 200

    @app.route('/knockouts')
    def get_knockout_page():
        return render_template('knockouts.html',
                               userinfo=session[constants.PROFILE_KEY]), 200

    @app.route('/division_fighters/<int:division_id>')
    def get_division_fighters(division_id):
        # Here I call the api function and use it on render_template
        response = get_division_fighters_api(division_id)
        data = json.loads(response)
        div_fighter_data = data["data"]

        return render_template('division_fighters.html',
                               userinfo=session[constants.PROFILE_KEY],
                               userinfo_pretty=json.dumps(
                                   session[constants.JWT_PAYLOAD], indent=4),
                               fighters=div_fighter_data), 200

    @app.route('/fighter/<int:id>')
    def get_selected_fighter(id):
        fighter = Fighter.query.get(id)
        if fighter is None:
            abort(404)
        selected_fighter = [fighter.format()]

        return render_template('/selected_fighter.html',
                               userinfo=session[constants.PROFILE_KEY],
                               userinfo_pretty=json.dumps(
                                   session[constants.JWT_PAYLOAD], indent=4),
                               fighter=selected_fighter), 200

    @app.route('/event/<date>')
    def get_event(date):
        # Here I call the api function and use it on render_template
        response = get_event_api(date)
        data = json.loads(response)
        event_info = data["event_info"]

        return render_template('event.html',
                               userinfo=session[constants.PROFILE_KEY],
                               userinfo_pretty=json.dumps(
                                   session[constants.JWT_PAYLOAD], indent=4),
                               events=event_info), 200

    @app.route('/event-create', methods=['GET'])
    @requires_auth('get:event-create')
    def create_event_form(token):
        form = EventForm()
        return render_template('forms/new_event.html', form=form,
                               userinfo=session[constants.PROFILE_KEY]), 200

    @app.route('/event-create', methods=['POST'])
    @requires_auth('post:event-create')
    def create_event(token):
        try:
            # get form and create new obj
            form = EventForm()
            form_event = Event(
                event_name=form.event_name.data,
                event_date=form.event_date.data,
                location=form.location.data,
                division=form.division.data,
                fighter_1=form.fighter_1.data,
                fighter_2=form.fighter_2.data,
                fighter_1_votes=0,
                fighter_2_votes=0,
                fighter_1_odds=form.fighter_1_odds.data,
                fighter_2_odds=form.fighter_2_odds.data,
                fight_order=form.fight_order.data,
            )
            # commit session to database
            form_event.insert()
            # Success
            flash('Event insert was successfully listed!')
            return redirect(url_for('create_event_form'))
        except BaseException as e:
            print(e)
            db.session.rollback()
            # flash failure
            flash('An error occurred. Event could not be listed.')
            abort(422)
        finally:
            db.session.close()

    @app.route('/event/plus/<name>/<number>', methods=['PATCH'])
    def get_event_fighter_votes(name, number):
        return get_event_fighter_votes_api(name, number)


    @app.route('/event-delete/<date>', methods=['GET'])
    @requires_auth('get:event-delete')
    def edit_event_form(token, date):
        clean_date = html.unescape(date)
        events = Event.query.filter(Event.event_date == clean_date).all()
        if len(events) == 0:
            abort(404)
        events_data = [event.format() for event in events]

        return render_template('delete_event.html', events=events_data,
                               userinfo=session[constants.PROFILE_KEY]), 200

    @app.route('/event-delete/<date>', methods=['DELETE'])
    @requires_auth('delete:event-delete')
    def delete_event(token, date):
        delete_event_api(date)

    @app.route('/event-delete/<int:id>', methods=['DELETE'])
    @requires_auth('delete:event-delete')
    def delete_event_id(token, id):
        response = delete_event_id_api(id)
        data = json.loads(response)
        success = data['success']
        deleted = data['deleted']
        return jsonify({
            'success':success,
            'deleted':deleted
        })

    @app.route('/fighter-edit/<int:fighter_id>', methods=['GET'])
    @requires_auth('get:fighter-edit')
    def fighter_edit_form(token, fighter_id):
        fighter = Fighter.query.get(fighter_id)
        response = fighter_edit_form_api(fighter_id)
        data = json.loads(response)
        fighter_details = data['fighter_details']

        # Here we populate the form from the database
        form = FighterForm(obj=fighter)
        return render_template('forms/edit_fighter.html', form=form,
                               fighter=fighter_details,
                               userinfo=session[constants.PROFILE_KEY]), 200

    @app.route('/fighter-edit/<int:fighter_id>', methods=['POST'])
    @requires_auth('get:fighter-edit')
    def edit_fighters(token, fighter_id):
        response = edit_fighters_api(fighter_id)
        data = json.loads(response)
        fighter_division = data['division_id']

        return redirect(url_for('get_division_fighters',
                                division_id=fighter_division))
    # -------------------------------------------------------------#
    # API - functions with json responses.
    # -------------------------------------------------------------#

    @app.route('/api/index')
    def get_all_fighters_api():

        # Here we get all the fighters by division
        fighter_info = Fighter.query.order_by(Fighter.division, Fighter.rank)\
            .all()
        if len(fighter_info) == 0:
            abort(404)
        div_data = [fighter.format() for fighter in fighter_info]

        event_info = []
        event_data = Event.query.order_by(
            Event.event_date.desc()).limit(1).all()
        if len(event_data) == 0:
            abort(404)

        event_info.append(
            {
                'event_name': event_data[0].event_name,
                'event_date': format_datetime(str(event_data[0].event_date)),
                'location': event_data[0].location,
            }
        )

        # Here I set a session variable so I can link to
        # the event page from the main.html
        session['Upcoming Event'] = '/event/' + \
            format_datetime(str(event_data[0].event_date))

        return json.dumps({
            "success": True,
            "events": event_info,
            "div_data": div_data
        })

    @app.route('/api/division_fighters/<int:division_id>')
    def get_division_fighters_api(division_id):
        # Here I join Fighters and Divisions Tables
        division_fighters = db.session.query(Fighter, Division).join(
                                             Division).filter(
                                             Fighter.division == division_id)\
                                             .order_by(Fighter.rank).all()

        if len(division_fighters) == 0:
            abort(404)
        data = []

        for fighter, division in division_fighters:
            data.append({
                        'id': fighter.id,
                        'first_name': fighter.first_name,
                        'last_name': fighter.last_name,
                        'age': fighter.age,
                        'height': fighter.height,
                        'weight': fighter.weight,
                        'arm_reach': fighter.arm_reach,
                        'leg_reach': fighter.leg_reach,
                        'sex': fighter.sex,
                        'win': fighter.win,
                        'loss': fighter.loss,
                        'draw': fighter.draw,
                        'division': fighter.division,
                        'rank': fighter.rank,
                        'div_id': division.id,
                        'div_name': division.name,
                        }
                        )
        return json.dumps({
            'success': True,
            'data': data,
        }
        )

    @app.route('/api/event/<date>')
    def get_event_api(date):
        clean_date = html.unescape(date)
        event_info = []
        # Here we join Events table and Division table
        event_data = db.session.query(Event, Division).join(Division).filter(
            Event.event_date == clean_date).order_by(Event.fight_order).all()
        if len(event_data) == 0:
            abort(404)

        for event, division in event_data:
            event_info.append(
                {
                    'event_name': event.event_name,
                    'event_date': format_datetime(str(event.event_date)),
                    'location': event.location,
                    'division': event.division,
                    'fighter_1': event.fighter_1,
                    'fighter_2': event.fighter_2,
                    'fighter_1_votes': event.fighter_1_votes,
                    'fighter_2_votes': event.fighter_2_votes,
                    'fighter_1_odds': event.fighter_1_odds,
                    'fighter_2_odds': event.fighter_2_odds,
                    'fight_order': event.fight_order,
                    'div_id': division.id,
                    'div_name': division.name,
                }
            )
        return json.dumps({
            'success': True,
            'event_info': event_info
        })

    @app.route('/api/event-create', methods=['GET'])
    @requires_auth('get:event-create')
    def create_event_form_api(token):
        try:
            form = EventForm()

            return jsonify({
                'success': True,
            }), 200
        except BaseException as e:
            print(e)
            abort(500)

    @app.route('/api/event-create', methods=['POST'])
    @requires_auth('post:event-create')
    def create_event_api(token):
        # get request body
        data = request.get_json()
        try:
            form = EventForm()

            event_data = Event(
                event_name=form.event_name.data,
                event_date=form.event_date.data,
                location=form.location.data,
                division=form.division.data,
                fighter_1=form.fighter_1.data,
                fighter_2=form.fighter_2.data,
                fighter_1_votes=0,
                fighter_2_votes=0,
                fighter_1_odds=form.fighter_1_odds.data,
                fighter_2_odds=form.fighter_2_odds.data,
                fight_order=form.fight_order.data,
            )

            # commit session to database
            event_data.insert()
            # Success
            flash('Event insert was successfully listed!')

            return jsonify({
                'success': True,
                'id': event_data.id
            }), 200
        except BaseException as e:
            print(e)
            db.session.rollback()
            # flash failure
            flash('An error occurred. Event could not be listed.')
            abort(422)
        finally:
            db.session.close()

    @app.route('/api/event/plus/<name>/<number>', methods=['PATCH'])
    def get_event_fighter_votes_api(name, number):

        clean_name = html.unescape(name)
        fighter_number = number

        if(fighter_number == '1'):
            # event_data for latest event
            event_data = Event.query.filter(Event.fighter_1 == clean_name)\
                .order_by(Event.event_date.desc()).limit(1).all()
            if len(event_data) == 0:
                abort(404)
            vote_number = event_data[0].fighter_1_votes + 1
            event_data[0].fighter_1_votes = vote_number
            try:
                db.session.commit()
            except BaseException as e:
                print(e)
                abort(422)

            data = []
            for event in event_data:
                data.append({
                    'fighter_number': 1,
                    'fighter_1_votes': event.fighter_1_votes,
                })
                return jsonify({
                    'success': True,
                    'fighter_votes': data,
                }), 200
        else:
            # If fighter number 2 then get that latest even
            event_data = Event.query.filter(Event.fighter_2 == clean_name)\
                .order_by(Event.event_date.desc()).limit(1).all()
            if len(event_data) == 0:
                abort(404)

            vote_number = event_data[0].fighter_2_votes + 1
            event_data[0].fighter_2_votes = vote_number
            try:
                db.session.commit()
            except BaseException as e:
                print(e)
                abort(422)

            data = []
            for event in event_data:
                data.append({
                    'fighter_number': 2,
                    'fighter_2_votes': event.fighter_2_votes,
                })

                return jsonify({
                    'success': True,
                    'fighter_votes': data,
                }), 200

    @app.route('/api/event-delete/<date>', methods=['GET'])
    @requires_auth('get:event-delete')
    def edit_event_form_api(token, date):
        clean_date = html.unescape(date)
        events = Event.query.filter(Event.event_date == clean_date).all()
        if len(events) == 0:
            abort(404)
        events_data = [event.format() for event in events]
        return json.dumps({
            'success': True,
            'event_data': events_data,
        })

    @app.route('/api/event-delete/<date>', methods=['DELETE'])
    @requires_auth('delete:event-delete')
    def delete_event_api(token, date):
        clean_date = html.unescape(date)
        events = Event.query.filter(Event.event_date == clean_date).all()
        if len(events) == 0:
            abort(404)

        [event.delete() for event in events]

        return json.dumps({
            'success': True,
            'deleted': date,
        })

    @app.route('/api/event-delete/<int:id>', methods=['DELETE'])
    @requires_auth('delete:event-delete')
    def delete_event_id_api(token, id):
        # Get event by id
        event = Event.query.filter(Event.id == id).one_or_none()
        if event is None:
            abort(404)

        event.delete()

        return json.dumps({
            'success': True,
            'deleted': id,
        })

    @app.route('/api/fighter-edit/<int:fighter_id>', methods=['GET'])
    @requires_auth('get:fighter-edit')
    def fighter_edit_form_api(token, fighter_id):
        # Get fighter by id
        fighter = Fighter.query.get(fighter_id)
        if fighter is None:
            abort(400)
        fighter_details = fighter.format()

        # Here we populate the form from the database
        form = FighterForm(obj=fighter)

        return json.dumps({
            'success': True,
            'fighter_details': fighter_details,
        })

    @app.route('/api/fighter-edit/<int:fighter_id>', methods=['POST'])
    @requires_auth('get:fighter-edit')
    def edit_fighters_api(token, fighter_id):
        fighter_division = 0
        try:
            fighter = Fighter.query.filter(
                Fighter.id == fighter_id).one_or_none()
            fighter_division = fighter.division
            form = FighterForm(obj=fighter)

            form.populate_obj(fighter)
            db.session.commit()
            flash('Event was successfully listed!')

            return json.dumps({
            'success': True,
            'division_id': fighter_division,
        })
        except BaseException as e:
            print(e)
            db.session.rollback()
            # flash failure
            flash('An error occurred. Event could not be listed.')
            abort(422)
        finally:
            db.session.close()

    # -------------------------------------------------------------#
    # ---ERROR HANDLERS--------------------------------------------#

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify({
            "success": False,
            "error": 405,
            "message": "method not allowed"
        }), 405

    @app.errorhandler(404)
    def resource_not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    @app.errorhandler(AuthError)
    def authentification_failed(AuthError):
        return jsonify({
            "success": False,
            "error": AuthError.status_code,
            "message": AuthError.error
        }), 401

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
        }), 400

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "Server Error"
        }), 500

    @app.errorhandler(Exception)
    def handle_auth_error(ex):
        response = jsonify(message=str(ex))
        response.status_code = (
            ex.code if isinstance(ex, HTTPException) else 500)
        return response

    return app
