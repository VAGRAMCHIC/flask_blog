from flask_script._compat import text_type
from flask_script import Manager, Command
from . import create_app, app


app = create_app()

if __name__ == '__main__':
    manager = Manager(app)
    manager.add_command('db', Command)
    manager.run()