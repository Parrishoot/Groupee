from sqlalchemy import Column, Integer, String
from backend.database.util import Manager


class User(Manager.get_instance().db.Model):

    # Table name
    __tablename__ = 'user'

    # Columns
    id = Column(Integer, primary_key=True)
    user_name = Column(String(45), unique=True, nullable=False)
    first_name = Column(String(45), unique=False, nullable=False)
    last_name = Column(String(45), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.user_name
