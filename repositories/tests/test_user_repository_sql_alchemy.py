import pytest

from pytest_fixture_db import db_session
from repositories.tests.queries.queries_users import *
from use_cases.exceptions import InvalidUserException

db = db_session

def user(db):
    create_user(db=db)
    users = get_user_all(db=db)
    return users[0].id


def test_user_repository_sqlalchemy_add_should_persist_a_user(db):
    users = create_user(db=db)
    assert len(users) is 1


'''def test_user_repository_sqlalchemy_add_should_raise_and_error_if_email_all_ready_exist(db):
    with pytest.raises(InvalidUserException):
        create_user(db=db)
    users = get_user_all(db=db)
    assert len(users) is 1


def test_user_repository_sqlalchemy_get_user_by_email_should_return_a_user(db):
    user_recover = get_user_by_email(db=db, email='admin@email.com')
    assert type(user_recover) is User
    assert user_recover.email == 'admin@email.com'
    assert user_recover.first_name == 'first_name'


def test_user_repository_sqlalchemy_get_user_by_email_should_raise_error_if_user_do_not_exist(db):
    with pytest.raises(InvalidUserException):
        get_user_by_email(db=db, email="email2@email2.com2")


def test_user_repository_sqlalchemy_delete_users_successfully(db):
    users = get_user_all(db=db)
    delete_user(db=db, uid=users[0].id)
    num_users = get_user_all(db=db)
    assert len(num_users) is 0'''