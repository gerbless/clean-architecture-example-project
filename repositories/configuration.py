from injector import Binder

from repositories.i_user_repository import IUserRepository

from repositories.sql_alchemy.user_repository_sql_alchemy import UserRepositorySqlAlchemy

def configure_repositories_binding(binder: Binder)-> Binder:
    binder.bind(IUserRepository, UserRepositorySqlAlchemy)
    return Binder