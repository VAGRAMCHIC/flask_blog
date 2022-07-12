from flask_app import create_app

from flask_script import Manager, Command


app = create_app()

if __name__ == '__main__':
    manager = Manager(app)
    manager.add_command('db', Command)
    manager.run()