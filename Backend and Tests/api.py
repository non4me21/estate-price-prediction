from flask import Flask, jsonify, request
from flask_cors import CORS
import pickle
import requests


API_KEY = 'AIzaSyBy4sslGQRKnGwItbbJoanyg2QE-sRGQ_U'
base_url = 'https://maps.googleapis.com/maps/api/geocode/json?'
model = pickle.load(open('model.sav', 'rb'))

app = Flask(__name__)
CORS(app)


@app.route('/pricing/')
def index():
    address = request.args.get('address')
    rooms = request.args.get('rooms')
    area = request.args.get('area')
    if address == None or rooms == None or area == None:
        return {'message': 'Missing parameter'}, 400
    params = {
        'key': API_KEY,
        'address': address
    }
    response = requests.get(base_url, params=params).json()
    location = response['results'][0]['geometry']['location']
    lat = location['lat']
    lng = location['lng']
    price = round(model.predict([[lat,lng,rooms,area]])[0],-2)
    print(lat, lng, rooms, area, price)

    return jsonify({'price': price})

app.run(port=8080)