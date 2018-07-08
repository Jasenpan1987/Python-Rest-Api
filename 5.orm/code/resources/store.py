from flask_restful import Resource
from models.store import StoreModel


class Store(Resource):
    def get(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {"message": "Store not found"}, 404

    def post(self, name):
        store = StoreModel.find_by_name(name)
        if store:
            return {"message": f"Store {name} already exist"}, 400
        store = StoreModel(name)
        try:
            store.save_to_db()
            return store.json(), 201
        except:
            return {"message": "Something went wrong"}, 500

    def delete(self, name):
        store = StoreModel.find_by_name(name)
        if not store:
            return {"message": "Store not exists"}, 404
        store.delete_from_db()


class StoreList(Resource):
    def get(self):
        return {"stores": [store.json() for store in StoreModel.query.all()]}
