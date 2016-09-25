from flask_wtf import Form
from wtforms import StringField, TextField, PasswordField
from wtforms.validators import DataRequired

#http://wtforms.simplecodes.com/docs/0.6/fields.html
class  LoginFrom(Form):
	username = TextField('username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])

