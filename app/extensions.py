from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager   # ✅ add this

db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
bcrypt = Bcrypt()
jwt = JWTManager()   # ✅ add this

# ✅ Always encode identity as a string so PyJWT never complains about "sub must be a string"
@jwt.user_identity_loader
def user_identity_lookup(identity):
    return str(identity)