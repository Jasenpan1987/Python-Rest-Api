from flask import Flask
from datetime import timedelta
from flask_restful import Resource, Api
from flask_jwt import JWT
from security import authenticate, identity
from user import UserRegister
from item import Item, ItemList

app = Flask(__name__)
api = Api(app)
app.secret_key = "helloworld123"


app.config['JWT_AUTH_URL_RULE'] = '/login'
app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=1800)
jwt = JWT(app, authenticate, identity)


# map to localhost:5000/item/:name
api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(UserRegister, "/register")

if __name__ == "__main__":  # when we do python app.py, this will be true
    app.run(port=5000, debug=True)
