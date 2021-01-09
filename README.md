# UFC FAN

This application is a fan site for the Ultimate Fighting Championship (UFC).  The site is hosted on Heroku at https://www.ufc-fan.com. Anyone can create a public account and learn about the UFC divisions and an upcoming Event.  The landing page shows all twelve divisions and an upcoming event for the UFC.  The user can take a deeper look at the divisions and also vote on the main card fighters in that upcoming event.  Admin and the Event Editor have special priveleges to edit fighters or edit event information.

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
* Example: curl https://www.ufc-fan.com/api/index
```
{"success": true,
"events": [
    {"event_name": "UFC Fight Night: Holloway vs. Kattar", "event_date": "Saturday January, 16,
2021 at 12:00PM", "location": "Etihad Arena, Abu Dhabi, United Arab Emirates"}],
"div_data": [
    {"id": 70, "first_name":"Deiveson", "last_name": "Figueiredo", "age": 32, "height": 65.0,
"weight": 125.0, "arm_reach": 68.0, "leg_reach": 38.0,"sex": "M", "win": 19, "loss": 1, "draw": 1, "division": 1, "rank": 0},
{"id": 72, "first_name": "Brandon", "last_name":"Moreno", "age": 26, "height": 67.0, "weight": 125.0,
"arm_reach": 70.0, "leg_reach": 38.0, "sex": "M", "win": 17,"loss": 5, "draw": 2, "division": 1, "rank": 1},
{"id": 71, "first_name": "Joseph", "last_name": "Benavidez", "age": 35,
"height": 64.0, "weight": 126.0, "arm_reach": 65.0, "leg_reach": 36.0, "sex": "M", "win": 28, "loss": 7, "draw": 0,
"division": 1, "rank": 2}, {"id": 73, "first_name": "Askar", "last_name": "Askarov", "age": 27, "height": 66.0,
"weight": 125.0, "arm_reach": 67.0, "leg_reach": 36.0, "sex": "M", "win": 11, "loss": 0, "draw": 1, "division": 1,
"rank": 3}, {"id": 74, "first_name": "Alex", "last_name": "Perez", "age": 28, "height": 66.0, "weight": 125.0,
"arm_reach": 65.5, "leg_reach": 38.0, "sex": "M", "win": 24, "loss": 5, "draw": 0, "division": 1, "rank": 4}, {"id": 75,
"first_name": "Alexandre", "last_name": "Pantoja", "age": 30, "height": 65.0, "weight": 125.0, "arm_reach": 67.0,
"leg_reach": 36.5, "sex": "M", "win": 22, "loss": 5, "draw": 0, "division": 1, "rank": 5}, {"id": 76, "first_name":
"Petr", "last_name": "Yan", "age": 27, "height": 67.5, "weight": 135.0, "arm_reach": 67.0, "leg_reach": 38.0, "sex":
"M", "win": 15, "loss": 1, "draw": 0, "division": 2, "rank": 0}, {"id": 77, "first_name": "Aljamain", "last_name":
"Sterling", "age": 30, "height": 67.0, "weight": 136.0, "arm_reach": 71.0, "leg_reach": 39.0, "sex": "M", "win": 19,
"loss": 3, "draw": 0, "division": 2, "rank": 1}, {"id": 78, "first_name": "Cory", "last_name": "Sandhagen", "age": 28,
"height": 71.0, "weight": 135.0, "arm_reach": 70.0, "leg_reach": 40.0, "sex": "M", "win": 13, "loss": 2, "draw": 0,
"division": 2, "rank": 2}, {"id": 79, "first_name": "Marlon", "last_name": "Moraes", "age": 32, "height": 66.0,
"weight": 135.0, "arm_reach": 67.0, "leg_reach": 37.0, "sex": "M", "win": 23, "loss": 7, "draw": 1, "division": 2,
"rank": 3}, {"id": 80, "first_name": "Cody", "last_name": "Garbrandt", "age": 28, "height": 68.0, "weight": 135.0,
"arm_reach": 65.5, "leg_reach": 38.0, "sex": "M", "win": 12, "loss": 3, "draw": 0, "division": 2, "rank": 4}, {"id": 81,
"first_name": "Frankie", "last_name": "Edgar", "age": 38, "height": 66.0, "weight": 135.0, "arm_reach": 68.0,
"leg_reach": 37.5, "sex": "M", "win": 23, "loss": 8, "draw": 1, "division": 2, "rank": 5}, {"id": 82, "first_name":
"Alexander", "last_name": "Volkanovski", "age": 31, "height": 66.0, "weight": 145.0, "arm_reach": 71.5, "leg_reach":
36.0, "sex": "M", "win": 22, "loss": 1, "draw": 0, "division": 3, "rank": 0}, {"id": 83, "first_name": "Max",
"last_name": "Holloway", "age": 28, "height": 71.0, "weight": 146.0, "arm_reach": 69.0, "leg_reach": 42.0, "sex": "M",
"win": 21, "loss": 6, "draw": 0, "division": 3, "rank": 1}, {"id": 84, "first_name": "Brian", "last_name": "Ortega",
"age": 29, "height": 68.0, "weight": 145.0, "arm_reach": 69.0, "leg_reach": 39.0, "sex": "M", "win": 15, "loss": 1,
"draw": 0, "division": 3, "rank": 2}, {"id": 85, "first_name": "Zabit", "last_name": "Magomedsharipov", "age": 29,
"height": 73.0, "weight": 145.0, "arm_reach": 73.0, "leg_reach": 42.0, "sex": "M", "win": 18, "loss": 1, "draw": 0,
"division": 3, "rank": 3}, {"id": 86, "first_name": "Yair", "last_name": "Rodriguez", "age": 27, "height": 71.0,
"weight": 145.0, "arm_reach": 71.0, "leg_reach": 41.5, "sex": "M", "win": 13, "loss": 2, "draw": 0, "division": 3,
"rank": 4}, {"id": 87, "first_name": "Chan", "last_name": "Sung Jung", "age": 33, "height": 67.0, "weight": 145.0,
"arm_reach": 72.0, "leg_reach": 38.5, "sex": "M", "win": 16, "loss": 6, "draw": 0, "division": 3, "rank": 5}, {"id": 88,
"first_name": "Khabib", "last_name": "Nurmagomedov", "age": 32, "height": 70.0, "weight": 155.0, "arm_reach": 70.0,
"leg_reach": 40.0, "sex": "M", "win": 28, "loss": 0, "draw": 0, "division": 4, "rank": 0}, {"id": 89, "first_name":
"Justin", "last_name": "Gaethje", "age": 31, "height": 71.0, "weight": 155.0, "arm_reach": 70.0, "leg_reach": 40.0,
"sex": "M", "win": 22, "loss": 3, "draw": 0, "division": 4, "rank": 1}, {"id": 90, "first_name": "Dustin", "last_name":
"Poirier", "age": 31, "height": 69.0, "weight": 155.0, "arm_reach": 72.0, "leg_reach": 40.5, "sex": "M", "win": 26,
"loss": 6, "draw": 0, "division": 4, "rank": 2}, {"id": 91, "first_name": "Tony", "last_name": "Ferguson", "age": 36,
"height": 71.0, "weight": 155.0, "arm_reach": 76.5, "leg_reach": 40.5, "sex": "M", "win": 26, "loss": 5, "draw": 0,
"division": 4, "rank": 3}, {"id": 92, "first_name": "Conor", "last_name": "McGregor", "age": 32, "height": 69.0,
"weight": 145.0, "arm_reach": 74.0, "leg_reach": 40.0, "sex": "M", "win": 22, "loss": 4, "draw": 0, "division": 4,
"rank": 4}, {"id": 93, "first_name": "Dan", "last_name": "Hooker", "age": 30, "height": 72.0, "weight": 145.0,
"arm_reach": 75.0, "leg_reach": 42.5, "sex": "M", "win": 20, "loss": 9, "draw": 0, "division": 4, "rank": 5}, {"id": 94,
"first_name": "Kamaru", "last_name": "Usman", "age": 33, "height": 72.0, "weight": 170.0, "arm_reach": 76.0,
"leg_reach": 41.0, "sex": "M", "win": 17, "loss": 1, "draw": 0, "division": 5, "rank": 0}, {"id": 95, "first_name":
"Colby", "last_name": "Covington", "age": 32, "height": 71.0, "weight": 170.0, "arm_reach": 72.0, "leg_reach": 41.0,
"sex": "M", "win": 15, "loss": 2, "draw": 0, "division": 5, "rank": 1}, {"id": 96, "first_name": "Gilbert", "last_name":
"Burns", "age": 33, "height": 70.0, "weight": 155.0, "arm_reach": 71.0, "leg_reach": 40.0, "sex": "M", "win": 19,
"loss": 3, "draw": 0, "division": 5, "rank": 2}, {"id": 97, "first_name": "Leon", "last_name": "Edwards", "age": 28,
"height": 72.0, "weight": 170.0, "arm_reach": 74.0, "leg_reach": 43.0, "sex": "M", "win": 18, "loss": 3, "draw": 0,
"division": 5, "rank": 3}, {"id": 98, "first_name": "Jorge", "last_name": "Masvidal", "age": 35, "height": 71.0,
"weight": 156.0, "arm_reach": 74.0, "leg_reach": 39.5, "sex": "M", "win": 35, "loss": 14, "draw": 0, "division": 5,
"rank": 4}, {"id": 99, "first_name": "Stephen", "last_name": "Thompson", "age": 37, "height": 72.0, "weight": 170.0,
"arm_reach": 75.0, "leg_reach": 42.0, "sex": "M", "win": 16, "loss": 4, "draw": 1, "division": 5, "rank": 5}, {"id":
100, "first_name": "Israel", "last_name": "Adesanya", "age": 31, "height": 76.0, "weight": 185.0, "arm_reach": 80.0,
"leg_reach": 44.5, "sex": "M", "win": 19, "loss": 0, "draw": 0, "division": 6, "rank": 0}, {"id": 101, "first_name":
"Robert", "last_name": "Whittaker", "age": 29, "height": 72.0, "weight": 185.0, "arm_reach": 73.5, "leg_reach": 43.0,
"sex": "M", "win": 22, "loss": 5, "draw": 0, "division": 6, "rank": 1}, {"id": 102, "first_name": "Paulo", "last_name":
"Costa", "age": 29, "height": 73.0, "weight": 185.0, "arm_reach": 72.0, "leg_reach": 39.5, "sex": "M", "win": 13,
"loss": 0, "draw": 0, "division": 6, "rank": 2}, {"id": 103, "first_name": "Jared", "last_name": "Cannonier", "age": 36,
"height": 71.0, "weight": 205.0, "arm_reach": 77.5, "leg_reach": 41.5, "sex": "M", "win": 13, "loss": 4, "draw": 0,
"division": 6, "rank": 3}, {"id": 104, "first_name": "Jack", "last_name": "Hermansson", "age": 32, "height": 73.0,
"weight": 186.0, "arm_reach": 77.5, "leg_reach": 46.5, "sex": "M", "win": 21, "loss": 5, "draw": 0, "division": 6,
"rank": 4}, {"id": 105, "first_name": "Yoel", "last_name": "Romero", "age": 43, "height": 72.0, "weight": 185.0,
"arm_reach": 73.5, "leg_reach": 42.0, "sex": "M", "win": 13, "loss": 5, "draw": 0, "division": 6, "rank": 5}, {"id":
106, "first_name": "Jan", "last_name": "Blachowicz", "age": 37, "height": 74.0, "weight": 216.0, "arm_reach": 78.0,
"leg_reach": 44.0, "sex": "M", "win": 27, "loss": 8, "draw": 0, "division": 7, "rank": 0}, {"id": 107, "first_name":
"Glover", "last_name": "Teixeira", "age": 41, "height": 74.0, "weight": 205.0, "arm_reach": 76.0, "leg_reach": 42.5,
"sex": "M", "win": 31, "loss": 7, "draw": 0, "division": 7, "rank": 1}, {"id": 108, "first_name": "Thiago", "last_name":
"Santos", "age": 36, "height": 74.0, "weight": 205.0, "arm_reach": 76.0, "leg_reach": 42.5, "sex": "M", "win": 21,
"loss": 8, "draw": 0, "division": 7, "rank": 2}, {"id": 109, "first_name": "Dominick", "last_name": "Reyes", "age": 30,
"height": 76.0, "weight": 205.0, "arm_reach": 77.0, "leg_reach": 43.5, "sex": "M", "win": 12, "loss": 1, "draw": 0,
"division": 7, "rank": 3}, {"id": 110, "first_name": "Aleksandar", "last_name": "Rakic", "age": 28, "height": 76.0,
"weight": 205.0, "arm_reach": 78.0, "leg_reach": 46.0, "sex": "M", "win": 13, "loss": 2, "draw": 0, "division": 7,
"rank": 4}, {"id": 111, "first_name": "Jiri", "last_name": "Prochazka", "age": 27, "height": 75.0, "weight": 205.0,
"arm_reach": 80.0, "leg_reach": 45.0, "sex": "M", "win": 27, "loss": 3, "draw": 1, "division": 7, "rank": 5}, {"id":
112, "first_name": "Stipe", "last_name": "Miocic", "age": 37, "height": 77.0, "weight": 240.0, "arm_reach": 80.0,
"leg_reach": 39.0, "sex": "M", "win": 20, "loss": 3, "draw": 0, "division": 8, "rank": 0}, {"id": 113, "first_name":
"Francis", "last_name": "Ngannou", "age": 33, "height": 76.0, "weight": 250.0, "arm_reach": 83.0, "leg_reach": 44.5,
"sex": "M", "win": 15, "loss": 3, "draw": 0, "division": 8, "rank": 1}, {"id": 114, "first_name": "Curtis", "last_name":
"Blaydes", "age": 29, "height": 76.0, "weight": 265.0, "arm_reach": 80.0, "leg_reach": 46.0, "sex": "M", "win": 14,
"loss": 2, "draw": 0, "division": 8, "rank": 2}, {"id": 115, "first_name": "Jairzinho", "last_name": "Rozenstruik",
"age": 32, "height": 76.0, "weight": 242.0, "arm_reach": 78.0, "leg_reach": 41.0, "sex": "M", "win": 11, "loss": 1,
"draw": 0, "division": 8, "rank": 3}, {"id": 116, "first_name": "Derrick", "last_name": "Lewis", "age": 35, "height":
75.0, "weight": 260.0, "arm_reach": 79.0, "leg_reach": 43.5, "sex": "M", "win": 23, "loss": 7, "draw": 0, "division": 8,
"rank": 4}, {"id": 117, "first_name": "Alistair", "last_name": "Overeem", "age": 40, "height": 76.0, "weight": 260.0,
"arm_reach": 80.0, "leg_reach": 44.5, "sex": "M", "win": 47, "loss": 18, "draw": 0, "division": 8, "rank": 5}, {"id":
118, "first_name": "Weili", "last_name": "Zhang", "age": 30, "height": 64.0, "weight": 115.0, "arm_reach": 63.0,
"leg_reach": 36.0, "sex": "F", "win": 21, "loss": 1, "draw": 0, "division": 9, "rank": 0}, {"id": 119, "first_name":
"Rose", "last_name": "Namajunas", "age": 28, "height": 65.0, "weight": 115.0, "arm_reach": 65.0, "leg_reach": 39.5,
"sex": "F", "win": 10, "loss": 4, "draw": 0, "division": 9, "rank": 1}, {"id": 120, "first_name": "Joanna", "last_name":
"Jedrzejczyk", "age": 32, "height": 66.0, "weight": 115.0, "arm_reach": 65.5, "leg_reach": 35.0, "sex": "F", "win": 16,
"loss": 4, "draw": 0, "division": 9, "rank": 2}, {"id": 121, "first_name": "Yan", "last_name": "Xiaonan", "age": 31,
"height": 65.0, "weight": 115.0, "arm_reach": 63.0, "leg_reach": 37.0, "sex": "F", "win": 13, "loss": 1, "draw": 0,
"division": 9, "rank": 3}, {"id": 122, "first_name": "Carla", "last_name": "Esparza", "age": 32, "height": 61.0,
"weight": 115.0, "arm_reach": 63.0, "leg_reach": 35.0, "sex": "F", "win": 18, "loss": 6, "draw": 0, "division": 9,
"rank": 4}, {"id": 123, "first_name": "Nina", "last_name": "Ansaroff", "age": 34, "height": 65.0, "weight": 115.0,
"arm_reach": 64.0, "leg_reach": 39.0, "sex": "F", "win": 10, "loss": 6, "draw": 0, "division": 9, "rank": 5}, {"id":
124, "first_name": "Valentina", "last_name": "Shevchenko", "age": 32, "height": 65.0, "weight": 125.0, "arm_reach":
67.0, "leg_reach": 38.0, "sex": "F", "win": 19, "loss": 3, "draw": 0, "division": 10, "rank": 0}, {"id": 125,
"first_name": "Jessica", "last_name": "Andrade", "age": 29, "height": 61.5, "weight": 135.0, "arm_reach": 62.0,
"leg_reach": 35.0, "sex": "F", "win": 21, "loss": 8, "draw": 0, "division": 10, "rank": 1}, {"id": 126, "first_name":
"Katlyn", "last_name": "Chookagian", "age": 31, "height": 69.0, "weight": 125.0, "arm_reach": 68.0, "leg_reach": 42.0,
"sex": "F", "win": 14, "loss": 4, "draw": 0, "division": 10, "rank": 2}, {"id": 127, "first_name": "Jennifer",
"last_name": "Maia", "age": 32, "height": 64.0, "weight": 125.0, "arm_reach": 64.0, "leg_reach": 38.0, "sex": "F",
"win": 18, "loss": 6, "draw": 1, "division": 10, "rank": 3}, {"id": 128, "first_name": "Cynthia", "last_name":
"Calvillo", "age": 33, "height": 64.0, "weight": 125.0, "arm_reach": 64.0, "leg_reach": 37.0, "sex": "F", "win": 9,
"loss": 1, "draw": 1, "division": 10, "rank": 4}, {"id": 129, "first_name": "Lauren", "last_name": "Murphy", "age": 37,
"height": 65.0, "weight": 135.0, "arm_reach": 67.0, "leg_reach": 38.0, "sex": "F", "win": 13, "loss": 4, "draw": 0,
"division": 10, "rank": 5}, {"id": 130, "first_name": "Amanda", "last_name": "Nunes", "age": 32, "height": 68.0,
"weight": 135.0, "arm_reach": 69.0, "leg_reach": 41.0, "sex": "F", "win": 20, "loss": 4, "draw": 0, "division": 11,
"rank": 0}, {"id": 131, "first_name": "Germaine", "last_name": "de Randamie", "age": 36, "height": 69.0, "weight":
135.0, "arm_reach": 71.0, "leg_reach": 41.0, "sex": "F", "win": 10, "loss": 4, "draw": 0, "division": 11, "rank": 1},
{"id": 132, "first_name": "Holly", "last_name": "Holm", "age": 39, "height": 68.0, "weight": 135.0, "arm_reach": 69.0,
"leg_reach": 38.0, "sex": "F", "win": 14, "loss": 5, "draw": 0, "division": 11, "rank": 2}, {"id": 133, "first_name":
"Aspen", "last_name": "Ladd", "age": 25, "height": 66.0, "weight": 135.0, "arm_reach": 66.0, "leg_reach": 38.5, "sex":
"F", "win": 9, "loss": 1, "draw": 0, "division": 11, "rank": 3}, {"id": 134, "first_name": "Raquel", "last_name":
"Pennington", "age": 31, "height": 67.0, "weight": 135.0, "arm_reach": 67.5, "leg_reach": 37.0, "sex": "F", "win": 11,
"loss": 9, "draw": 0, "division": 11, "rank": 4}, {"id": 135, "first_name": "Irene", "last_name": "Aldana", "age": 32,
"height": 69.0, "weight": 135.0, "arm_reach": 68.5, "leg_reach": 38.5, "sex": "F", "win": 12, "loss": 6, "draw": 0,
"division": 11, "rank": 5}, {"id": 136, "first_name": "Amanda", "last_name": "Nunes", "age": 32, "height": 68.0,
"weight": 135.0, "arm_reach": 69.0, "leg_reach": 41.0, "sex": "F", "win": 20, "loss": 4, "draw": 0, "division": 12,
"rank": 0}, {"id": 137, "first_name": "Felicia", "last_name": "Spencer", "age": 29, "height": 66.0, "weight": 145.0,
"arm_reach": 68.0, "leg_reach": 40.0, "sex": "F", "win": 8, "loss": 2, "draw": 0, "division": 12, "rank": 1}, {"id":
138, "first_name": "Megan", "last_name": "Anderson", "age": 31, "height": 72.0, "weight": 145.0, "arm_reach": 68.0,
"leg_reach": 40.0, "sex": "F", "win": 8, "loss": 2, "draw": 0, "division": 12, "rank": 2}, {"id": 139, "first_name": "",
"last_name": "", "age": 0, "height": 0.0, "weight": 0.0, "arm_reach": 0.0, "leg_reach": 0.0, "sex": "F", "win": 0,
"loss": 0, "draw": 0, "division": 12, "rank": 3}, {"id": 140, "first_name": "", "last_name": "", "age": 0, "height":
0.0, "weight": 0.0, "arm_reach": 0.0, "leg_reach": 0.0, "sex": "F", "win": 0, "loss": 0, "draw": 0, "division": 12,
"rank": 4}, {"id": 141, "first_name": "", "last_name": "", "age": 0, "height": 0.0, "weight": 0.0, "arm_reach": 0.0,
"leg_reach": 0.0, "sex": "F", "win": 0, "loss": 0, "draw": 0, "division": 12, "rank": 5}]}
```
### GET /api/division_fighters/<int:division_id>
* General: Gets fighters by division.
* Does not require authorization.
* Example: curl https://www.ufc-fan.com/api/division_fighters/1
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
* Example: curl https://www.ufc-fan.com/api/event/2020-12-19%2016:00:00
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
    * Login with Admin or Event Editor credentials, then obtain JWT token at https://www.ufc-fan.com/api-key
    * In terminal, export ROLE_TOKEN=<jwt> with active Admin or Event Editor JWT before request.
