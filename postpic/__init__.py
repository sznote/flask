from flask import Flask
from flask_uploads import UploadSet, UploadNotAllowed, configure_uploads, IMAGES
from flask_sqlalchemy import SQLAlchemy
import os 

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(__name__)

app.config['SECRET_KEY'] = "Hello saza"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///picname.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOADED_IMAGES_DEST'] =   os.path.join(os.path.abspath(BASE_DIR), "static/images")
app.config['UPLOADED_IMAGES_URL'] = '/static/images/'
app.config['DEBUG'] = True
app.config['SERVER_URL'] = '127.0.0.1:5000'




upload_images = UploadSet('images', IMAGES )
configure_uploads(app, upload_images)


db = SQLAlchemy(app)



import view 