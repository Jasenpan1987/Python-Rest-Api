from werkzeug.security import safe_str_cmp
from user import User

users = [
    User(1, "Jasen", "1234")
]

username_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}


def authenticate(username, password):
    # on dictionary, there is a get method, and compares to the
    # username_mapping[username] method, it can accept a default
    # value once the lookup is failed
    user = username_mapping.get(username, None)
    # string compare in python 2.7 is not safe
    print(user.id, user.username, user.password)
    if user and safe_str_cmp(user.password, password):
        return user


def identity(payload):
    user_id = payload["identity"]
    return userid_mapping.get(user_id, None)
