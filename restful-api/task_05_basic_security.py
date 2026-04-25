#!/usr/bin/python3
"""
API Security: Basic Auth, JWT, and Role-based Access Control.
"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

# JWT Configuration
app.config["JWT_SECRET_KEY"] = "super-secret-key"  # Real işdə bunu dəyiş!
jwt = JWTManager(app)

# In-memory user data
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

# --- Basic Authentication Logic ---

@auth.verify_password
def verify_password(username, password):
    """Verifies the username and password for Basic Auth."""
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return user
    return None

@auth.error_handler
def auth_error():
    """Returns 401 for Basic Auth errors to satisfy test requirements."""
    return jsonify({"error": "Unauthorized"}), 401

# --- JWT Custom Error Handlers (Mütləq lazımdır!) ---

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

# --- Routes ---

@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """Route protected by Basic Authentication."""
    return "Basic Auth: Access Granted"

@app.route("/login", methods=["POST"])
def login():
    """Login route to obtain a JWT access token."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Missing JSON in request"}), 400

    username = data.get("username")
    password = data.get("password")
    
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        # Store the whole user object or just the username in the identity
        # Here we store username and use it to check roles later
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    
    return jsonify({"error": "Invalid credentials"}), 401

@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """Route protected by JWT Authentication."""
    return "JWT Auth: Access Granted"

@app.route("/admin-only")
@jwt_required()
def admin_only():
    """Route protected by JWT with Role-based Access Control."""
    current_username = get_jwt_identity()
    user = users.get(current_username)
    
    if user and user.get("role") == "admin":
        return "Admin Access: Granted"
    
    # User is authenticated but doesn't have the required role
    return jsonify({"error": "Admin access required"}), 403


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)#!/usr/bin/python3
"""
API Security: Basic Auth, JWT, and Role-based Access Control.
"""
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

# JWT Configuration
app.config["JWT_SECRET_KEY"] = "super-secret-key"  # Real işdə bunu dəyiş!
jwt = JWTManager(app)

# In-memory user data
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}

# --- Basic Authentication Logic ---

@auth.verify_password
def verify_password(username, password):
    """Verifies the username and password for Basic Auth."""
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return user
    return None

@auth.error_handler
def auth_error():
    """Returns 401 for Basic Auth errors to satisfy test requirements."""
    return jsonify({"error": "Unauthorized"}), 401

# --- JWT Custom Error Handlers (Mütləq lazımdır!) ---

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

# --- Routes ---

@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """Route protected by Basic Authentication."""
    return "Basic Auth: Access Granted"

@app.route("/login", methods=["POST"])
def login():
    """Login route to obtain a JWT access token."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Missing JSON in request"}), 400

    username = data.get("username")
    password = data.get("password")
    
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        # Store the whole user object or just the username in the identity
        # Here we store username and use it to check roles later
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)
    
    return jsonify({"error": "Invalid credentials"}), 401

@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """Route protected by JWT Authentication."""
    return "JWT Auth: Access Granted"

@app.route("/admin-only")
@jwt_required()
def admin_only():
    """Route protected by JWT with Role-based Access Control."""
    current_username = get_jwt_identity()
    user = users.get(current_username)
    
    if user and user.get("role") == "admin":
        return "Admin Access: Granted"
    
    # User is authenticated but doesn't have the required role
    return jsonify({"error": "Admin access required"}), 403


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
