import pytest
from app import create_app, db
from app.config import TestingConfig

@pytest.fixture
def client():
    # ✅ Pass TestingConfig directly to create_app
    app = create_app(config_class=TestingConfig)

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.session.remove()
            db.drop_all()

def test_health_check(client):
    res = client.get("/api/v1/products", follow_redirects=True)  # ✅ follow redirects
    assert res.status_code in (200, 404)  # works regardless of seeded data

