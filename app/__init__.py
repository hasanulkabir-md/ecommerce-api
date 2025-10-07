from flask import Flask, jsonify
from .extensions import db, migrate, ma, jwt, bcrypt
from .config import load_config

# Blueprints
from .auth.routes import bp as auth_bp
from .products.routes import bp as products_bp
from .cart.routes import bp as cart_bp
from .orders.routes import bp as orders_bp


def create_app():
    app = Flask(__name__)
    load_config(app)

    # init extensions
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)

    # ✅ Register blueprints with proper prefixes
    app.register_blueprint(auth_bp, url_prefix="/api/v1/auth")
    app.register_blueprint(products_bp, url_prefix="/api/v1/products")
    app.register_blueprint(cart_bp, url_prefix="/api/v1/cart")
    app.register_blueprint(orders_bp, url_prefix="/api/v1/orders")

    # ✅ Root route
    @app.route("/")
    def index():
        return {"message": "✅ Ecommerce API is running!"}

    # ✅ Health check
    @app.route("/api/v1/health")
    def health():
        return jsonify({"status": "ok"}), 200

    return app
