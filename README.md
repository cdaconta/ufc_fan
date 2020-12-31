# UFC FAN

This application is a fan site for the Ultimate Fighting Championship (UFC).  The site is hosted on Heroku at https://ufc-fan.herokuapp.com. Anyone can create a public account and learn about the UFC divisions and an upcoming Event.  The landing page shows all twelve divisions and an upcoming event for the UFC.  The user can take a deeper look at the divisions and also vote on the main card fighters in that upcoming event.  Admin and the Event Editor have special priveleges to edit fighters or edit event information.

This project is the capstone project for the Udacity Full Stack Web Developer Nanodegree Program.  Some of the objectives for the project are:
*Architect relational database models in Python
*Utilize SQLAlchemy to conduct database queries
*Follow RESTful principles of API development
*Enable Role Based Authentication and roles-based access control (RBAC) in a Flask application
*Use the unittest library to test endpoint behavior

# Roles and Permissions
* This project has two primary roles configured in Auth0.com.  A JWT token needs to be passed to each endpoint that requires permission.
  * Admin role - The admin role has complete permissions to all endpoints in the project.
    * Permissions:
      * get:event-delete - Read the event delete page and see items available to be deleted.
      * delete:event-delete	- Delete a part of an event or the whole event.
      * get:event-create - Get event form prefilled with event information.
      * post:event-create - Change event in event form and Post the changes.
      * get:fighter-edit -	Read the fighter you want to edit in fighter form.
      * post:fighter-edit	- Edit the fighter base on rank provided in fighter form.
  * Edit Event Role - The Event Editor has permissions for all endpoints in the project involving Event information.
    * Permissions:
      * get:event-create - Get event form prefilled with event information.
      * delete:event-delete	- Delete a part of an event or the whole event.
      * get:event-delete - Read the event page and see items available to be deleted.
      * post:event-create - Change event in event form and Post changes.
* All other users who sign up fall into a default permission category which only allows access to these endpoints:
  * GET /api-key - Shows JWK web token.
  * GET /index - Gets all fighters by division and shows upcoming Event.
  * GET /knockouts - Gets knockout videos.
  * GET /division_fighters/<int:division_id> - Shows fighters by division id.
  * GET /event/<date> - Shows event associated with a given date.

## API Reference
# Getting Started on Local Machine
People using this project should already have Python, PIP, and Postgres installed on their local machine. You will also have to create an account and configure Auth0.
*	https://www.python.org/
*	https://pypi.org/project/pip/
*   https://www.postgresql.org/
*   https://auth0.com/


Clone the repository from github.com to your local machine.  In your .env file and the auth.py file you will need to add your Auth0 account informaton.

It is recommended to use a virtual environment for the project.  https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/

Open a terminal to run the project.
*	One for the backend and the other for the front end.

```
	pip3 install -r requirements.txt
```

*	To run the server, execute:
```
	export FLASK_APP=app
	export FLASK_ENV=development
	flask run
```
* Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.
*	On Windows 10 with PowerShell:
```
    $env:FLASK_APP = "app"
    $env:FLASK_DEBUG=1
    Flask run
```
* Setting `FLASK_DEBUG=1` will detect file changes and restart the server automatically.
## Testing

To run the tests, in psql run
```
create database ufcfan_test;
```
Use provided sql to create database or tables as needed with pgAdmin.
You database information will need to be added to .env file.

In the terminal run:
`python test_api.py`

## Error Handling

Errors are returned as JSON in the following format:
```
{
    "success": False,
    "error": 404,
    "message": "resource not found"
}
```
The API will return five types of errors:
*	400 – bad request
*   401 - not authorized
*	404 – resource not found
*   405 - method not allowed
*	422 – unprocessable


Endpoints (**All example curl commands will be difference in Powershell)

## Endpoints

