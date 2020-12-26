import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
import psycopg2

from api import create_app
from models import setup_db, Fighter, Event, Division
import re
import constants
user = os.environ.get('USER')
password = os.environ.get('PASSWORD')
#----------------------------------------------------------maybe not worth it
""" conn = psycopg2.connect(
    #host="localhost:5432",
    database="ufcfan_test",
    user="postgres",
    password="Opensaysme69") """

class UfcFanTestCase(unittest.TestCase):
    """This class represents the plant survey test case"""

    # auth tokens needed for successful testing
    """ APP_ADMIN_TOKEN = os.environ.get('APP_ADMIN')
    EVENT_EDITOR_TOKEN = os.environ.get('EVENT_EDITOR') """
    token = constants.JWT

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "ufcfan_test"
        self.database_path = "postgres://{}/{}".format(f'{user}:{password}@localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    # UTILITY METHODS

    """ cur = conn.cursor()
    sql_file_divisions = 'divisions.sql'
    sql_file_events = 'events.sql'
    sql_file_fighters = 'fighters.sql'

    def exec_sql_file(cursor, sql_file):
        statement = ""
        for line in open(sql_file):
            if re.match(r'--', line):  # ignore sql comment lines
                continue
            if not re.search(r';$', line):  # keep appending lines that don't end in ';'
                statement = statement + line
            else:  # when you get a line ending in ';' then exec statement and reset for next statement
                statement = statement + line
                try:
                    cursor.execute(statement)
                except BaseException as e:
                    print('Error: ' + e)
                statement = ""
    exec_sql_file(cur, sql_file_divisions)
    exec_sql_file(cur, sql_file_events)
    exec_sql_file(cur, sql_file_fighters) """

    # creates auth header with bearer token
    def create_auth_headers(self, token):
        # return auth headers using token
        return {
            "Authorization": "Bearer {}".format(
                token
            )}

    division_test = {
        'name':"Men's Flyweight",
        'weight':125
    }

    def create_division(self):
        division = Division(
            name= self.division_test['name'],
            weight = self.division_test['weight']
        
        )
        division.insert()
        #return division.id

    test_fighter = [
        {'first_name':'Test','last_name':'Case','age':100,'height':10.00,'weight':10.00,'arm_reach':10.00,'leg_reach':10.00,'sex':'M','win':1,'loss':1,'draw':1,'division':1,'rank':10,},
        {'first_name':'Test','last_name':'Case','age':100,'height':10.00,'weight':10.00,'arm_reach':10.00,'leg_reach':10.00,'sex':'M','win':1,'loss':1,'draw':1,'division':2,'rank':10,},
        {'first_name':'Test','last_name':'Case','age':100,'height':10.00,'weight':10.00,'arm_reach':10.00,'leg_reach':10.00,'sex':'M','win':1,'loss':1,'draw':1,'division':3,'rank':10,},
        {'first_name':'Test','last_name':'Case','age':100,'height':10.00,'weight':10.00,'arm_reach':10.00,'leg_reach':10.00,'sex':'M','win':1,'loss':1,'draw':1,'division':4,'rank':10,},
        {'first_name':'Test','last_name':'Case','age':100,'height':10.00,'weight':10.00,'arm_reach':10.00,'leg_reach':10.00,'sex':'M','win':1,'loss':1,'draw':1,'division':5,'rank':10,},
        {'first_name':'Test','last_name':'Case','age':100,'height':10.00,'weight':10.00,'arm_reach':10.00,'leg_reach':10.00,'sex':'M','win':1,'loss':1,'draw':1,'division':6,'rank':10,},
        {'first_name':'Test','last_name':'Case','age':100,'height':10.00,'weight':10.00,'arm_reach':10.00,'leg_reach':10.00,'sex':'M','win':1,'loss':1,'draw':1,'division':7,'rank':10,},
        {'first_name':'Test','last_name':'Case','age':100,'height':10.00,'weight':10.00,'arm_reach':10.00,'leg_reach':10.00,'sex':'M','win':1,'loss':1,'draw':1,'division':8,'rank':10,},
        {'first_name':'Test','last_name':'Case','age':100,'height':10.00,'weight':10.00,'arm_reach':10.00,'leg_reach':10.00,'sex':'M','win':1,'loss':1,'draw':1,'division':9,'rank':10,},
        {'first_name':'Test','last_name':'Case','age':100,'height':10.00,'weight':10.00,'arm_reach':10.00,'leg_reach':10.00,'sex':'M','win':1,'loss':1,'draw':1,'division':10,'rank':10,},
        {'first_name':'Test','last_name':'Case','age':100,'height':10.00,'weight':10.00,'arm_reach':10.00,'leg_reach':10.00,'sex':'M','win':1,'loss':1,'draw':1,'division':11,'rank':10,},
        {'first_name':'Test','last_name':'Case','age':100,'height':10.00,'weight':10.00,'arm_reach':10.00,'leg_reach':10.00,'sex':'M','win':1,'loss':1,'draw':1,'division':12,'rank':10,},
        ]
    # creates test fighter
    def create_fighter(self):

        # create and insert new plant
        for item in self.test_fighter:

            fighter = Fighter(
            first_name = item['first_name'],
            last_name = item['last_name'],
            age = item['age'],
            height = item['height'],
            weight = item['weight'],
            arm_reach = item['arm_reach'],
            leg_reach = item['leg_reach'],
            sex = item['sex'],
            win = item['win'],
            loss = item['loss'],
            draw = item['draw'],
            division = item['division'],
            rank = item['rank']
            )
            fighter.insert()

        #return self.item.id

    test_event = {
    'event_name':'UFC',
    'event_date':'2020-12-12T12:00:00.000Z', 
    'location':'Somewhere',
    'division':1,
    'fighter_1':'Doorman',
    'fighter_2':'Hammer',
    'fighter_1_votes':0,
    'fighter_2_votes':0,
    'fighter_1_odds':0,
    'fighter_2_odds':0,
    'fight_order':0,
    }

    def create_event(self):
        event = Event(
            event_name = self.test_event['event_name'], 
            event_date = self.test_event['event_date'], 
            division = self.test_event['division'],
            fighter_1 = self.test_event['fighter_1'],
            fighter_2 = self.test_event['fighter_2'],
            fighter_1_votes = self.test_event['fighter_1_votes'],
            fighter_2_votes = self.test_event['fighter_2_votes'],
            fighter_1_odds = self.test_event['fighter_1_odds'],
            fighter_2_odds = self.test_event['fighter_2_odds'],
            fight_order = self.test_event['fight_order'],
        )
        event.insert()
        #return event.id    

    def delete_fighters(self):
        fighters = Fighter.query.all()
        for item in fighters:
            item.delete();

    def delete_divisions(self):
        divisions = Division.query.all()
        for item in divisions:
            item.delete();

    def delete_events(self):
        events = Event.query.all()
        for item in events:
            item.delete();
    
    """ 
    create_division(self)
    create_fighter(self)
    create_event(self)  """

    """ def test_get_knockouts(self):
        
        res = self.client().get('/knockouts')-----------------------------------------starts here-------------#
        self.assertEqual(res.status_code, 200) """

    def test_get_division_fighters(self):
        """Tests Get Division Fighters"""
        self.create_division()
        self.create_fighter()
        res = self.client().get('/api/division_fighters/1')
        data = json.loads(res.data)
        self.assertTrue(data['data'])
        self.assertEqual(res.status_code, 200)
        
    def test_get_division_fighters_fail(self):
        """Tests Fail Division Fighters"""
        
        """ fighters = Fighter.query.filter(Fighter.division == 1).all()
        for item in fighters:
            item.delete() """
        self.delete_fighters()
        
        res = self.client().get('/api/division_fighters/1')
        data = json.loads(res.data)
        print(f'This is reponse data -- {data}')
        self.assertTrue(data['data'])
        self.assertEqual(res.status_code, 404)
    
    def test_get_all_fighters_api(self):
        """Tests Get All Fighters"""
        self.create_fighter()
        res = self.client().get('/api/index')
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['events'])
        self.assertTrue(data['div_1'])
        self.assertTrue(data['div_2'])
        self.assertTrue(data['div_3'])
        self.assertTrue(data['div_4'])
        self.assertTrue(data['div_5'])
        self.assertTrue(data['div_6'])
        self.assertTrue(data['div_7'])
        self.assertTrue(data['div_8'])
        self.assertTrue(data['div_9'])
        self.assertTrue(data['div_10'])
        self.assertTrue(data['div_11'])
        self.assertTrue(data['div_12'])

    def test_get_all_fighters_api_fail(self):
        """Tests Get All Fighters"""
        self.delete_fighters()

        res = self.client().get('/api/index')
        data = json.loads(res.data)
        self.assertEqual(data['success'], False)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['message'], 'resource not found')

    
        
    

    


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()