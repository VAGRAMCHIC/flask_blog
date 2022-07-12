from flask import Flask
from dotenv import load_dotenv
from pathlib import Path
import os


try:
    env_path = Path(os.getcwd())/'.env'
    if os.path.exists(env_path):
        load_dotenv(dotenv_path = env_path)
except Exception as e:
    exit()


def get_env_variable(env_var_name: str):
    if os.getenv(env_var_name):
        return os.getenv(env_var_name)



from .extentions import *
from .admin import admin_bp
from .blog import blog_bp

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
app = Flask('photozz')

def register_extentons(app):
    db.init_app(app)
    ma.init_app(app)
    migrate.init_app(app, db)
    
def register_blueprints(app):
    app.register_blueprint(blog_bp, url_prefix = '/blog')
    app.register_blueprint(admin_bp, url_prefix = '/admin')

def create_app(): 
    app.config.update(
        SQLALCHEMY_DATABASE_URI=get_env_variable('SQLALCHEMY_DATABASE_URI'),
        DEBUG=get_env_variable('DEBUG'),
        SECRET_KEY=get_env_variable('SECRET_KEY'),
        USERNAME=get_env_variable('USERNAME'),
        PASSWORD=get_env_variable('PASSWORD')
    )
    register_extentons(app)
    register_blueprints(app)
    
    return app
    
if __name__=='__main__':
    app = create_app()
    app.run()



