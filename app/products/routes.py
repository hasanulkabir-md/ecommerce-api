from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models import Product

bp = Blueprint("products", __name__)

# ✅ Get all products
@bp.route("/", methods=["GET"])
def get_products():
    products = Product.query.all()
    return jsonify([{"id": p.id, "name": p.name, "price": p.price} for p in products])

# ✅ Add product
@bp.route("/", methods=["POST"])
def add_product():
    data = request.get_json()
    if not data or "name" not in data or "price" not in data:
        return jsonify({"error": "Name and price required"}), 400

    product = Product(name=data["name"], price=float(data["price"]))
    db.session.add(product)
    db.session.commit()
    return jsonify({"message": "Product added", "id": product.id}), 201

# ✅ Get single product
@bp.route("/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    return jsonify({"id": product.id, "name": product.name, "price": product.price})

# ✅ Update product
@bp.route("/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    
    data = request.get_json()
    product.name = data.get("name", product.name)
    product.price = data.get("price", product.price)
    product.stock = data.get("stock", product.stock)
    db.session.commit()
    return jsonify({"message": "Product updated"}), 200

# ✅ Delete product
@bp.route("/<int:product_id>", methods=["DELETE"])
def delete_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "Product deleted"}), 200
