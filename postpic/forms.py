from flask_wtf import Form
from wtforms import StringField, TextField, PasswordField
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


