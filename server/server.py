from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
import osm_nominatim_requests
import geopy_requests
import base64

#app instance
app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/api/address/coordinates", methods=["POST"])
def return_coordinates():
    street = request.json.get('street')
    number = request.json.get('housenumber')
    postal_code = request.json.get('postalCode')
    coordinates = osm_nominatim_requests.get_location_by_address(street, number, postal_code)
    return jsonify({"lat": coordinates[0], "lon": coordinates[1]})

@app.route("/api/address/nearbynodes", methods=["POST"])
def return_nearby_nodes():
    lat = request.json.get('lat')
    lon = request.json.get('lon')
    nodes = osm_nominatim_requests.get_nearby_nodes(lat, lon)
    return jsonify({"nodes": nodes})

@app.route("/api/address/housewidth", methods=["POST"])
def return_house_width():
    marker_1 = request.json.get('marker1')
    marker_2 = request.json.get('marker2')
    marker1 = (marker_1["lat"], marker_1["lon"])
    marker2 = (marker_2["lat"], marker_2["lon"])
    width = float("%.2f"%geopy_requests.calculate_distance(marker1, marker2))
    return jsonify({"width": width})

@app.route("/api/picture/receive", methods=["POST"])
def receive_picture():
    b64 = request.json.get('picture')
    house_width = request.json.get('houseWidth')
    return jsonify({"message": "Picture received"})

if __name__ == '__main__':
    app.run(debug=True, port=8080) # remove debug=True for production, keep for development


