import logging

from flask import request
from flask_restplus import Resource
from route.api.restplus import api


log = logging.getLogger(__name__)

ns = api.namespace('modulo/hellowold', description='ejemplo para construcir un enpoint nuevo bajo un grupo de recurso')

@ns.route('/')
class HelloWorld(Resource):
    def get(self):
        """
        Returns str saludo.
        """
        return "HOLA MUNDO"


@ns.route('/test')
class HelloWorld(Resource):
    def get(self):
        """
        Returns str saludo.
        """
        return "HOLA MUNDO 2"

