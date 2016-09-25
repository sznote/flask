import os

class BaseConfig(object):

	DEBUG = False
	SECRET_KEY = '\xab\xd1f{\x91\xcc\xeb\xe9z3{\xef\xc7\xd2\xfd\x93\x82#*\x00&"\x7f\xe8'
	#SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
	SQLALCHEMY_DATABASE_URI = 'mysql://flask:flask@27.254.149.216:3307/flask_intro'
	SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(BaseConfig):
	DEBUG = True

class ProductionConfig(BaseConfig):
	DEBUG = False

class TestConfig(BaseConfig):
	DEBUG = True
	TESTING = True
	WTF_CSRF_ENABLED = False
	SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'

