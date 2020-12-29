### UFC FAN   

This application is a fan site for the Ultimate Fighting Championship (UFC).  Anyone can create a public account and learn about the UFC divisions and an upcoming Event.  The landing page shows all twelve divisions and an upcoming event for the UFC.  The user can take a deeper look at the divisions and also vote on the main card fighters in that upcoming event.  Admin and the Event Editor have special priveleges to edit fighters or edit event information.

This project is the capstone project for the Udacity Full Stack Web Developer Nanodegree Program.  Some of the objectives for the project are:
*Architect relational database models in Python
*Utilize SQLAlchemy to conduct database queries
*Follow RESTful principles of API development
*Enable Role Based Authentication and roles-based access control (RBAC) in a Flask application
*Use the unittest library to test endpoint behavior

##API Reference
#Getting Started on Local Machine
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
	pip install -r requirements.txt
```

*	The key dependencies are Flask, SQLalchemy, and Flask-Cors.
*	To run the server, execute:
```
	export FLASK_APP=flaskr
	export FLASK_ENV=development
	flask run
```
* Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.
* Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application.
*	On Windows 10 in the flaskr folder with PowerShell:
```
    $env:FLASK_APP = "__init__"
    $env:FLASK_DEBUG=1
    Flask run	
```

