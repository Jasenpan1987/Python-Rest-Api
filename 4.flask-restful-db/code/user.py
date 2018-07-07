import sqlite3
from sql_client import SqlClient
from flask_restful import Resource, reqparse


class User():
    client = SqlClient("data.db")

    def __init__(self, _id, username, password):
        self.id = _id  # id is a reserved keyword
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        query = "SELECT * FROM users WHERE username=?"
        result = User.client.run(query, (username, ))

        if len(result) > 0:
            row = result[0]  # get the first row
            user = cls(*row)  # == cls(row[0], row[1], row[2])
        else:
            user = None
        return user

    @classmethod
    def find_by_id(cls, _id):
        query = "SELECT * FROM users WHERE id=?"
        result = User.client.run(query, (_id, ))

        if len(result) > 0:
            row = result[0]  # get the first row
            user = cls(*row)  # == cls(row[0], row[1], row[2])
        else:
            user = None
        return user


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("username",
                        type=str,
                        required=True,
                        help="Username is required")
    parser.add_argument("password",
                        type=str,
                        required=True,
                        help="Password is required")

    def post(self):
        data = UserRegister.parser.parse_args()

        if User.find_by_username(data["username"]):  # check user name
            return {"message": "Username already exist"}, 400

        query = "INSERT INTO USERS VALUES (NULL, ?, ?)"
        User.client.run(query, (data["username"], data["password"]))

        return {"message": "User created"}, 201
