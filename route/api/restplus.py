import logging

from flask_restplus import Api
from environment_config import EnvironmentConfig


log = logging.getLogger(__name__)

api = Api(version='1.0', title='Slotting API',
          description='')


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)

    if not EnvironmentConfig.MODE_DEBBUGER:
        return {'message': message}, 500

