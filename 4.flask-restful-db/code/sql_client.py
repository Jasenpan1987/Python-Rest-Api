import sqlite3
import os


class SqlClient():
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def run(self, query_string, query_params, one=False):
        connection = sqlite3.connect(self.connection_string)
        cursor = connection.cursor()
        if query_params:
            _result = cursor.execute(query_string, query_params)
        else:
            _result = cursor.execute(query_string)
        result = []

        if query_string.find("INSERT") != -1 or query_string.find("UPDATE") != -1 or query_string.find("DELETE") != -1:
            connection.commit()
        else:
            if one:
                result = _result.fetchone()
                print("result:: ", result)
            else:
                result = [row for row in _result]

        connection.close()
        return result
