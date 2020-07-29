from injector import Binder

from use_cases.i_login_use_case import ILoginUseCase

from use_cases.login_use_case import LoginUseCase

def configure_user_case_binding(binder: Binder) -> Binder:
    binder.bind(ILoginUseCase, LoginUseCase)
    return binder