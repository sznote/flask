from flask_wtf import Form
from wtforms import StringField, TextField, PasswordField, TextAreaField
from wtforms.validators import Email,  DataRequired, Length, EqualTo, DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from models import Category

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



def categories():
    return Category.query.all()

class PostForm(Form):
    title  = StringField("Title",
        validators=[DataRequired(), Length(min=4,max=200)]
        )
    
    body = TextAreaField('Content', validators=[DataRequired()])
    category = QuerySelectField('Category', query_factory=categories, allow_blank=True)
    new_category = StringField('New Category')
    # slug = 
    # publish_date = 
    # live = 