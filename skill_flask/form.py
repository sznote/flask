from flask_wtf import Form
from wtforms import StringField, TextField, PasswordField
from wtforms.validators import Email,  DataRequired, Length, EqualTo, DataRequired


class registerForm(Form):
    fullname = StringField("Full name", validators=
        [DataRequired("Full name"), 
        Length(min=3, max=30) 
        ])
    email  = TextField(
        'Email Address',
        validators=[DataRequired(), Email(message=None)])
    username = StringField("Username",
        validators=[DataRequired(), Length(min=4,max=25)])
    password = PasswordField("New Password", 
        validators=[DataRequired(), Length(min=4,max=25) ])
    confirm  = PasswordField('Repeat Password',
        validators=[EqualTo('password',  message="Password Not match!!")])


class  SetupForm(Form):
          
    blogname  = StringField('Blog Name', validators=
        [DataRequired(), Length(max=80)]
        )
    fullname = StringField("Full name", validators=
        [DataRequired("Full name"), 
        Length(min=3, max=30) ]
        )
    email  = TextField(
        'Email Address',
        validators=[DataRequired(), Email(message=None)]
        )
    username = StringField("Username",
        validators=[DataRequired(), Length(min=4,max=25)]
        )
    password = PasswordField("New Password", 
        validators=[DataRequired(), Length(min=4,max=25) ]
        )
    confirm  = PasswordField('Repeat Password',
        validators=[EqualTo('password',  message="Password Not match!!")]
        )


class LoginForm(Form):

    username = StringField("Username",
        validators=[DataRequired(), Length(min=4,max=25)])
    password = PasswordField("Password", 
        validators=[DataRequired(), Length(min=4,max=25) ])

class PostForm(Form):
    title  = StringField("Title",
        validators=[DataRequired(), Length(min=4,max=200)]
        )
    