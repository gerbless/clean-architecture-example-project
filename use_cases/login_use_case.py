from injector import inject 

from repositories.i_user_repository import IUserRepository
from use_cases.exceptions import InvalidUserException, InvalidPasswordException
from use_cases.i_login_use_case import ILoginUseCase

class LoginUseCase(ILoginUseCase):

    @inject
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    def valid_credential(self, email: str, password: str):
        try:
            user = self.user_repository.get_user_by_email(email)
            if user is not None:
                return user
        except InvalidUserException:
            pass
        except InvalidPasswordException:
            pass

        return False
