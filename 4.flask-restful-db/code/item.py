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
        print(result)
        if len(result) > 0:
            row = result[0]
            return {"item": {"name": row[0], "price": row[1]}}
        return None

    def get(self, name):
        try:
            item = self._get_item_by_name(name)
        except:
            return {"message": "An Error Occured"}, 500

        if item:
            return item, 200
        return {"message": "Item not found"}, 404

    @jwt_required()
    def post(self, name):
        try:
            if Item._get_item_by_name(name):
                return {"error": "Item exist"}, 400
        except:
            return {"message": "An Error Occured"}, 500

        data = Item.parser.parse_args()  # get the formatted req.body
        item = {"name": name, "price": data["price"]}

        query = "INSERT INTO items VALUES(?, ?)"
        try:
            Item.client.run(query, (item["name"], item["price"]))

            return item, 201
        except:
            return {"message": "An Error Occured"}, 500

    @jwt_required()
    def delete(self, name):
        if not Item._get_item_by_name(name):
            return {"error": "name not found"}, 400

        query = "DELETE FROM items WHERE name=?"
        try:
            Item.client.run(query, (name, ))
        except:
            return {"message": "An Error Occured"}, 500

        return {"message": "Item deleted"}, 201

    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()
        price = data["price"]
        is_item_found = False
        try:
            if Item._get_item_by_name(name):
                is_item_found = True
        except:
            return {"message": "An Error Occured"}, 500

        try:
            if is_item_found:
                query = "UPDATE items SET price=? WHERE name=?"
                Item.client.run(query, (price, name))
            else:
                query = "INSERT INTO items VALUES(?, ?)"
                Item.client.run(query, (name, price))

            return {"item": {
                "name": name,
                "price": price
            }}, 201
        except:
            return {"message": "An Error Occured"}, 500


class ItemList(Resource):
    client = SqlClient("data.db")

    def get(self):
        query = "SELECT * from items"
        _items = ItemList.client.run(query, None)
        items = [{"name": item[0], "price": item[1]} for item in _items]
        return {"items": items}, 200
