from flask import Flask, request
from flask_restful import Resource, Api
from flask_jwt import JWT, jwt_required
from security import authenticate, identity

app = Flask(__name__)
api = Api(app)
app.secret_key = "helloworld123"
# fake db in this section
items = []

# init jwt
# creates an endpot at POST /auth with username and password
jwt = JWT(app, authenticate, identity)


class Item(Resource):
    @classmethod
    def _get_item_by_name(cls, name):
        return next(filter(lambda i: i["name"] == name, items), None)

    def get(self, name):  # map to get method
        # for item in items:
        #     if item["name"] == name:
        #         return item

        # if the next function doesn't find a item, return None
        item = Item._get_item_by_name(name)
        return {"item": item}, 200 if item else 404

    @jwt_required()
    def post(self, name):
        if Item._get_item_by_name(name):
            return {"error": "Item exist"}, 400
        # force=True means you don't need the application/json header
        # data = request.get_json(force=True)
        # data = request.get_json(silence=True)  # will not raise an error
        data = request.get_json()
        item = {"name": name, "price": data["price"]}
        items.append(item)
        return item, 201  # don't need to jsonify

    @jwt_required()
    def delete(self, name):
        if not Item._get_item_by_name(name):
            return {"error": "name not found"}, 400

        global items
        items = list(filter(lambda i: i["name"] != name, items))
        return {"items": items}, 200

    @jwt_required()
    def put(self, name):
        data = request.get_json()
        item = next(filter(lambda x: x["name"] == name, items), None)
        if item == None:
            items.append({"name": name, "price": data["price"]})
        else:
            item.update(data)
        return {"items": items}


class ItemList(Resource):
    def get(self):
        return {"items": items}


# map to localhost:5000/item/:name
api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")

app.run(port=5000, debug=True)
