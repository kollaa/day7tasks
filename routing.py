from flask import Flask,jsonify,request

app = Flask(__name__)

stores = [{
    'name' : 'akhil',
    'items' :[
        {
            'name' : 'sai',
            'price' : 15.99
        }
    ]
}]

@app.route('/store', methods=['post'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name' : request_data['name'],
        'items' : []
    }
    stores.append(new_store)
    return jsonify(new_store)

@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})

@app.route('/store/<string:name>')
def get_storename(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message':'store not found'})

@app.route('/store/<string:name>/item', methods=['post'])
def update_items(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item =  {
                'name': request_data['name'],
                'price': request_data['price']
                }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message':'store not found'})

@app.route('/store/<string:name>/item')
def get_items(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message':'store not found'})
    
app.run(port = 5001)