### GET /api/index
* General: Returns a list of fighters and an event.
* Does not require authorization.
* Example: curl https://ufc-fan.herokuapp.com/api/index
```
{
    "div_1": [
        {
            "age": 32,
            "arm_reach": 68.0,
            "division": 1,
            "draw": 1,
            "first_name": "Deiveson",
            "height": 65.0,
            "id": 70,
            "last_name": "Figueiredo",
            "leg_reach": 38.0,
            "loss": 1,
            "rank": 0,
            "sex": "M",
            "weight": 125.0,
            "win": 19
        },
        {
            "age": 35,
            "arm_reach": 65.0,
            "division": 1,
            "draw": 0,
            "first_name": "Joseph",
            "height": 64.0,
            "id": 71,
            "last_name": "Benavidez",
            "leg_reach": 36.0,
            "loss": 7,
            "rank": 1,
            "sex": "M",
            "weight": 126.0,
            "win": 28
        },
        {
            "age": 26,
            "arm_reach": 70.0,
            "division": 1,
            "draw": 2,
            "first_name": "Brandon",
            "height": 67.0,
            "id": 72,
            "last_name": "Moreno",
            "leg_reach": 38.0,
            "loss": 5,
            "rank": 2,
            "sex": "M",
            "weight": 125.0,
            "win": 17
        },
        {
            "age": 27,
            "arm_reach": 67.0,
            "division": 1,
            "draw": 1,
            "first_name": "Askar",
            "height": 66.0,
            "id": 73,
            "last_name": "Askarov",
            "leg_reach": 36.0,
            "loss": 0,
            "rank": 3,
            "sex": "M",
            "weight": 125.0,
            "win": 11
        },
        {
            "age": 28,
            "arm_reach": 65.5,
            "division": 1,
            "draw": 0,
            "first_name": "Alex",
            "height": 66.0,
            "id": 74,
            "last_name": "Perez",
            "leg_reach": 38.0,
            "loss": 5,
            "rank": 4,
            "sex": "M",
            "weight": 125.0,
            "win": 24
        },
        {
            "age": 30,
            "arm_reach": 67.0,
            "division": 1,
            "draw": 0,
            "first_name": "Alexandre",
            "height": 65.0,
            "id": 75,
            "last_name": "Pantoja",
            "leg_reach": 36.5,
            "loss": 5,
            "rank": 5,
            "sex": "M",
            "weight": 125.0,
            "win": 22
        }
    ],
    "div_10": [
        {
            "age": 32,
            "arm_reach": 67.0,
            "division": 10,
            "draw": 0,
            "first_name": "Valentina",
            "height": 65.0,
            "id": 124,
            "last_name": "Shevchenko",
            "leg_reach": 38.0,
            "loss": 3,
            "rank": 0,
            "sex": "F",
            "weight": 125.0,
            "win": 19
        },
        {
            "age": 29,
            "arm_reach": 62.0,
            "division": 10,
            "draw": 0,
            "first_name": "Jessica",
            "height": 61.5,
            "id": 125,
            "last_name": "Andrade",
            "leg_reach": 35.0,
            "loss": 8,
            "rank": 1,
            "sex": "F",
            "weight": 135.0,
            "win": 21
        },
        {
            "age": 31,
            "arm_reach": 68.0,
            "division": 10,
            "draw": 0,
            "first_name": "Katlyn",
            "height": 69.0,
            "id": 126,
            "last_name": "Chookagian",
            "leg_reach": 42.0,
            "loss": 4,
            "rank": 2,
            "sex": "F",
            "weight": 125.0,
            "win": 14
        },
        {
            "age": 32,
            "arm_reach": 64.0,
            "division": 10,
            "draw": 1,
            "first_name": "Jennifer",
            "height": 64.0,
            "id": 127,
            "last_name": "Maia",
            "leg_reach": 38.0,
            "loss": 6,
            "rank": 3,
            "sex": "F",
            "weight": 125.0,
            "win": 18
        },
        {
            "age": 33,
            "arm_reach": 64.0,
            "division": 10,
            "draw": 1,
            "first_name": "Cynthia",
            "height": 64.0,
            "id": 128,
            "last_name": "Calvillo",
            "leg_reach": 37.0,
            "loss": 1,
            "rank": 4,
            "sex": "F",
            "weight": 125.0,
            "win": 9
        },
        {
            "age": 37,
            "arm_reach": 67.0,
            "division": 10,
            "draw": 0,
            "first_name": "Lauren",
            "height": 65.0,
            "id": 129,
            "last_name": "Murphy",
            "leg_reach": 38.0,
            "loss": 4,
            "rank": 5,
            "sex": "F",
            "weight": 135.0,
            "win": 13
        }
    ],
    "div_11": [
        {
            "age": 32,
            "arm_reach": 69.0,
            "division": 11,
            "draw": 0,
            "first_name": "Amanda",
            "height": 68.0,
            "id": 130,
            "last_name": "Nunes",
            "leg_reach": 41.0,
            "loss": 4,
            "rank": 0,
            "sex": "F",
            "weight": 135.0,
            "win": 20
        },
        {
            "age": 36,
            "arm_reach": 71.0,
            "division": 11,
            "draw": 0,
            "first_name": "Germaine",
            "height": 69.0,
            "id": 131,
            "last_name": "de Randamie",
            "leg_reach": 41.0,
            "loss": 4,
            "rank": 1,
            "sex": "F",
            "weight": 135.0,
            "win": 10
        },
        {
            "age": 39,
            "arm_reach": 69.0,
            "division": 11,
            "draw": 0,
            "first_name": "Holly",
            "height": 68.0,
            "id": 132,
            "last_name": "Holm",
            "leg_reach": 38.0,
            "loss": 5,
            "rank": 2,
            "sex": "F",
            "weight": 135.0,
            "win": 14
        },
        {
            "age": 25,
            "arm_reach": 66.0,
            "division": 11,
            "draw": 0,
            "first_name": "Aspen",
            "height": 66.0,
            "id": 133,
            "last_name": "Ladd",
            "leg_reach": 38.5,
            "loss": 1,
            "rank": 3,
            "sex": "F",
            "weight": 135.0,
            "win": 9
        },
        {
            "age": 31,
            "arm_reach": 67.5,
            "division": 11,
            "draw": 0,
            "first_name": "Raquel",
            "height": 67.0,
            "id": 134,
            "last_name": "Pennington",
            "leg_reach": 37.0,
            "loss": 9,
            "rank": 4,
            "sex": "F",
            "weight": 135.0,
            "win": 11
        },
        {
            "age": 32,
            "arm_reach": 68.5,
            "division": 11,
            "draw": 0,
            "first_name": "Irene",
            "height": 69.0,
            "id": 135,
            "last_name": "Aldana",
            "leg_reach": 38.5,
            "loss": 6,
            "rank": 5,
            "sex": "F",
            "weight": 135.0,
            "win": 12
        }
    ],
    "div_12": [
        {
            "age": 32,
            "arm_reach": 69.0,
            "division": 12,
            "draw": 0,
            "first_name": "Amanda",
            "height": 68.0,
            "id": 136,
            "last_name": "Nunes",
            "leg_reach": 41.0,
            "loss": 4,
            "rank": 0,
            "sex": "F",
            "weight": 135.0,
            "win": 20
        },
        {
            "age": 29,
            "arm_reach": 68.0,
            "division": 12,
            "draw": 0,
            "first_name": "Felicia",
            "height": 66.0,
            "id": 137,
            "last_name": "Spencer",
            "leg_reach": 40.0,
            "loss": 2,
            "rank": 1,
            "sex": "F",
            "weight": 145.0,
            "win": 8
        },
        {
            "age": 31,
            "arm_reach": 68.0,
            "division": 12,
            "draw": 0,
            "first_name": "Megan",
            "height": 72.0,
            "id": 138,
            "last_name": "Anderson",
            "leg_reach": 40.0,
            "loss": 2,
            "rank": 2,
            "sex": "F",
            "weight": 145.0,
            "win": 8
        },
        {
            "age": 0,
            "arm_reach": 0.0,
            "division": 12,
            "draw": 0,
            "first_name": "",
            "height": 0.0,
            "id": 139,
            "last_name": "",
            "leg_reach": 0.0,
            "loss": 0,
            "rank": 3,
            "sex": "F",
            "weight": 0.0,
            "win": 0
        },
        {
            "age": 0,
            "arm_reach": 0.0,
            "division": 12,
            "draw": 0,
            "first_name": "",
            "height": 0.0,
            "id": 140,
            "last_name": "",
            "leg_reach": 0.0,
            "loss": 0,
            "rank": 4,
            "sex": "F",
            "weight": 0.0,
            "win": 0
        },
        {
            "age": 0,
            "arm_reach": 0.0,
            "division": 12,
            "draw": 0,
            "first_name": "",
            "height": 0.0,
            "id": 141,
            "last_name": "",
            "leg_reach": 0.0,
            "loss": 0,
            "rank": 5,
            "sex": "F",
            "weight": 0.0,
            "win": 0
        }
    ],
    "div_2": [
        {
            "age": 27,
            "arm_reach": 67.0,
            "division": 2,
            "draw": 0,
            "first_name": "Petr",
            "height": 67.5,
            "id": 76,
            "last_name": "Yan",
            "leg_reach": 38.0,
            "loss": 1,
            "rank": 0,
            "sex": "M",
            "weight": 135.0,
            "win": 15
        },
        {
            "age": 30,
            "arm_reach": 71.0,
            "division": 2,
            "draw": 0,
            "first_name": "Aljamain",
            "height": 67.0,
            "id": 77,
            "last_name": "Sterling",
            "leg_reach": 39.0,
            "loss": 3,
            "rank": 1,
            "sex": "M",
            "weight": 136.0,
            "win": 19
        },
        {
            "age": 28,
            "arm_reach": 70.0,
            "division": 2,
            "draw": 0,
            "first_name": "Cory",
            "height": 71.0,
            "id": 78,
            "last_name": "Sandhagen",
            "leg_reach": 40.0,
            "loss": 2,
            "rank": 2,
            "sex": "M",
            "weight": 135.0,
            "win": 13
        },
        {
            "age": 32,
            "arm_reach": 67.0,
            "division": 2,
            "draw": 1,
            "first_name": "Marlon",
            "height": 66.0,
            "id": 79,
            "last_name": "Moraes",
            "leg_reach": 37.0,
            "loss": 7,
            "rank": 3,
            "sex": "M",
            "weight": 135.0,
            "win": 23
        },
        {
            "age": 28,
            "arm_reach": 65.5,
            "division": 2,
            "draw": 0,
            "first_name": "Cody",
            "height": 68.0,
            "id": 80,
            "last_name": "Garbrandt",
            "leg_reach": 38.0,
            "loss": 3,
            "rank": 4,
            "sex": "M",
            "weight": 135.0,
            "win": 12
        },
        {
            "age": 38,
            "arm_reach": 68.0,
            "division": 2,
            "draw": 1,
            "first_name": "Frankie",
            "height": 66.0,
            "id": 81,
            "last_name": "Edgar",
            "leg_reach": 37.5,
            "loss": 8,
            "rank": 5,
            "sex": "M",
            "weight": 135.0,
            "win": 23
        }
    ],
    "div_3": [
        {
            "age": 31,
            "arm_reach": 71.5,
            "division": 3,
            "draw": 0,
            "first_name": "Alexander",
            "height": 66.0,
            "id": 82,
            "last_name": "Volkanovski",
            "leg_reach": 36.0,
            "loss": 1,
            "rank": 0,
            "sex": "M",
            "weight": 145.0,
            "win": 22
        },
        {
            "age": 28,
            "arm_reach": 69.0,
            "division": 3,
            "draw": 0,
            "first_name": "Max",
            "height": 71.0,
            "id": 83,
            "last_name": "Holloway",
            "leg_reach": 42.0,
            "loss": 6,
            "rank": 1,
            "sex": "M",
            "weight": 146.0,
            "win": 21
        },
        {
            "age": 29,
            "arm_reach": 69.0,
            "division": 3,
            "draw": 0,
            "first_name": "Brian",
            "height": 68.0,
            "id": 84,
            "last_name": "Ortega",
            "leg_reach": 39.0,
            "loss": 1,
            "rank": 2,
            "sex": "M",
            "weight": 145.0,
            "win": 15
        },
        {
            "age": 29,
            "arm_reach": 73.0,
            "division": 3,
            "draw": 0,
            "first_name": "Zabit",
            "height": 73.0,
            "id": 85,
            "last_name": "Magomedsharipov",
            "leg_reach": 42.0,
            "loss": 1,
            "rank": 3,
            "sex": "M",
            "weight": 145.0,
            "win": 18
        },
        {
            "age": 27,
            "arm_reach": 71.0,
            "division": 3,
            "draw": 0,
            "first_name": "Yair",
            "height": 71.0,
            "id": 86,
            "last_name": "Rodriguez",
            "leg_reach": 41.5,
            "loss": 2,
            "rank": 4,
            "sex": "M",
            "weight": 145.0,
            "win": 13
        },
        {
            "age": 33,
            "arm_reach": 72.0,
            "division": 3,
            "draw": 0,
            "first_name": "Chan",
            "height": 67.0,
            "id": 87,
            "last_name": "Sung Jung",
            "leg_reach": 38.5,
            "loss": 6,
            "rank": 5,
            "sex": "M",
            "weight": 145.0,
            "win": 16
        }
    ],
    "div_4": [
        {
            "age": 32,
            "arm_reach": 70.0,
            "division": 4,
            "draw": 0,
            "first_name": "Khabib",
            "height": 70.0,
            "id": 88,
            "last_name": "Nurmagomedov",
            "leg_reach": 40.0,
            "loss": 0,
            "rank": 0,
            "sex": "M",
            "weight": 155.0,
            "win": 28
        },
        {
            "age": 31,
            "arm_reach": 70.0,
            "division": 4,
            "draw": 0,
            "first_name": "Justin",
            "height": 71.0,
            "id": 89,
            "last_name": "Gaethje",
            "leg_reach": 40.0,
            "loss": 3,
            "rank": 1,
            "sex": "M",
            "weight": 155.0,
            "win": 22
        },
        {
            "age": 31,
            "arm_reach": 72.0,
            "division": 4,
            "draw": 0,
            "first_name": "Dustin",
            "height": 69.0,
            "id": 90,
            "last_name": "Poirier",
            "leg_reach": 40.5,
            "loss": 6,
            "rank": 2,
            "sex": "M",
            "weight": 155.0,
            "win": 26
        },
        {
            "age": 36,
            "arm_reach": 76.5,
            "division": 4,
            "draw": 0,
            "first_name": "Tony",
            "height": 71.0,
            "id": 91,
            "last_name": "Ferguson",
            "leg_reach": 40.5,
            "loss": 5,
            "rank": 3,
            "sex": "M",
            "weight": 155.0,
            "win": 26
        },
        {
            "age": 32,
            "arm_reach": 74.0,
            "division": 4,
            "draw": 0,
            "first_name": "Conor",
            "height": 69.0,
            "id": 92,
            "last_name": "McGregor",
            "leg_reach": 40.0,
            "loss": 4,
            "rank": 4,
            "sex": "M",
            "weight": 145.0,
            "win": 22
        },
        {
            "age": 30,
            "arm_reach": 75.0,
            "division": 4,
            "draw": 0,
            "first_name": "Dan",
            "height": 72.0,
            "id": 93,
            "last_name": "Hooker",
            "leg_reach": 42.5,
            "loss": 9,
            "rank": 5,
            "sex": "M",
            "weight": 145.0,
            "win": 20
        }
    ],
    "div_5": [
        {
            "age": 33,
            "arm_reach": 76.0,
            "division": 5,
            "draw": 0,
            "first_name": "Kamaru",
            "height": 72.0,
            "id": 94,
            "last_name": "Usman",
            "leg_reach": 41.0,
            "loss": 1,
            "rank": 0,
            "sex": "M",
            "weight": 170.0,
            "win": 17
        },
        {
            "age": 32,
            "arm_reach": 72.0,
            "division": 5,
            "draw": 0,
            "first_name": "Colby",
            "height": 71.0,
            "id": 95,
            "last_name": "Covington",
            "leg_reach": 41.0,
            "loss": 2,
            "rank": 1,
            "sex": "M",
            "weight": 170.0,
            "win": 15
        },
        {
            "age": 33,
            "arm_reach": 71.0,
            "division": 5,
            "draw": 0,
            "first_name": "Gilbert",
            "height": 70.0,
            "id": 96,
            "last_name": "Burns",
            "leg_reach": 40.0,
            "loss": 3,
            "rank": 2,
            "sex": "M",
            "weight": 155.0,
            "win": 19
        },
        {
            "age": 28,
            "arm_reach": 74.0,
            "division": 5,
            "draw": 0,
            "first_name": "Leon",
            "height": 72.0,
            "id": 97,
            "last_name": "Edwards",
            "leg_reach": 43.0,
            "loss": 3,
            "rank": 3,
            "sex": "M",
            "weight": 170.0,
            "win": 18
        },
        {
            "age": 35,
            "arm_reach": 74.0,
            "division": 5,
            "draw": 0,
            "first_name": "Jorge",
            "height": 71.0,
            "id": 98,
            "last_name": "Masvidal",
            "leg_reach": 39.5,
            "loss": 14,
            "rank": 4,
            "sex": "M",
            "weight": 156.0,
            "win": 35
        },
        {
            "age": 37,
            "arm_reach": 75.0,
            "division": 5,
            "draw": 1,
            "first_name": "Stephen",
            "height": 72.0,
            "id": 99,
            "last_name": "Thompson",
            "leg_reach": 42.0,
            "loss": 4,
            "rank": 5,
            "sex": "M",
            "weight": 170.0,
            "win": 16
        }
    ],
    "div_6": [
        {
            "age": 31,
            "arm_reach": 80.0,
            "division": 6,
            "draw": 0,
            "first_name": "Israel",
            "height": 76.0,
            "id": 100,
            "last_name": "Adesanya",
            "leg_reach": 44.5,
            "loss": 0,
            "rank": 0,
            "sex": "M",
            "weight": 185.0,
            "win": 19
        },
        {
            "age": 29,
            "arm_reach": 73.5,
            "division": 6,
            "draw": 0,
            "first_name": "Robert",
            "height": 72.0,
            "id": 101,
            "last_name": "Whittaker",
            "leg_reach": 43.0,
            "loss": 5,
            "rank": 1,
            "sex": "M",
            "weight": 185.0,
            "win": 22
        },
        {
            "age": 29,
            "arm_reach": 72.0,
            "division": 6,
            "draw": 0,
            "first_name": "Paulo",
            "height": 73.0,
            "id": 102,
            "last_name": "Costa",
            "leg_reach": 39.5,
            "loss": 0,
            "rank": 2,
            "sex": "M",
            "weight": 185.0,
            "win": 13
        },
        {
            "age": 36,
            "arm_reach": 77.5,
            "division": 6,
            "draw": 0,
            "first_name": "Jared",
            "height": 71.0,
            "id": 103,
            "last_name": "Cannonier",
            "leg_reach": 41.5,
            "loss": 4,
            "rank": 3,
            "sex": "M",
            "weight": 205.0,
            "win": 13
        },
        {
            "age": 32,
            "arm_reach": 77.5,
            "division": 6,
            "draw": 0,
            "first_name": "Jack",
            "height": 73.0,
            "id": 104,
            "last_name": "Hermansson",
            "leg_reach": 46.5,
            "loss": 5,
            "rank": 4,
            "sex": "M",
            "weight": 186.0,
            "win": 21
        },
        {
            "age": 43,
            "arm_reach": 73.5,
            "division": 6,
            "draw": 0,
            "first_name": "Yoel",
            "height": 72.0,
            "id": 105,
            "last_name": "Romero",
            "leg_reach": 42.0,
            "loss": 5,
            "rank": 5,
            "sex": "M",
            "weight": 185.0,
            "win": 13
        }
    ],
    "div_7": [
        {
            "age": 37,
            "arm_reach": 78.0,
            "division": 7,
            "draw": 0,
            "first_name": "Jan",
            "height": 74.0,
            "id": 106,
            "last_name": "Blachowicz",
            "leg_reach": 44.0,
            "loss": 8,
            "rank": 0,
            "sex": "M",
            "weight": 216.0,
            "win": 27
        },
        {
            "age": 41,
            "arm_reach": 76.0,
            "division": 7,
            "draw": 0,
            "first_name": "Glover",
            "height": 74.0,
            "id": 107,
            "last_name": "Teixeira",
            "leg_reach": 42.5,
            "loss": 7,
            "rank": 1,
            "sex": "M",
            "weight": 205.0,
            "win": 31
        },
        {
            "age": 36,
            "arm_reach": 76.0,
            "division": 7,
            "draw": 0,
            "first_name": "Thiago",
            "height": 74.0,
            "id": 108,
            "last_name": "Santos",
            "leg_reach": 42.5,
            "loss": 8,
            "rank": 2,
            "sex": "M",
            "weight": 205.0,
            "win": 21
        },
        {
            "age": 30,
            "arm_reach": 77.0,
            "division": 7,
            "draw": 0,
            "first_name": "Dominick",
            "height": 76.0,
            "id": 109,
            "last_name": "Reyes",
            "leg_reach": 43.5,
            "loss": 1,
            "rank": 3,
            "sex": "M",
            "weight": 205.0,
            "win": 12
        },
        {
            "age": 28,
            "arm_reach": 78.0,
            "division": 7,
            "draw": 0,
            "first_name": "Aleksandar",
            "height": 76.0,
            "id": 110,
            "last_name": "Rakic",
            "leg_reach": 46.0,
            "loss": 2,
            "rank": 4,
            "sex": "M",
            "weight": 205.0,
            "win": 13
        },
        {
            "age": 27,
            "arm_reach": 80.0,
            "division": 7,
            "draw": 1,
            "first_name": "Jiri",
            "height": 75.0,
            "id": 111,
            "last_name": "Prochazka",
            "leg_reach": 45.0,
            "loss": 3,
            "rank": 5,
            "sex": "M",
            "weight": 205.0,
            "win": 27
        }
    ],
    "div_8": [
        {
            "age": 37,
            "arm_reach": 80.0,
            "division": 8,
            "draw": 0,
            "first_name": "Stipe",
            "height": 77.0,
            "id": 112,
            "last_name": "Miocic",
            "leg_reach": 39.0,
            "loss": 3,
            "rank": 0,
            "sex": "M",
            "weight": 240.0,
            "win": 20
        },
        {
            "age": 33,
            "arm_reach": 83.0,
            "division": 8,
            "draw": 0,
            "first_name": "Francis",
            "height": 76.0,
            "id": 113,
            "last_name": "Ngannou",
            "leg_reach": 44.5,
            "loss": 3,
            "rank": 1,
            "sex": "M",
            "weight": 250.0,
            "win": 15
        },
        {
            "age": 29,
            "arm_reach": 80.0,
            "division": 8,
            "draw": 0,
            "first_name": "Curtis",
            "height": 76.0,
            "id": 114,
            "last_name": "Blaydes",
            "leg_reach": 46.0,
            "loss": 2,
            "rank": 2,
            "sex": "M",
            "weight": 265.0,
            "win": 14
        },
        {
            "age": 32,
            "arm_reach": 78.0,
            "division": 8,
            "draw": 0,
            "first_name": "Jairzinho",
            "height": 76.0,
            "id": 115,
            "last_name": "Rozenstruik",
            "leg_reach": 41.0,
            "loss": 1,
            "rank": 3,
            "sex": "M",
            "weight": 242.0,
            "win": 11
        },
        {
            "age": 35,
            "arm_reach": 79.0,
            "division": 8,
            "draw": 0,
            "first_name": "Derrick",
            "height": 75.0,
            "id": 116,
            "last_name": "Lewis",
            "leg_reach": 43.5,
            "loss": 7,
            "rank": 4,
            "sex": "M",
            "weight": 260.0,
            "win": 23
        },
        {
            "age": 40,
            "arm_reach": 80.0,
            "division": 8,
            "draw": 0,
            "first_name": "Alistair",
            "height": 76.0,
            "id": 117,
            "last_name": "Overeem",
            "leg_reach": 44.5,
            "loss": 18,
            "rank": 5,
            "sex": "M",
            "weight": 260.0,
            "win": 47
        }
    ],
    "div_9": [
        {
            "age": 30,
            "arm_reach": 63.0,
            "division": 9,
            "draw": 0,
            "first_name": "Weili",
            "height": 64.0,
            "id": 118,
            "last_name": "Zhang",
            "leg_reach": 36.0,
            "loss": 1,
            "rank": 0,
            "sex": "F",
            "weight": 115.0,
            "win": 21
        },
        {
            "age": 28,
            "arm_reach": 65.0,
            "division": 9,
            "draw": 0,
            "first_name": "Rose",
            "height": 65.0,
            "id": 119,
            "last_name": "Namajunas",
            "leg_reach": 39.5,
            "loss": 4,
            "rank": 1,
            "sex": "F",
            "weight": 115.0,
            "win": 10
        },
        {
            "age": 32,
            "arm_reach": 65.5,
            "division": 9,
            "draw": 0,
            "first_name": "Joanna",
            "height": 66.0,
            "id": 120,
            "last_name": "Jedrzejczyk",
            "leg_reach": 35.0,
            "loss": 4,
            "rank": 2,
            "sex": "F",
            "weight": 115.0,
            "win": 16
        },
        {
            "age": 31,
            "arm_reach": 63.0,
            "division": 9,
            "draw": 0,
            "first_name": "Yan",
            "height": 65.0,
            "id": 121,
            "last_name": "Xiaonan",
            "leg_reach": 37.0,
            "loss": 1,
            "rank": 3,
            "sex": "F",
            "weight": 115.0,
            "win": 13
        },
        {
            "age": 32,
            "arm_reach": 63.0,
            "division": 9,
            "draw": 0,
            "first_name": "Carla",
            "height": 61.0,
            "id": 122,
            "last_name": "Esparza",
            "leg_reach": 35.0,
            "loss": 6,
            "rank": 4,
            "sex": "F",
            "weight": 115.0,
            "win": 18
        },
        {
            "age": 34,
            "arm_reach": 64.0,
            "division": 9,
            "draw": 0,
            "first_name": "Nina",
            "height": 65.0,
            "id": 123,
            "last_name": "Ansaroff",
            "leg_reach": 39.0,
            "loss": 6,
            "rank": 5,
            "sex": "F",
            "weight": 115.0,
            "win": 10
        }
    ],
    "events": [
        {
            "event_date": "Sat 12, 19, 2020 4:00PM",
            "event_name": "UFC Fight Night: Thompson vs. Neal",
            "location": "UFC APEX, Las Vegas, NV"
        }
    ],
    "success": true
}
```
### GET /api/division_fighters/<int:division_id>
* General: Gets fighters by division.
* Does not require authorization.
* Example: curl https://ufc-fan.herokuapp.com/api/division_fighters/1
```
{
    "data": [
        {
            "age": 35,
            "arm_reach": 65.0,
            "div_id": 1,
            "div_name": "Men's Flyweight",
            "division": 1,
            "draw": 0,
            "first_name": "Joseph",
            "height": 64.0,
            "id": 71,
            "last_name": "Benavidez",
            "leg_reach": 36.0,
            "loss": 7,
            "rank": 1,
            "sex": "M",
            "weight": 126.0,
            "win": 28
        },
        {
            "age": 27,
            "arm_reach": 67.0,
            "div_id": 1,
            "div_name": "Men's Flyweight",
            "division": 1,
            "draw": 1,
            "first_name": "Askar",
            "height": 66.0,
            "id": 73,
            "last_name": "Askarov",
            "leg_reach": 36.0,
            "loss": 0,
            "rank": 3,
            "sex": "M",
            "weight": 125.0,
            "win": 11
        },
        {
            "age": 28,
            "arm_reach": 65.5,
            "div_id": 1,
            "div_name": "Men's Flyweight",
            "division": 1,
            "draw": 0,
            "first_name": "Alex",
            "height": 66.0,
            "id": 74,
            "last_name": "Perez",
            "leg_reach": 38.0,
            "loss": 5,
            "rank": 4,
            "sex": "M",
            "weight": 125.0,
            "win": 24
        },
        {
            "age": 30,
            "arm_reach": 67.0,
            "div_id": 1,
            "div_name": "Men's Flyweight",
            "division": 1,
            "draw": 0,
            "first_name": "Alexandre",
            "height": 65.0,
            "id": 75,
            "last_name": "Pantoja",
            "leg_reach": 36.5,
            "loss": 5,
            "rank": 5,
            "sex": "M",
            "weight": 125.0,
            "win": 22
        },
        {
            "age": 32,
            "arm_reach": 68.0,
            "div_id": 1,
            "div_name": "Men's Flyweight",
            "division": 1,
            "draw": 1,
            "first_name": "Deiveson",
            "height": 65.0,
            "id": 70,
            "last_name": "Figueiredo",
            "leg_reach": 38.0,
            "loss": 1,
            "rank": 0,
            "sex": "M",
            "weight": 125.0,
            "win": 19
        },
        {
            "age": 26,
            "arm_reach": 70.0,
            "div_id": 1,
            "div_name": "Men's Flyweight",
            "division": 1,
            "draw": 2,
            "first_name": "Brandon",
            "height": 67.0,
            "id": 72,
            "last_name": "Moreno",
            "leg_reach": 38.0,
            "loss": 5,
            "rank": 2,
            "sex": "M",
            "weight": 125.0,
            "win": 17
        }
    ],
    "success": true
}
```
### GET /api/event/<date>
* General: Gets an event by date.
* Does not require authorization.
* Example: curl https://ufc-fan.herokuapp.com/api/event/2020-12-19%2016:00:00
```
{
    "event_info": [
        {
            "div_id": 5,
            "div_name": "Men's Welterweight",
            "division": 5,
            "event_date": "Sat 12, 19, 2020 4:00PM",
            "event_name": "UFC Fight Night: Thompson vs. Neal",
            "fight_order": 1,
            "fighter_1": "Thompson",
            "fighter_1_odds": -100,
            "fighter_1_votes": 18,
            "fighter_2": "Neal",
            "fighter_2_odds": 200,
            "fighter_2_votes": 8,
            "location": "UFC APEX, Las Vegas, NV"
        },
        {
            "div_id": 2,
            "div_name": "Men's Bantamweight",
            "division": 2,
            "event_date": "Sat 12, 19, 2020 4:00PM",
            "event_name": "UFC Fight Night: Thompson vs. Neal",
            "fight_order": 2,
            "fighter_1": "Aldo",
            "fighter_1_odds": -150,
            "fighter_1_votes": 7,
            "fighter_2": "Vera",
            "fighter_2_odds": 100,
            "fighter_2_votes": 8,
            "location": "UFC APEX, Las Vegas, NV"
        },
        {
            "div_id": 5,
            "div_name": "Men's Welterweight",
            "division": 5,
            "event_date": "Sat 12, 19, 2020 4:00PM",
            "event_name": "UFC Fight Night: Thompson vs. Neal",
            "fight_order": 3,
            "fighter_1": "Pereira",
            "fighter_1_odds": -200,
            "fighter_1_votes": 9,
            "fighter_2": "Williams",
            "fighter_2_odds": 100,
            "fighter_2_votes": 19,
            "location": "UFC APEX, Las Vegas, NV"
        },
        {
            "div_id": 2,
            "div_name": "Men's Bantamweight",
            "division": 2,
            "event_date": "Sat 12, 19, 2020 4:00PM",
            "event_name": "UFC Fight Night: Thompson vs. Neal",
            "fight_order": 4,
            "fighter_1": "Moraes",
            "fighter_1_odds": 100,
            "fighter_1_votes": 3,
            "fighter_2": "Font",
            "fighter_2_odds": -100,
            "fighter_2_votes": 4,
            "location": "UFC APEX, Las Vegas, NV"
        },
        {
            "div_id": 8,
            "div_name": "Men's Heavyweight",
            "division": 8,
            "event_date": "Sat 12, 19, 2020 4:00PM",
            "event_name": "UFC Fight Night: Thompson vs. Neal",
            "fight_order": 5,
            "fighter_1": "Tybura",
            "fighter_1_odds": 200,
            "fighter_1_votes": 14,
            "fighter_2": "Hardy",
            "fighter_2_odds": -100,
            "fighter_2_votes": 4,
            "location": "UFC APEX, Las Vegas, NV"
        }
    ],
    "success": true
}
```
### GET /api/event-create
### Permissions needed (get:event-create)
* General: Gets form to create an event.
* The endpoint does require authorization token with permission - get:event-create.
    * Login with Admin or Event Editor credentials, then obtain JWT token at https://ufc-fan.herokuapp.com/api-key
    * In terminal, export ROLE_TOKEN=<jwt> with active Admin or Event Editor JWT before request.
