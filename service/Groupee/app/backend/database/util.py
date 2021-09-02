import sys
from flask_sqlalchemy import SQLAlchemy


def get_db_password():

    # TODO: UPDATE THIS!!!
    password_path = sys.argv[1]

    with open(password_path, 'r') as f:
        password = f.read().strip('\n')

    return password


def get_db_host():

    # TODO: Eventually update this from localhost
    return '127.0.0.1:3306'


def get_db_connection_string():
    return f'mysql://Groupee_Admin:{get_db_password()}@{get_db_host()}/models'


class Manager:

    __instance = None

    @staticmethod
    def get_instance():
        """ Static access method. """
        if not Manager.__instance:
            Manager()
        return Manager.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if Manager.__instance:
            raise Exception("This class is a singleton!")
        else:
            self.db = SQLAlchemy()
            Manager.__instance = self

