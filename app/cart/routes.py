from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models import Cart, Product
from flask_jwt_extended import jwt_required, get_jwt_identity

bp = Blueprint("cart", __name__)

# ✅ View cart
@bp.route("/", methods=["GET"])
@jwt_required()
def view_cart():
    user_id = get_jwt_identity()
    cart_items = Cart.query.filter_by(user_id=user_id).all()
    return jsonify([
        {
            "id": item.id,
            "product": item.product.name,
            "quantity": item.quantity,
            "price": item.product.price
        } for item in cart_items
    ])

# ✅ Add to cart
@bp.route("/", methods=["POST"])
@jwt_required()
def add_to_cart():
    user_id = get_jwt_identity()
    data = request.get_json()
    product_id = data.get("product_id")
    quantity = data.get("quantity", 1)

    product = Product.query.get(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    cart_item = Cart.query.filter_by(user_id=user_id, product_id=product_id).first()
    if cart_item:
        cart_item.quantity += quantity
    else:
        cart_item = Cart(user_id=user_id, product_id=product_id, quantity=quantity)
        db.session.add(cart_item)

    db.session.commit()
    return jsonify({"message": "Product added to cart"}), 201

# ✅ Update cart item
@bp.route("/<int:item_id>", methods=["PUT"])
@jwt_required()
def update_cart_item(item_id):
    user_id = get_jwt_identity()
    cart_item = Cart.query.filter_by(id=item_id, user_id=user_id).first()
    if not cart_item:
        return jsonify({"error": "Item not found"}), 404

    data = request.get_json()
    cart_item.quantity = data.get("quantity", cart_item.quantity)
    db.session.commit()
    return jsonify({"message": "Cart item updated"}), 200

# ✅ Remove item
@bp.route("/<int:item_id>", methods=["DELETE"])
@jwt_required()
def remove_cart_item(item_id):
    user_id = get_jwt_identity()
    cart_item = Cart.query.filter_by(id=item_id, user_id=user_id).first()
    if not cart_item:
        return jsonify({"error": "Item not found"}), 404

    db.session.delete(cart_item)
    db.session.commit()
    return jsonify({"message": "Item removed from cart"}), 200
