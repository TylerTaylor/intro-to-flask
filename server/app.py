#!/usr/bin/env python3

# 1. ✅ Set up models.py - we need to create the DB there, then import it here

# 2. ✅ Set up Imports
    # Flask, jsonify, make_response, request from 'flask'
    # Migrate from 'flask_migrate'
    # db and any models from 'models'

from flask import Flask, jsonify, make_response, request
from flask_migrate import Migrate

from models import db, Service

# 3. ✅ Initialize the App
    # Add `app = Flask(__name__)`
app = Flask(__name__)

    # Configure the database connection by adding:
        # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
        # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Set up the migrations:
        # migrate = Migrate(app, db)
migrate = Migrate(app, db)

    # Finally, actually initialize the application:
        # db.init_app(app)
db.init_app(app)

# 4. ✅ Migrate
    # `cd` into the `server` folder

    # Run in terminal:
        # export FLASK_APP=app.py
        # export FLASK_RUN_PORT=5555
        # flask db init
        # flask db revision --autogenerate -m "Create table <table name>"
        # flask db upgrade

    # Double check the database to verify the migration worked as expected

# 5. ✅ Seed data in `seed.py`

# reddit.com/r/sneakers
# 6. ✅ Routes
@app.before_request
def banana():
    print("This runs before each request")

@app.route('/')
def index():
    return '<h1>Hello World</h1>'

# 7a. Create a dynamic route
    # 7b. Find a "service" by its "name" and send it to our browser
@app.route('/services/<string:name>')
def service_by_name(name):
    # import ipdb; ipdb.set_trace()
    # service = Service.query.filter_by(name == name)
    service = Service.query.filter(Service.name == name).first()

    service_response = {
        "name": service.name,
        "price": service.price,
        "created_at": service.created_at
    }

    response = make_response(
        service_response,
        200
    )

    return response

# Create a route to grab a service by ID
# id is an integer (int)
@app.route('/services/<int:id>')
def service_by_id(id):
    # service = Service.query.filter_by(id == id).first()
    service = Service.query.filter(Service.id == id).first()

    service_response = {
        "id": service.id,
        "name": service.name,
        "price": service.price,
        "created_at": service.created_at
    }

    response = make_response(
        jsonify(service_response), # you don't need jsonify anymore but it still works
        200
    )

    return response


# Note: If you'd like to run the application as a script instead of using `flask run`, uncomment the line below 
# and run `python app.py`

# if __name__ == '__main__':
#     app.run(port=5555, debug=True)