import sqlite3
from flask_restful import Resource, reqparse


class User():
    def __init__(self, _id, username, password):
        self.id = _id  # id is a reserved keyword
        self.username = username
        self.password = password

    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE username=?"
        # the parameter for execute MUST be a tuple
        result = cursor.execute(query, (username, ))
        row = result.fetchone()  # get the first row
        if row:
            user = cls(*row)  # == cls(row[0], row[1], row[2])
        else:
            user = None
        connection.close()
        return user

    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()
        query = "SELECT * FROM users WHERE id=?"
        # the parameter for execute MUST be a tuple
        result = cursor.execute(query, (_id, ))
        row = result.fetchone()  # get the first row
        if row:
            user = cls(*row)  # == cls(row[0], row[1], row[2])
        else:
            user = None
        connection.close()
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

        connection = sqlite3.connect("data.db")
        cursor = connection.cursor()

        query = "INSERT INTO USERS VALUES (NULL, ?, ?)"
        cursor.execute(query, (data["username"], data["password"]))

        connection.commit()
        connection.close()

        return {"message": "User created"}, 201
