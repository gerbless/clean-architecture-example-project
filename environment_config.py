import os
from abc import ABC

from dotenv import load_dotenv, find_dotenv


class IEnvironmentConfig(ABC):
    pass

class EnvironmentConfig(IEnvironmentConfig):
    load_dotenv(find_dotenv())
    MODE_DEBBUGER = os.environ.get('MODE_DEBBUGER', False)
    PORT = os.environ.get('PORT', 5000)
    TEMPLATE_DIR = os.environ.get('TEMPLATE_DIR', './route/templates')
    SECRET_KEY = os.environ.get('SECRET_KEY', 'M#lOkNdmdAxaGS=GgEPl)&9_$JFNCE&djMPB30zwRwvMDQxFq&tTnv=)')

    DATABASE = os.environ.get('DATABASE')
    BASE_URL = os.environ.get('BASE_URL')