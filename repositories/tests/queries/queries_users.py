from entities.user.user import User
from repositories.sql_alchemy.user_repository_sql_alchemy import UserRepositorySqlAlchemy


def get_user_all(db):
    user_repository = UserRepositorySqlAlchemy(db)
    return user_repository.get_all()


def get_user_by_email(db, email: str):
    user_repository = UserRepositorySqlAlchemy(db)
    return user_repository.get_user_by_email(email=email)


def create_user(db):
    user_repository = UserRepositorySqlAlchemy(db)
    user = User("first_name", "last_name", "admin@email.com")
    user_repository.add(user)
    return get_user_all(db)


def get_subscriptions(db, email: str):
    user_repository = UserRepositorySqlAlchemy(db)
    return user_repository.get_subscriptions(email=email)


def delete_user(db, uid: int):
    user_repository = UserRepositorySqlAlchemy(db)
    user = user_repository.delete(uid=uid)
    return user
