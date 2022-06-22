from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_fontawesome import FontAwesome
from flask_migrate import Migrate

from admin import admin

app = Flask(__name__)

app.register_blueprint(admin, url_prefix='/admin')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
bootstrap = Bootstrap(app)
fonts = FontAwesome(app)

db_session = db.session

app.run(debug=True)