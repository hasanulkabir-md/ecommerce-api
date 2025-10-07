from flask_jwt_extended import decode_token


def auth_headers(client):
client.post("/api/v1/auth/register", json={"email":"a@a.com","password":"pw","name":"A"})
r = client.post("/api/v1/auth/login", json={"email":"a@a.com","password":"pw"})
access = r.get_json()["access"]
return {"Authorization": f"Bearer {access}"}


def test_cart_and_checkout_flow(client):
# seed a product
client.post("/api/v1/auth/register", json={"email":"admin@x.com","password":"pw","name":"Admin"})
# directly insert via endpoint disabled in tests; instead rely on db in memory or create admin bypass in app if needed.
# For brevity: use products table via direct SQL
from app.extensions import db
from app.models import Product
with client.application.app_context():
db.session.add(Product(title="Item", description="d", price=10.0, stock=5))
db.session.commit()


h = auth_headers(client)
# list, add to cart, view cart
pid = client.get("/api/v1/products").get_json()["items"][0]["id"]
assert client.post("/api/v1/cart", json={"product_id": pid, "qty": 2}, headers=h).status_code == 201
cart = client.get("/api/v1/cart", headers=h).get_json()
assert cart["total"] == 20.0
# checkout
r = client.post("/api/v1/checkout", headers=h)
assert r.status_code == 201
order = r.get_json()
assert order["total"] == 20.0