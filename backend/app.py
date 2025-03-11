from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend-backend communication

# Configure MongoDB connection
app.config["MONGO_URI"] = "mongodb://mongo:27017/mlops-task3"

mongo = PyMongo(app)

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "status": "Backend is running!",
        "message": "Welcome to the MongoDB API",
        "endpoints": {
            "/add": "POST - Add data to MongoDB"
                            }
    })

@app.route('/add', methods=['POST'])
def add_data():
    data = request.json  # Get JSON data from frontend
    if not data or 'input' not in data:
        return jsonify({"error": "Invalid data"}), 400
    
    mongo.db.inputs.insert_one({"input": data["input"]})  # Insert into MongoDB
    return jsonify({"message": "Data saved successfully!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)