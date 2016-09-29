from flask_wtf import Form
from wtforms import StringField, TextField, PasswordField
from wtforms.validators import DataRequired, Length

#http://wtforms.simplecodes.com/docs/0.6/fields.html
class  MessageForm(Form):
	title = TextField('Title', validators=[DataRequired()])
	description = TextField(
		'Description', validators=[DataRequired(), Length(min=6, max=140)])
