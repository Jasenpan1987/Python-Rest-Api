from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# fake db in this section
items = []

# this is a resouce defination


class Item(Resource):
    def get(self, name):  # map to get method
        for item in items:
            if item["name"] == name:
                return item
        return {"item": None}, 404

    def post(self, name):
        item = {"name": name, "price": 12}
        items.append(item)
        return item, 201  # don't need to jsonify


# map to localhost:5000/item/:name
api.add_resource(Item, "/item/<string:name>")

app.run(port=5000)
