from flask_sqlalchemy import SQLAlchemy
from injector import inject
from sqlalchemy.exc import IntegrityError

from entities.user.user import User
from repositories.i_user_repository import IUserRepository
#from use_cases.exceptions import InvalidUserException


class UserRepositorySqlAlchemy(IUserRepository):
    @inject
    def __init__(self, db: SQLAlchemy):
        self.db = db

    def add(self, user: User):
        try:
            self.db.session.add(user)
            self.db.session.commit()
        except IntegrityError:
            self.db.session.rollback()
            raise ValueError('error BD ' )#InvalidUserException

    def get_all(self):
        return self.db.session.query(User).all()

    def get_user_by_email(self, email: str):
        user = self.db.session.query(User).filter(User.email == email).first()
        if user:
            return user
        raise InvalidUserException

    def get_user_by_customerId(self, customerId: str):
        user = self.db.session.query(User).filter(User.customerId == customerId).first()

        if user:
            return user
        raise ValueError('error BD ' )#InvalidUserException

    def delete(self, uid: int):
        try:
            self.db.session.query(User).filter(User.id == uid).delete()
            self.db.session.commit()
        except IntegrityError:
            self.db.session.rollback()
            raise ValueError('error BD ' )#InvalidUserException
