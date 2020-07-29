import pytest
from user import User

def test_user_validate_type_data():
    user = User("Germain", "Bueno","gbueno@gmail.com")
    assert type(user.first_name) == str
    assert type(user.last_name) == str

def test_user_full_name():
    user = User("Germain", "Bueno","gbueno@gmail.com")
    assert user.full_name() == 'Germain Bueno'

def test_user_fail_full_name():
    user = User("Fabian", "Novales","fnovales@gmail.com")
    assert not user.full_name() == 'Germain Bueno'