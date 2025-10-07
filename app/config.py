import os

def load_config(app):
    app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "super-secret-key")
    app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY", "super-secret-jwt")
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
        "SQLALCHEMY_DATABASE_URI",
        "mysql+pymysql://root:newpassword@127.0.0.1:3306/ecommerce"
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Pagination
    app.config['PAGINATION_PAGE_SIZE'] = int(os.getenv("PAGINATION_PAGE_SIZE", 10))

    # Admin credentials
    app.config['ADMIN_EMAIL'] = os.getenv("ADMIN_EMAIL", "admin@example.com")
    app.config['ADMIN_PASSWORD'] = os.getenv("ADMIN_PASSWORD", "Admin@123")

    # JWT header setup
    app.config['JWT_TOKEN_LOCATION'] = ['headers']
    app.config['JWT_HEADER_NAME'] = 'Authorization'
    app.config['JWT_HEADER_TYPE'] = 'Bearer'


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///:memory:")
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "test-secret"
