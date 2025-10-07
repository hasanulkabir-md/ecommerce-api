from flask import Blueprint, request, jsonify
from app.extensions import db, bcrypt, jwt
from app.models import User
from flask_jwt_extended import create_access_token

bp = Blueprint("auth", __name__)

# ✅ Register
@bp.route("/register", methods=["POST"])
def register_user():
    data = request.get_json()
    if not data or "email" not in data or "password" not in data:
        return jsonify({"error": "Email and password required"}), 400

    if User.query.filter_by(email=data["email"]).first():
        return jsonify({"error": "User already exists"}), 400

    hashed_pw = bcrypt.generate_password_hash(data["password"]).decode("utf-8")
    user = User(email=data["email"], password=hashed_pw, name=data.get("name", ""))
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201


# ✅ Login
@bp.route("/login", methods=["POST"])
def login_user():
    data = request.get_json()
    user = User.query.filter_by(email=data.get("email")).first()

    if user and bcrypt.check_password_hash(user.password, data.get("password")):
        token = create_access_token(identity=str(user.id))  # 👈 ensure string identity
        return jsonify({"token": token}), 200

    return jsonify({"error": "Invalid credentials"}), 401
