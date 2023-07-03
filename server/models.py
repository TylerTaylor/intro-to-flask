# Import SQLAlchemy from flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy

# Initialize our db
db = SQLAlchemy()

# Create model(s)

# class ClassName(db.Model):
#   __tablename__ = 'table name'

#   id = db.Column(db.Integer, primary_key=True)
#   name = db.Column(db.String)
#   created_at = db.Column(db.DateTime, server_default=db.func.now())
#   updated_at = db.Column(db.DateTime, onupdate=db.func.now())
#   etc

#   def __repr__(self):
#      return f'Some information about the object'

class Service(db.Model):
    __tablename__ = 'services' 

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Float)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__(self):
        return f'<Service Name: {self.name}, Price: ${self.price}>'