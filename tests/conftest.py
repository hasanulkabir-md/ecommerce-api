import os
import pytest
from app import create_app
from app.extensions import db
from app.config import TestingConfig

@pytest.fixture
def client():
    # Ensure Flask doesn’t auto-load .env during tests
    os.environ["FLASK_SKIP_DOTENV"] = "1"

    app = create_app(TestingConfig)

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
        try:
            yield client
        finally:
            with app.app_context():
                db.drop_all()
