### 1. Folder VS Packages

In python, to make a folder to a package, we need to add a file called `__init__.py`. Then Python will look inside and search for files.

### 2. Resources

Resources in python normally refers to things that the API can response with, and the things that the Api Client can ask for.
In general any class that directly work with the API is a resource.

In this project, `User` class is not a resource because it doesn't directly provide data to the API Client, it more like a helper class which is a model.

### 3. Models

A model is a internal representation of an entity where as a resource is an external representation of an entity. A model is essentially a helper.

### 4. SQLAlchemy

SqlAlchemy is a orm for python, and flask also got its own SqlAlchemy extension called `flask_sqlalchemy`.

To set it up, we need to do the following things:

1.  `pip install flask_sqlalchemy` to install the package.

2.  Create a `db.py` file at the same level of `app.py`, and add the following to initialize it.

```
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
```

3.  Go to the models, and do the following

```
# Update models
...
from db import db

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
```

```
# configs in app.py

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    ...
```

4.  Data operations

For querying data, we can do something like

```
return cls.query.filter_by(id=_id).first()
```

To save and update data, we can do something like

```
def save_to_db(self):
        db.session.add(self)
        db.session.commit()
```

To delete data, we can do something like

```
def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
```

5.  Create Table automatically

To let sqlAlchemy create the table, we need to add the following code in the app.py

```
@app.before_first_request
def create_tables():
    db.create_all()
```
