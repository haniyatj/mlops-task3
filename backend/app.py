from flask import Flask, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

app.config["MONGO_URI"] = os.getenv("MONGO_URI", "mongodb://localhost:27017/mlops-task3")
mongo = PyMongo(app)

@app.route("/")
def home():
    return jsonify({"message": "Flask API is running!"})

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
