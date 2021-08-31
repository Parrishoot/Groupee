import sys


class Manager:

    @staticmethod
    def get_db_password():

        # TODO: UPDATE THIS!!!
        password_path = sys.argv[1]

        with open(password_path, 'r') as f:
            password = f.read().strip('\n')

        return password
