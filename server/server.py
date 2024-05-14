from flask import Flask, jsonify, request
from flask_cors import CORS
import osm_nominatim_requests
#app instance
app = Flask(__name__)
CORS(app)

@app.route('/api/home', methods=["GET"])
def return_home():
    return jsonify({"message": "API here, yes i do"})

@app.route('/api/second', methods=["GET"])
def return_second():
    return jsonify({"message": "Hey, that worked!"})

@app.route('/api/third', methods=["GET"])
def return_third():
    name = request.args.get('name')
    number = int(request.args.get('number'))
    return jsonify({"name": name, "number": number*2})

@app.route("/api/address/coordinates", methods=["POST"])
def return_coordinates():
    city = request.json.get('city')
    street = request.json.get('street')
    number = request.json.get('housenumber')
    postal_code = request.json.get('postalCode')
    coordinates = osm_nominatim_requests.get_location_by_address(street, number, postal_code, city)
    return jsonify({"lat": coordinates[0], "lon": coordinates[1]})

@app.route("/api/address/nearbynodes", methods=["POST"])
def return_nearby_nodes():
    lat = request.json.get('lat')
    lon = request.json.get('lon')
    nodes = osm_nominatim_requests.get_nearby_nodes(lat, lon)
    return jsonify({"nodes": nodes})

if __name__ == '__main__':
    app.run(debug=True, port=8080) # remove debug=True for production, keep for development