* Example: curl -H "Authorization: Bearer $ROLE_TOKEN" -X GET https://ufc-fan.herokuapp.com/api/event-create
```
{
    "success": true
}
```
### POST /api/event-create
### Permissions needed (post:event-create)
* General: Post form to create an event.
* The endpoint does require authorization token with permission - post:event-create
    * Login with Admin or Event Editor credentials, then obtain JWT token at https://ufc-fan.herokuapp.com/api-key
    * In terminal, export ROLE_TOKEN=<jwt> with active Admin or Event Editor JWT before request.
* Example: curl -d '{
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
    }' -H "Content-Type: application/json" -H "Authorization: Bearer $ROLE_TOKEN" -X POST https://ufc-fan.herokuapp.com/api/event-create

```
{
    "id": 36,
    "success": true
}
```
### PATCH /api/event/plus/<name>/number
* General: Add a vote for a fighter.
* The endpoint does not require authorization token.
* Example: curl -X PATCH https://ufc-fan.herokuapp.com/api/event/plus/Hammer/2
```
{
    "fighter_votes": [
        {
            "fighter_2_votes": 1,
            "fighter_number": 2
        }
    ],
    "success": true
}
```
### GET /api/event-delete/<date>
### Permissions needed (get:event-delete)
* General: Gets event to delete. Please use event-create first.
* The endpoint does require authorization token with permission - get:event-delete.
    * Login with Admin or Event Editor credentials, then obtain JWT token at https://ufc-fan.herokuapp.com/api-key
    * In terminal, export ROLE_TOKEN=<jwt> with active Admin or Event Editor JWT before request.
