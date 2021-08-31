from flask_restful import Resource, reqparse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.database.models.user import User
from backend.database.manager import Manager

class UserResouce(Resource):

    # GET
    def get(self):

        pass

    def post(self):

        # TODO: Create a DB Manager with singleton access to the session
        some_engine = create_engine(f'mysql://Groupee_Admin:{Manager.get_db_password()}@127.0.0.1:3306/models')
        Session = sessionmaker(bind=some_engine)
        session = Session()

        parser = reqparse.RequestParser()  # initialize

        parser.add_argument('user_name', required=True)  # add args
        parser.add_argument('first_name', required=True)
        parser.add_argument('last_name', required=True)

        args = parser.parse_args()  # parse arguments to dictionary

        # create new User model object containing new values
        new_user = User(id=None,
                        user_name=args.user_name,
                        first_name=args.first_name,
                        last_name=args.last_name)

        session.add(new_user)
        session.commit()
        session.close()

        return {'data': 'SUCCESS'}, 200

