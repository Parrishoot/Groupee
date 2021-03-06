import json
from flask_restful import Resource, reqparse
from flask import make_response, render_template, url_for, request
from sqlalchemy.exc import IntegrityError
from backend.database.models.user import User
from backend.database.util import Manager


class UserResource(Resource):
    """RESOURCE FOR THE USERS"""

    # GET
    @staticmethod
    def get(id):

        # Get the user for the specific ID
        # user = User.query.get_or_404(id)
        return {
            'url': url_for('userresource', id='2'),
            'url_2': request.root_url
        }

    # POST
    @staticmethod
    def post():

        manager = Manager.get_instance()
        session = manager.db.session

        # Parse the arguments from the request
        parser = reqparse.RequestParser()

        parser.add_argument('user_name', required=True)
        parser.add_argument('first_name', required=True)
        parser.add_argument('last_name', required=True)

        args = parser.parse_args()

        # TODO: Validate arguments

        # create new User model object containing new values
        new_user = User(id=None,
                        user_name=args.user_name,
                        first_name=args.first_name,
                        last_name=args.last_name)

        try:
            # Add that user to the datbase
            session.add(new_user)
            session.commit()
            session.close()

            # Return a 200 code for success
            return {'data': 'SUCCESS'}, 200

        # TODO: Add more in depth error handling
        except IntegrityError as e:

            return {'data': f'Data Integrity Error:\n{e}'}, 400

        except Exception as e:

            return {'data': f'Internal Server Error\n{e}'}, 500



