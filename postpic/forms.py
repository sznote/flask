from flask_wtf import Form
from wtforms import StringField, TextField, PasswordField
from wtforms.validators import DataRequired, Length, Email

class  ImageForm(Form):
	image = StringField('Image', validators=[DataRequired(), Length(min=2,max=100)])
	# email = TextField(
 #                'Email',
 #                validators=[DataRequired(),Email(message=None), Length(min=6, max=40)]
 #        )


