import sqlite3
from sql_client import SqlClient
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required


class Item(Resource):
    client = SqlClient("data.db")
    parser = reqparse.RequestParser()  # create new parser for parse the req
    parser.add_argument("price",  # validation req.body
                        type=float,
                        required=True,
                        help="This field is required")

    @classmethod
    def _get_item_by_name(cls, name):
        query = "SELECT * FROM items WHERE NAME=?"
        result = cls.client.run(query, (name, ))
        if len(result) > 0:
            row = result[0]
            return {"item": {"name": row[0], "price": row[1]}}
        return None

    def get(self, name):
        item = self._get_item_by_name(name)

        if item:
            return item, 200
        return {"message": "Item not found"}, 404

    @jwt_required()
    def post(self, name):
        if Item._get_item_by_name(name):
            return {"error": "Item exist"}, 400

        data = Item.parser.parse_args()  # get the formatted req.body
        item = {"name": name, "price": data["price"]}

        query = "INSERT INTO items VALUES(?, ?)"
        Item.client.run(query, (item["name"], item["price"]))

        return item, 201  # don't need to jsonify

    @jwt_required()
    def delete(self, name):
        if not Item._get_item_by_name(name):
            return {"error": "name not found"}, 400

        query = "DELETE FROM items WHERE name=?"

        Item.client.run(query, (name, ))

        return {"message": "Item deleted"}, 201

    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()
        price = data["price"]
        print("price:: ", price)
        if not Item._get_item_by_name(name):
            return {"error": "name not found"}, 400

        query = "UPDATE items SET price=? WHERE name=?"
        Item.client.run(query, (price, name))

        return {"item": {
            "name": name,
            "price": price
        }}, 201


class ItemList(Resource):
    client = SqlClient("data.db")

    def get(self):
        query = "SELECT * from items"
        _items = ItemList.client.run(query, None)
        items = [{"name": item[0], "price": item[1]} for item in _items]
        return {"items": items}, 200