* Example: curl -H "Authorization: Bearer $ROLE_TOKEN" -X GET https://ufc-fan.herokuapp.com/api/event-delete/2020-12-12T12:00:00.000Z
```
{
    "event_data": [
        {
            "division": 1,
            "event_date": "Sat, 12 Dec 2020 12:00:00 GMT",
            "event_name": "UFC",
            "fight_order": 0,
            "fighter_1": "Doorman",
            "fighter_1_odds": 0,
            "fighter_1_votes": 0,
            "fighter_2": "Hammer",
            "fighter_2_odds": 0,
            "fighter_2_votes": 0,
            "id": 33,
            "location": "Somewhere"
        },
        {
            "division": 1,
            "event_date": "Sat, 12 Dec 2020 12:00:00 GMT",
            "event_name": "UFC",
            "fight_order": 0,
            "fighter_1": "Doorman",
            "fighter_1_odds": 0,
            "fighter_1_votes": 0,
            "fighter_2": "Hammer",
            "fighter_2_odds": 0,
            "fighter_2_votes": 0,
            "id": 34,
            "location": "Somewhere"
        },
        {
            "division": 1,
            "event_date": "Sat, 12 Dec 2020 12:00:00 GMT",
            "event_name": "UFC",
            "fight_order": 0,
            "fighter_1": "Doorman",
            "fighter_1_odds": 0,
            "fighter_1_votes": 0,
            "fighter_2": "Hammer",
            "fighter_2_odds": 0,
            "fighter_2_votes": 0,
            "id": 36,
            "location": "Somewhere"
        },
        {
            "division": 1,
            "event_date": "Sat, 12 Dec 2020 12:00:00 GMT",
            "event_name": "UFC",
            "fight_order": 0,
            "fighter_1": "Doorman",
            "fighter_1_odds": 0,
            "fighter_1_votes": 0,
            "fighter_2": "Hammer",
            "fighter_2_odds": 0,
            "fighter_2_votes": 1,
            "id": 32,
            "location": "Somewhere"
        }
    ],
    "success": true
}
```
### DELETE /api/event-delete/<date>
### Permissions needed (delete:event-delete)
* General: Delete event by date. Please use event-create first.
* The endpoint does require authorization token with permission - delete:event-delete.
    * Login with Admin or Event Editor credentials, then obtain JWT token at https://ufc-fan.herokuapp.com/api-key
    * In terminal, export ROLE_TOKEN=<jwt> with active Admin or Event Editor JWT before request.
