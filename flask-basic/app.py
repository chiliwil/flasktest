from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name': 'My Store',
        'items': [
            {
                'name': 'My item',
                'price': 15.99
            }
        ]
    }
]


# post /store data : {name: }
@app.route('/store', methods=['POST'])
def create_store():
    req = request.get_json()
    new_store = {
        'name': req['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


# get /store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'no found'})


# get / store
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})


# post/store/<string:name>item {name: , price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    req = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': req['name'],
                'price': req['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'not found'})


# get /store/<string:name>/item
@app.route('/store/<string:name>')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'not found'})


@app.route('/')
def home():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
