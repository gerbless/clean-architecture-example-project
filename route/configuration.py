from flask import Flask
from flask_restplus import Api
from injector import Binder

from environment_config import IEnvironmentConfig, EnvironmentConfig
from route.api.endpoints.hello_wold import ns as HelloWorld
from route.api.endpoints.login import ns as Login
from route.web.hello_world_view import HelloWorldView
from route.web.login_view import LoginView



def configure_web_route(app: Flask):
    app.add_url_rule('/', view_func=HelloWorldView.as_view("hello_world"))
    app.add_url_rule('/login1', view_func=LoginView.as_view("login_view"))


def configure_api_route(app:Api):
    app.add_namespace(HelloWorld)
    app.add_namespace(Login)


def configure_web_binding(binder: Binder):
    binder.bind(IEnvironmentConfig, EnvironmentConfig)
    return binder
