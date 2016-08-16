# default config

class  BaseConfig(object):
	DEBUG = True
	SECRET_KEY = 'my previous'
	SQLALCHEMY_TRACK_MODIFICATIONS = True
	SQLALCHEMY_DATABASE_URI = 'sqlite:///posts.db'
	#DATABASE = 'sample.db'


