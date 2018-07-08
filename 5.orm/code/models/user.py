import sqlite3
from flask_restful import Resource, reqparse
from db import db


class UserModel(db.Model):
    __tablename__ = 'users'

    # These properties must match the ones in the class constructor
    # and these properties will map to the database
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))

    TABLE_NAME = 'users'

    def __init__(self, username, password):
        self.username = username
        self.password = password
        # you can have other properties here, but they
        # won't get matched to the database

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
