import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'DiWeb.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "0000"
