from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_marshmallow.fields import fields
from flask_migrate import Migrate

db = SQLAlchemy()
ma = Marshmallow()
migrate = Migrate()


