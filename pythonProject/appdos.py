from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []


class Item(Resource):
    def get(self, name):
        item= next(filter(lambda x: x['name'] == name, items), None)
        # for item in items:
        #     if item['name'] == name:
        #         return item
        return {'item': item}, 200 if item else 404

    def post(self, name):
        # item = {'name': name, 'price': 12.00}
        # items.append(item)
        if next(filter(lambda x: x['name'] == name, items), None):
            return {'message': "Un item con nombre '{}' ya existe.".f(name)}, 400

        data = request.get_json()
        item = {'name': name, 'price': data['price']}
        items.append(item)
        return item, 201


class ItemList(Resource):
    def get(self):
        return {'items': items}


api.add_resource(ItemList, "/items")
api.add_resource(Item, "/item/<string:name>")

app.run(port=8080, debug=True)
