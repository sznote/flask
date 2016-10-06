from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flaskext.markdown import Markdown




app = Flask(__name__)

app.config['SECRET_KEY'] = "Hello saza"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOADED_IMAGES_DEST'] = '/mycode/flask/skill_flask/static/images'
app.config['UPLOADED_IMAGES_URL'] = '/static/images'
app.config['DEBUG'] = True


bcrypt  = Bcrypt(app)
db =  SQLAlchemy(app)

# markdown.
md =  Markdown(app, extenstions=['fenced_code', 'table'])


uploaded_images = UploadSet('images', IMAGES)
configure_uploads(app, uploaded_images)

import views



#from models import User
# @app.route('/')
# def home():
#     return "Hello Word!!"

#if __name__ == '__main__':
#	app.run(debug=True)