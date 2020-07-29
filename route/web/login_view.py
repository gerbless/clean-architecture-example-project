from flask import render_template, request, flash, redirect, url_for, session
from flask.views import MethodView
from injector import inject

from use_cases.i_login_use_case import ILoginUseCase
from use_cases.exceptions import InvalidUserException

class LoginView(MethodView):

    @inject 
    def __init__(self, login_use_case: ILoginUseCase):
        self.login_use_case = login_use_case

    def get(self):
        session.clear()
        return render_template("hello_world.html")