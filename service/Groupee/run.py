from flask import Flask
from flask_restful import Api
from app.api.resources.user import UserResouce
from backend.database.util import Manager, get_db_connection_string

APP_NAME = 'GROUPEE'

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = get_db_connection_string()
manager = Manager.get_instance()
manager.db.init_app(app)

api.add_resource(UserResouce, '/user')

if __name__ == '__main__':
    app.run()
