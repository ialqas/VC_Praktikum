from flask import Flask, jsonify

#app instance
app = Flask(__name__)

@app.route('/api/home', methods=["GET"])
def return_home():
    return jsonify({"message": "Welcome to the home page"})

if __name__ == '__main__':
    app.run(debug=True) # remove debug=True for production, keep for development