* Example: curl -H "Authorization: Bearer $ROLE_TOKEN" -X DELETE https://ufc-fan.herokuapp.com/api/event-delete/2020-12-12T12:00:00.000Z
```
{
    "deleted": "2020-12-12T12:00:00.000Z",
    "success": true
}
```
### DELETE /api/event-delete/<int:id>
### Permissions needed (delete:event-delete)
* General: Delete event by id. Please use event-create first and look in your database for the id to test delete id endpoint.
* The endpoint does require authorization token with permission - delete:event-delete.
    * Login with Admin or Event Editor credentials, then obtain JWT token at https://ufc-fan.herokuapp.com/api-key
    * In terminal, export ROLE_TOKEN=<jwt> with active Admin or Event Editor JWT before request.
* Example: curl -H "Authorization: Bearer $ROLE_TOKEN" -X DELETE https://ufc-fan.herokuapp.com/api/event-delete/35
```
{
    "deleted": 35,
    "success": true
}
```
### GET /api/fighter-edit/<int:fighter_id>
### Permissions needed (get:figher-edit)
* General: Get fighter to edit by id. Confirm id of fighter in your database for test
* The endpoint does require authorization token with permission - get:figher-edit.
    * Login with Admin credentials, then obtain JWT token at https://ufc-fan.herokuapp.com/api-key
    * In terminal, export ROLE_TOKEN=<jwt> with active Admin or Event Editor JWT before request.
