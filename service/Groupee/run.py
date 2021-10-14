from flask import Flask, render_template
from flask_restful import Api
from app.api.resources.user import UserResource
from backend.database.util import Manager, get_db_connection_string

APP_NAME = 'GROUPEE'

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = get_db_connection_string()
manager = Manager.get_instance()
manager.db.init_app(app)

api.add_resource(UserResource, '/user/<int:id>')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
