from flask import Flask, request
from flask_restful import Resource, Api, reqparse
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
    parser = reqparse.RequestParser()  # create new parser for parse the req
    parser.add_argument("price",  # validation req.body
                        type=float,
                        required=True,
                        help="This field is required")

    @classmethod
    def _get_item_by_name(cls, name):
        return next(filter(lambda i: i["name"] == name, items), None)

    def get(self, name):  # map to get method

        item = Item._get_item_by_name(name)
        return {"item": item}, 200 if item else 404

    @jwt_required()
    def post(self, name):
        if Item._get_item_by_name(name):
            return {"error": "Item exist"}, 400

        data = Item.parser.parse_args()  # get the formatted req.body
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
        data = Item.parser.parse_args()

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