* Example: curl -H "Authorization: Bearer $ROLE_TOKEN" -X GET https://ufc-fan.herokuapp.com/api/fighter-edit/71
```
{
    "fighter_details": {
        "age": 35,
        "arm_reach": 65.0,
        "division": 1,
        "draw": 0,
        "first_name": "Joseph",
        "height": 64.0,
        "id": 71,
        "last_name": "Benavidez",
        "leg_reach": 36.0,
        "loss": 7,
        "rank": 1,
        "sex": "M",
        "weight": 126.0,
        "win": 28
    },
    "success": true
}
```
### POST /api/fighter-edit/<int:fighter_id>
### Permissions needed (post:figher-edit)
* General: Edit fighter to for division rank by id. Confirm id of fighter in your database for test
* The endpoint does require authorization token with permission - post:figher-edit.
    * Login with Admin credentials, then obtain JWT token at https://ufc-fan.herokuapp.com/api-key
    * In terminal, export ROLE_TOKEN=<jwt> with active Admin or Event Editor JWT before request.
* Example: curl -d '{
    'first_name':'Megan',
    'last_name':'Anderson',
    'age':31,
    'height':72,
    'weight':145,
    'arm_reach':68,
    'leg_reach':40,
    'sex':'F',
    'win':8,
    'loss':2,
    'draw':0,
    'division':12,
    'rank':2}' -H "Authorization: Bearer $ROLE_TOKEN" -X POST https://ufc-fan.herokuapp.com/api/fighter-edit/138
```
{
  "division_id": 12,
  "success": true
}
```
### Authors
Christian Daconta created the UFC Fan application.  The project was designed to fullful the requirement set for by the Full Stack Web Developer Nanodegree at Udacity.com.