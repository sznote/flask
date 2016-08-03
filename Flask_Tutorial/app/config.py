import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')

SECRET_KEY = 'Sm9obiBTY2hyb20ga2lja3MgYXNz'
STRIPE_API_KEY = 'SmFjb2IgS2FwbGFuLU1vc3MgaXMgYSBoZXJv'
#SQLALCHEMY_DATABASE_URL= 'sqlite:////tmp/test.db'
SQLALCHEMY_TRACK_MODIFICATIONS = True
DEBUG = True
