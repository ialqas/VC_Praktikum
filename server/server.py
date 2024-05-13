from flask import Flask, jsonify, request
from flask_cors import CORS
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

if __name__ == '__main__':
    app.run(debug=True, port=8080) # remove debug=True for production, keep for development


