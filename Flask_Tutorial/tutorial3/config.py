# default config

class  BaseConfig(object):
	DEBUG = False
	SECRET_KEY = '\xee\x00\xbc\x147\x1c\xcc\xec\r\xe45\x08\xcc\xdc\xda\xfc\x93\xa1V\xd7\x16\xa7\x0e\xf9'
	SQLALCHEMY_TRACK_MODIFICATIONS = True
	SQLALCHEMY_DATABASE_URI = 'sqlite:///posts.db'
	#DATABASE = 'sample.db'

class DevelopmentConfig(BaseConfig):
	DEBUG = True


class ProductionConfig(BaseConfig):
	DEBUG = False

