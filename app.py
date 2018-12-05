from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from resources.item import Item, ItemList
from security import authenticate, identity
from resources.user import UserRegister
from resources.store import Store, StoreList

# Create the App
app = Flask(__name__)

# Config some SQLAlchemy stuff
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = '12345'

# Create the API
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

# Create JSON Web Token
# JWT creates a new endpoint called '/auth'
# JWT sends the username and password to the auth endpoint
# auth endpoint returns a JWT token, which can be sent to next request. When 
#   that happens JWT calls the 'identity' function and returns the correct user
jwt = JWT(app, authenticate, identity)

    
# Add resource to API
api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

# Prevent the app from running if this file is imported
if __name__ == '__main__':
    # importing here to avoid confusion due to circular import
    from db import db
    db.init_app(app)
    
    # Run app
    app.run(port=5000, debug=True)
