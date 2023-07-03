#!/usr/bin/env python3

# 1. Set up models.py - we need to create the DB there, then import it here

# 2. Set up Imports
    # Flask, jsonify, make_response, request from 'flask'
    # Migrate from 'flask_migrate'
    # db and any models from 'models'

# 3. Initialize the App
    # Add `app = Flask(__name__)`

    # Configure the database connection by adding:
        # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
        # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Set up the migrations:
        # migrate = Migrate(app, db)

    # Finally, actually initialize the application:
        # db.init_app(app)

# 4. Migrate
    # `cd` into the `server` folder

    # Run in terminal:
        # export FLASK_APP=app.py
        # export FLASK_RUN_PORT=5555
        # flask db init
        # flask db revision --autogenerate -m "Create table <table name>"
        # flask db upgrade

    # Double check the database to verify the migration worked as expected

# 5. Seed data in `seed.py`

# 6. Routes

# 7a. Create a dynamic route
    # 7b. Find a "service" by its "name" and send it to our browser


# Note: If you'd like to run the application as a script instead of using `flask run`, uncomment the line below 
# and run `python app.py`

# if __name__ == '__main__':
#     app.run(port=5000, debug=True)