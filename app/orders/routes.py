from flask import Blueprint, request, jsonify
from app.extensions import db, bcrypt
from app.models import Order, Cart, Product
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime

bp = Blueprint("orders", __name__)

# Example utility: hash password (if you still need it here)
def hash_password(plain):
    return bcrypt.generate_password_hash(plain).decode("utf-8")


@bp.route("/", methods=["POST"])   # Place order
@bp.route("/", methods=["GET"])    # View all orders
#@bp.route("/<int:order_id>", methods=["GET"])  # Get single order
@jwt_required()
def checkout():
    user_id = int(get_jwt_identity())
    cart_items = Cart.query.filter_by(user_id=user_id).all()

    if not cart_items:
        return jsonify({"error": "Cart is empty"}), 400

    total = sum(item.product.price * item.quantity for item in cart_items)

    # Create order
    order = Order(user_id=user_id, total=total, created_at=datetime.utcnow())
    db.session.add(order)
    db.session.flush()  # get order.id before commit

    # Reduce stock and clear cart
    for item in cart_items:
        if item.product.stock > item.quantity:
            return jsonify({"error": f"Not enough stock for {item.product.name}"}), 400
        item.product.stock -= item.quantity
        db.session.delete(item)

    db.session.commit()
    return jsonify({"message": "Order placed successfully", "order_id": order.id}), 201


@bp.route("/", methods=["GET"])
@jwt_required()
def list_orders():
    user_id = get_jwt_identity()
    orders = Order.query.filter_by(user_id=user_id).all()
    return jsonify([
        {
            "id": o.id,
            "total": o.total,
            "created_at": o.created_at.strftime("%Y-%m-%d %H:%M:%S")
        } for o in orders
    ])
