### 1. Folder VS Packages

In python, to make a folder to a package, we need to add a file called `__init__.py`. Then Python will look inside and search for files.

### 2. Resources

Resources in python normally refers to things that the API can response with, and the things that the Api Client can ask for.
In general any class that directly work with the API is a resource.

In this project, `User` class is not a resource because it doesn't directly provide data to the API Client, it more like a helper class which is a model.

### 3. Models

A model is a internal representation of an entity where as a resource is an external representation of an entity. A model is essentially a helper.
