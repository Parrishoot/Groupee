from flask import Flask
from flask_restful import Api
from app.api.resources.user import UserResouce

APP_NAME = 'GROUPEE'

app = Flask(APP_NAME)
api = Api(app)

api.add_resource(UserResouce, '/user')

if __name__ == '__main__':
    app.run()
