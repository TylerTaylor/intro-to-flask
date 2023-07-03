# 5. Imports
    # app from app
    # db and Models from models

# 6. Create application context
    # with app.app_context():
    # Info on application context: https://flask.palletsprojects.com/en/1.1.x/appcontext/
    
# 7. Create a query to delete all existing records

# 8. Create some seed data and commit to the database
    print("Creating new services...")
    s1 = Service(name='netflix', price=19.99)
    s2 = Service(name='hulu', price=14.99)
    s3 = Service(name='amazon prime', price=9.99)

    services = [s1, s2, s3]

    # stage our session with updated data
   
    # commit the changes to our database

# 9. Run in terminal
    # python seed.py

# 10. (Optional) Test queries in Flask Shell