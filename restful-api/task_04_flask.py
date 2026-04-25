#!/usr/bin/python3
"""
A simple Flask-based API with multiple endpoints,
handling GET and POST requests.
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for users
users = {}


@app.route("/")
def home():
    """Root endpoint."""
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    """Returns a list of all usernames stored in the API."""
    return jsonify(list(users.keys()))


@app.route("/status")
def get_status():
    """Returns the API status."""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """Returns the full object for a given username."""
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Adds a new user to the users dictionary via POST request."""
    data = request.get_json()
    
    # Check if the request is valid JSON
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    # Check if username is provided
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Check if username already exists -> RETURN 409 CONFLICT
    if username in users:
        return jsonify({"error": "User already exists"}), 409

    # Add the user and return confirmation -> 201 CREATED
    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
