import json

import jinja2
from flask import Flask, Blueprint
from flask_injector import FlaskInjector
from flask_sqlalchemy import SQLAlchemy
from injector import Binder, singleton
from sqlalchemy import MetaData

from route.api.restplus import api
from environment_config import EnvironmentConfig

from repositories.configuration import configure_repositories_binding
from repositories.sql_alchemy.mapping.user_mapping import user_mapping

from services.configuration import configure_services_binding
from use_cases.configuration import configure_user_case_binding
from route.configuration import configure_api_route, configure_web_route, configure_web_binding


templates_folders = [
    EnvironmentConfig.TEMPLATE_DIR,
]

def configure_database_bindings(binder: Binder) -> Binder:
    application = binder.injector.get(Flask)
    metadata = MetaData()
    try:
        user_mapping(metadata)
    except Exception:
        pass
    db = SQLAlchemy(application)

    metadata.reflect(db.engine)
    metadata.drop_all(db.engine)
    db.session.commit()

    metadata.create_all(db.engine)
    db.session.commit()

    binder.bind(SQLAlchemy, to=db, scope=singleton)
    return binder

modules_list = [
    configure_web_binding,
    configure_repositories_binding,
    configure_services_binding,
    configure_user_case_binding,
    configure_database_bindings
]



def create_app(templates_folders_list=templates_folders, modules=modules_list):
    application = Flask(__name__)
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    configure_api_route(api)
    configure_web_route(application)
 
    application.config['SECRET_KEY'] = EnvironmentConfig.SECRET_KEY
    application.config['TESTING'] = True
    application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    application.config['SWAGGER_UI_DOC_EXPANSION'] = 'list'
    application.config['RESTPLUS_VALIDATE'] = True
    application.config['RESTPLUS_MASK_SWAGGER'] = False
    application.config['ERROR_404_HELP'] = False

    application.config.update(
        SQLALCHEMY_DATABASE_URI=EnvironmentConfig.DATABASE
    )

    custom_loader = jinja2.ChoiceLoader([
        application.jinja_loader,
        jinja2.FileSystemLoader(templates_folders_list)
    ])

    application.register_blueprint(blueprint)
    FlaskInjector(app=application, modules=modules)
    application.jinja_loader = custom_loader

    return application


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=EnvironmentConfig.PORT, debug=EnvironmentConfig.MODE_DEBBUGER)