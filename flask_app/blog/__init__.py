

from flask.blueprints import Blueprint

blog_bp = Blueprint('blog', __name__, static_folder='static', template_folder='templates')


from .routes import *