* Example: curl -H "Authorization: Bearer $ROLE_TOKEN" -X GET https://www.ufc-fan.com/api/event-create
```
{
    "success": true
}
```
### POST /api/event-create
### Permissions needed (post:event-create)
* General: Post form to create an event.
* The endpoint does require authorization token with permission - post:event-create
    * Login with Admin or Event Editor credentials, then obtain JWT token at https://www.ufc-fan.com/api-key
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
    }' -H "Content-Type: application/json" -H "Authorization: Bearer $ROLE_TOKEN" -X POST https://www.ufc-fan.com/api/event-create

```
{
    "id": 36,
    "success": true
}
```
### PATCH /api/event/plus/<name>/number
* General: Add a vote for a fighter.
* The endpoint does not require authorization token.
* Example: curl -X PATCH https://www.ufc-fan.com/api/event/plus/Hammer/2
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
    * Login with Admin or Event Editor credentials, then obtain JWT token at https://www.ufc-fan.com/api-key
    * In terminal, export ROLE_TOKEN=<jwt> with active Admin or Event Editor JWT before request.
* Example: curl -H "Authorization: Bearer $ROLE_TOKEN" -X GET https://www.ufc-fan.com/api/event-delete/2020-12-12T12:00:00.000Z
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
    * Login with Admin or Event Editor credentials, then obtain JWT token at https://www.ufc-fan.com/api-key
    * In terminal, export ROLE_TOKEN=<jwt> with active Admin or Event Editor JWT before request.
