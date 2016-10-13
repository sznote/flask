from flask_wtf import Form
from wtforms import StringField, TextField, PasswordField, IntegerField, SelectField, SelectMultipleField
from wtforms.validators import DataRequired, Length, Email
from flask_wtf.file import  FileField, FileAllowed
from __init__ import upload_images

class  ImageForm(Form):
    #image = StringField('Image', validators=[DataRequired(), Length(min=2,max=100)])
    image = FileField("image", validators=
                            [FileAllowed(['jpg', 'png', 'gif'], 'Image only')]
                      )
    # email = TextField(
 #                'Email',
 #                validators=[DataRequired(),Email(message=None), Length(min=6, max=40)]
 #        )

class LoginForm(Form):
	username = StringField ("Username", validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])

class ListForm(Form):

	username = StringField ("username", validators=[DataRequired()])
	email = StringField("email", validators=[Email()])
	country_code = IntegerField('country Code', validators=[DataRequired()])
	language = SelectField(u'Programming Language', choices=[('cpp', 'C++'), ('py', 'Python'), ('text', 'Plain Text')])
	available = SelectMultipleField('Available', choices=[('1','1'),('2','2')])


