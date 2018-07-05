from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# fake db in this section
items = []

# this is a resouce defination


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

    def delete(self, name):
        pass

    def put(self, name):
        pass


class ItemList(Resource):
    def get(self):
        return {"items": items}


# map to localhost:5000/item/:name
api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")

app.run(port=5000, debug=True)
