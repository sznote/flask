1 Setting up a static site, Hello world
2. create login page

https://www.youtube.com/watch?v=WfpFUmV1d0w&list=PLLjmbh6XPGK4ISY747FUHXEl9lBxre4mM
https://github.com/realpython/discover-flask

4. Template Inheritance.
5. Database.

x =  (('a1','a2'),('b1','b2'),('c1',c2))
posts=[dict(t=row[0],d=row[1])  for  row in x ]
[{'d': 'a2', 't': 'a1'}, {'d': 'b2', 't': 'b1'}, {'d': 'c2', 't': 'c1'}]

for z in posts:
    print z['d']

6. List Comprehensions
a=  [{'description': u"I'm good.", 'title': u'Good'}]
for x in a:
...     print x["title"]

7. unit Test.
8. Deploy to Heroku 
9. SqlAlchemy
	pip install Flask-SQLAlchemy
	pip install Flask-SQLAlchemy --upgrade

>>> from app import db
>>> from models import BlogPost
>>> posts = db.session.query(BlogPost).all()
>>> posts
[(Good,I'm good.), (Well,I'm well.), (Test,Shell Test)]

>>> db.session.add(BlogPost("Test2", "Shell2 Test"))
>>> db.session.commit(BlogPost)
>>> db.session.commit()



10. Config 
>>> from app import app
>>> print app.config

11. Secret Key.
>> import os
>> os.urandom(24)

 -- config.py
SECRET_KEY = '\xee\x00\xbc\x147\x1c\xcc\xec\r\xe45\x08\xcc\xdc\xda\xfc\x93\xa1V\xd7\x16\xa7\x0e\xf9'

12. Heroku Configure Settings , How to presql 
13. Heroku 
14. Local ProgreSql Setup.
15. Managing Database Migrations with Flask-Migrate. *** important **
 pip install flask-migrate

16. Database  Downgrades with Flask-Migrate/Alembic  ***important **
python manage.py db --help
python manage.py db downgrade  -1
python manage.py db history

17. virtualenvwrapper
pip freeze  > requirement.txt
mkvirtualenv  discover-flask
pip install -r  requirement.txt
postactivate

18. Password Hashing
pip install flask-bcrypt

python manage.py   db migrate
python manage.py   db upgrade

19. Bludprints.

.
├── __init__.py
└── users
    ├── __init__.py
    ├── templates
    │   └── login.html
    └── views.py
    
20. Blueprints Redux

.
├── __app.py
├── __init__.pyc
├── app.pyc
├── BluePrints.png
├── config.py
├── config.pyc
├── db_create.py
├── db_create_user.py
├── manage.py
├── migrations
│   ├── alembic.ini
│   ├── env.py
│   ├── env.pyc
│   ├── README
│   ├── script.py.mako
│   └── versions
│       ├── 05aec245c565_.py
│       ├── 05aec245c565_.pyc
│       └── 75234f9195a4_.py
├── models.py
├── models.pyc
├── project
│   ├── __init__.py
│   ├── __init__.pyc
│   ├── home
│   │   ├── __init__.py
│   │   ├── __init__.pyc
│   │   ├── templates
│   │   │   ├── index.html
│   │   │   └── welcome.html
│   │   ├── views.py
│   │   └── views.pyc
│   ├── models.py
│   ├── models.pyc
│   ├── posts.db
│   ├── static
│   │   ├── css
│   │   │   ├── bootstrap.css
│   │   │   ├── bootstrap.css.map
│   │   │   ├── bootstrap.min.css
│   │   │   ├── bootstrap.min.css.map
│   │   │   ├── bootstrap-theme.css
│   │   │   ├── bootstrap-theme.css.map
│   │   │   ├── bootstrap-theme.min.css
│   │   │   └── bootstrap-theme.min.css.map
│   │   ├── customs
│   │   │   ├── signin.css
│   │   │   └── starter-template.css
│   │   ├── fonts
│   │   │   ├── glyphicons-halflings-regular.eot
│   │   │   ├── glyphicons-halflings-regular.svg
│   │   │   ├── glyphicons-halflings-regular.ttf
│   │   │   ├── glyphicons-halflings-regular.woff
│   │   │   └── glyphicons-halflings-regular.woff2
│   │   └── js
│   │       ├── bootstrap.js
│   │       ├── bootstrap.min.js
│   │       └── npm.js
│   ├── templates
│   │   ├── base.html
│   │   ├── login.html_
│   │   ├── myhome.html
│   │   └── tem-login.html
│   └── users
│       ├── __init__.py
│       ├── __init__.pyc
│       ├── templates
│       │   └── login.html
│       ├── views.py
│       └── views.pyc
├── readme.txt
├── run.py
├── sql.py
├── test.py
└── views.py


21. UserAuthentication.
pip install flask-wtf

22. Unit Testing with Flask-Testing
pip install flask-testing


23.

24. Testing User Login and Logout.

25. User Registration (functionality and unit tests)

26. Finalize Messaging system

27-30 please see it.




##############
.
├── __app.py
├── __init__.pyc
├── app.pyc
├── BluePrints.png
├── config.py
├── config.pyc
├── db_create.py
├── db_create_user.py
├── manage.py
├── migrations
│   ├── alembic.ini
│   ├── env.py
│   ├── env.pyc
│   ├── README
│   ├── script.py.mako
│   └── versions
│       ├── 05aec245c565_.py
│       ├── 05aec245c565_.pyc
│       └── 75234f9195a4_.py
├── models.py
├── models.pyc
├── project
│   ├── __init__.py
│   ├── __init__.pyc
│   ├── home
│   │   ├── __init__.py
│   │   ├── __init__.pyc
│   │   ├── forms.py
│   │   ├── forms.pyc
│   │   ├── templates
│   │   │   ├── index.html
│   │   │   └── welcome.html
│   │   ├── views.py
│   │   └── views.pyc
│   ├── models.py
│   ├── models.pyc
│   ├── posts.db
│   ├── static
│   │   ├── css
│   │   │   ├── bootstrap.css
│   │   │   ├── bootstrap.css.map
│   │   │   ├── bootstrap.min.css
│   │   │   ├── bootstrap.min.css.map
│   │   │   ├── bootstrap-theme.css
│   │   │   ├── bootstrap-theme.css.map
│   │   │   ├── bootstrap-theme.min.css
│   │   │   └── bootstrap-theme.min.css.map
│   │   ├── customs
│   │   │   ├── signin.css
│   │   │   └── starter-template.css
│   │   ├── fonts
│   │   │   ├── glyphicons-halflings-regular.eot
│   │   │   ├── glyphicons-halflings-regular.svg
│   │   │   ├── glyphicons-halflings-regular.ttf
│   │   │   ├── glyphicons-halflings-regular.woff
│   │   │   └── glyphicons-halflings-regular.woff2
│   │   └── js
│   │       ├── bootstrap.js
│   │       ├── bootstrap.min.js
│   │       └── npm.js
│   ├── templates
│   │   ├── base.html
│   │   ├── login.html_
│   │   ├── myhome.html
│   │   └── tem-login.html
│   ├── test.db
│   └── users
│       ├── __init__.py
│       ├── __init__.pyc
│       ├── forms.py
│       ├── forms.pyc
│       ├── templates
│       │   ├── login.html
│       │   └── register.html
│       ├── views.py
│       └── views.pyc
├── readme.txt
├── requirement.txt
├── run.py
├── sql.py
├── test.py
└── views.py
