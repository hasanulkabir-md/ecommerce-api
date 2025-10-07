# 🛍️ Ecommerce API (Flask + MySQL + JWT)

A **modular, Dockerized E-commerce REST API** built with **Flask**, **SQLAlchemy**, and **JWT Authentication**.
It provides core features like **user registration**, **login**, **product management**, **shopping cart**, and **order checkout**.

---

## 📁 Project Structure

```
ecommere-api/
│
├── app/                      # Main Flask app (models, routes, config, extensions)
│
├── migrations/               # Alembic database migrations
│   ├── versions/
│   ├── env.py
│   ├── script.py.mako
│   └── README
│
├── tests/                    # Pytest test suite
│   ├── conftest.py
│   ├── factories.py
│   ├── test_auth.py
│   ├── test_products.py
│   ├── test_cart_checkout.py
│   └── test_sample.py
│
├── postman/                  # (Optional) Postman collection & environment
│   ├── ecommerce_api.postman_collection.json
│   └── ecommerce_api_environment.json
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── pyproject.toml
├── .env.example
├── .gitignore
├── run.py                    # Entry point
└── README.md
```

---

## 🚀 Features

✅ **Authentication**

* Register and login users securely with bcrypt.
* Issue JWT access tokens.

✅ **Products**

* Create, read, update, delete (CRUD) operations.
* Stock management.

✅ **Cart**

* Add, view, update, and remove items from user cart.

✅ **Orders**

* Checkout and automatically create orders from cart.

✅ **Database**

* MySQL via SQLAlchemy ORM + Alembic migrations.

✅ **Testing**

* Pytest-based unit/integration tests.

✅ **Dockerized**

* Run entire API + database with `docker-compose up`.

---

## ⚙️ Installation (Local)

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/ecommere-api.git
cd ecommere-api
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Copy `.env.example` → `.env` and adjust values:

```env
FLASK_ENV=development
FLASK_APP=run.py
SECRET_KEY=super-secret-key
JWT_SECRET_KEY=super-secret-jwt

# Local MySQL (or Docker)
SQLALCHEMY_DATABASE_URI=mysql+pymysql://root:newpassword@127.0.0.1:3306/ecommerce

PAGINATION_PAGE_SIZE=10
ADMIN_EMAIL=admin@example.com
ADMIN_PASSWORD=Admin@123
```

### 5. Initialize the database

```bash
flask db upgrade
```

### 6. Run the app

```bash
flask run
```

App will start at:
➡️ `http://127.0.0.1:5000`

---

## 🐳 Running with Docker

### 1. Build & run containers

```bash
sudo docker-compose up --build
```

This starts:

* `mysql-ecommerce` (MySQL 8)
* `flask-ecommerce` (Flask API)

App available at `http://127.0.0.1:5000`.

---

## 🧪 Running Tests

Run all tests with:

```bash
pytest -v
```

Or run with coverage:

```bash
pytest --cov=app --disable-warnings
```

---

## 🔑 Authentication Flow

1. **Register**
   `POST /api/v1/auth/register`

   ```json
   {
     "email": "user@example.com",
     "password": "123456"
   }
   ```

2. **Login**
   `POST /api/v1/auth/login`
   Returns JWT token:

   ```json
   {
     "token": "<jwt_access_token>"
   }
   ```

3. **Use Token**
   Include in headers for protected endpoints:

   ```
   Authorization: Bearer <jwt_access_token>
   ```

---

## 🛒 Core API Routes

### 🧍 Auth

| Method | Endpoint                | Description   |
| ------ | ----------------------- | ------------- |
| POST   | `/api/v1/auth/register` | Register user |
| POST   | `/api/v1/auth/login`    | Login user    |

### 🛍 Products

| Method | Endpoint                | Description        |
| ------ | ----------------------- | ------------------ |
| GET    | `/api/v1/products`      | List all products  |
| POST   | `/api/v1/products`      | Add product        |
| GET    | `/api/v1/products/<id>` | Get single product |
| PUT    | `/api/v1/products/<id>` | Update product     |
| DELETE | `/api/v1/products/<id>` | Delete product     |

### 🛒 Cart

| Method | Endpoint                 | Description         |
| ------ | ------------------------ | ------------------- |
| GET    | `/api/v1/cart`           | View user cart      |
| POST   | `/api/v1/cart`           | Add product to cart |
| PUT    | `/api/v1/cart/<item_id>` | Update cart item    |
| DELETE | `/api/v1/cart/<item_id>` | Remove from cart    |

### 📦 Orders

| Method | Endpoint              | Description                       |
| ------ | --------------------- | --------------------------------- |
| POST   | `/api/v1/orders`      | Checkout (create order from cart) |
| GET    | `/api/v1/orders`      | View user orders                  |
| GET    | `/api/v1/orders/<id>` | View specific order               |

---

## 🧰 Postman Collection

You can test the API using Postman.

**Steps:**

1. Import
   [`postman/ecommerce_api.postman_collection.json`](postman/ecommerce_api.postman_collection.json)
2. (Optional) Import environment
   [`postman/ecommerce_api_environment.json`](postman/ecommerce_api_environment.json)
3. Set

   ```
   {{base_url}} = http://127.0.0.1:5000
   ```
4. Run requests in order:

   1. Register → Login
   2. Add Product
   3. Add to Cart
   4. Checkout

---

## 🧱 Database Migrations

To apply migrations:

```bash
flask db upgrade
```

To create new migration:

```bash
flask db migrate -m "add new field"
```

---

## 🧩 Environment Example

`.env.example`

```env
FLASK_ENV=development
SECRET_KEY=super-secret-key
JWT_SECRET_KEY=super-secret-jwt
SQLALCHEMY_DATABASE_URI=mysql+pymysql://root:newpassword@127.0.0.1:3306/ecommerce
PAGINATION_PAGE_SIZE=10
ADMIN_EMAIL=admin@example.com
ADMIN_PASSWORD=Admin@123
```

---

## 🧾 License

This project is open-source under the **MIT License**.
Feel free to use, modify, and distribute with credit.

---

## 👨‍💻 Author

**Md Hasanul Kabir**
📍 Feni · Bangladesh
🐈 Founder, Feni Cat Society · MS CS @ Nanjing Normal University
🔗 [GitHub Profile](https://github.com/hasanulkabir-md)

---

