import logging

from flask import request, session
from flask_restplus import Resource
from route.api.restplus import api
from injector import inject

from use_cases.i_login_use_case import ILoginUseCase
from use_cases.exceptions import InvalidUserException

log = logging.getLogger(__name__)
ns = api.namespace('login', description='ejemplo conectado')

@ns.route('/')
class Login(Resource):

  @inject 
  def __init__(self, login_use_case: ILoginUseCase, api=api):
    self.login_use_case = login_use_case
    self.api = api
 

  def get(self):
    user = self.login_use_case.valid_credential(email='gerbueno@gmail.com', password='123546')
    print(user.full_name())
    """
    Returns str saludo.
    """
    return user.full_name()