* Example: curl -H "Authorization: Bearer $ROLE_TOKEN" -X DELETE https://www.ufc-fan.com/api/event-delete/2020-12-12T12:00:00.000Z
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
    * Login with Admin or Event Editor credentials, then obtain JWT token at https://www.ufc-fan.com/api-key
    * In terminal, export ROLE_TOKEN=<jwt> with active Admin or Event Editor JWT before request.
* Example: curl -H "Authorization: Bearer $ROLE_TOKEN" -X DELETE https://www.ufc-fan.com/api/event-delete/35
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
    * Login with Admin credentials, then obtain JWT token at https://www.ufc-fan.com/api-key
    * In terminal, export ROLE_TOKEN=<jwt> with active Admin or Event Editor JWT before request.
* Example: curl -H "Authorization: Bearer $ROLE_TOKEN" -X GET https://www.ufc-fan.com/api/fighter-edit/71
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
    * Login with Admin credentials, then obtain JWT token at https://www.ufc-fan.com/api-key
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
    'rank':2}' -H "Authorization: Bearer $ROLE_TOKEN" -X POST https://www.ufc-fan.com/api/fighter-edit/138
```
{
  "division_id": 12,
  "success": true
}
```
### Authors
Christian Daconta created the UFC Fan application.  The project was designed to fullful the requirement set for by the Full Stack Web Developer Nanodegree at Udacity.com.