from flask_wtf import Form
from wtforms import StringField, TextField, PasswordField
from wtforms.validators import DataRequired, Length, EqualTo, Email

#http://wtforms.simplecodes.com/docs/0.6/fields.html
class  LoginFrom(Form):
	username = TextField('username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])

class RegisterForm(Form):
	username  = TextField(
		'username',
		validators=[DataRequired(),Length(min=3,max=25)]
	)
	email = TextField(
		'email',
		validators=[DataRequired(),Email(message=None), Length(min=6, max=40)]
	)
	password = PasswordField(
		'password',
		validators=[DataRequired(),Length(min=6,max=25)]
	)
	confirm = PasswordField(
		'Repeat password',
		validators=[DataRequired(), EqualTo('password', message='Password must match')
		]
	)

