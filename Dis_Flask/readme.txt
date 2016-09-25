https://github.com/realpython/
http://www.youtube.com/playlist?list=PLLjmbh6XPGK4ISY747FUHXEl9lBxre4mM


1. setting up a static site, hello world.
	.
	├── flask-intro
	│   ├── app.py
	│   ├── static
	│   └── templates

	python app.py


2. Create login page
3. User Authentication.
	from functools import wrap
4. Template Inheritance
5. Databases
	posts = [dict(title=row[0],description=row[1]) for row in cur.fetchall()]

	x =  (('a1','a2'),('b1','b2'),('c1','c2'))
	posts=[dict(t=row[0],d=row[1])  for  row in x ]
	[{'d': 'a2', 't': 'a1'}, {'d': 'b2', 't': 'b1'}, {'d': 'c2', 't': 'c1'}]

	for z in posts:
	    print z['d']

	# 
	x={ 'a': 'hello', 'b': 'bello', 'c': 'cello' }
	>>> x.keys()
	['a', 'c', 'b']
    
    >>> x.values()
	['hello', 'cello', 'bello']
	
	>>> for v in x:
	...     print "%s:%s" %( v, x[v])
	...
	a:hello
	c:cello
	b:bello

6. List Comprehensions
	>>g.append( {'k':1,'y':2 } )
	>>g.append( {'k':3,'y':4 } )
	>>> g
	[{'y': 2, 'k': 1}, {'y': 4, 'k': 3}, {'y': 2, 'k': 1}]
	>>> for x in g:
		print x['y']

	post_dict = {}
	posts = []
	for row in cur.fetchall()
		post_dict['tilte'] =  row[0]
		post_ditc['description'] = row[1]
		posts.append(post_dict)

7. Unit Tests
python test.py -v

9. SQLAlchemy
	pip install SQLAlchemy

10. Configuration

11. Secret Key

import os
os.urandom(24)

12. Heroku config
13. Heroku PostgreSQL Setup.
14. local PostgesSQL Setup

** 15. Managing Database Migrations with Flask-Migrate
	pip install Flask-Migrate
	python manage.py db init
	python manage.py db migrate
		-> migrations -> versions -> 4881**_.py
	python manage.py runserver

16. Database Downgrades with FLask-Migrate 
	python manage.py  db --help

17. Virtualenvwrapper
18. Password Hashing
19. blueprint
20. blueprint Redux

<project>__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
import os


app = Flask(__name__)
bcrypt =  Bcrypt(app)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)


from project.users.views import users_blueprint
from project.home.views import home_blueprint

bcrypt = Bcrypt(app)

# register our blueprints
app.register_blueprint(users_blueprint)
app.register_blueprint(home_blueprint)


<flask-intro>
.
├── config.py
├── db_create.py
├── db_create_users.py
├── init.sh
├── manage.py
├── migrations
│   ├── alembic.ini
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions
│       ├── 1bc3202af6f8_.py
│       └── 55f26e7864a0_.py
├── posts.db
├── project
│   ├── __init__.py ****
│   ├── home
│   │   ├── __init__.py
│   │   ├── templates
│   │   │   ├── index.html
│   │   │   └── welcome.html
│   │   └── views.py
│   ├── models.py
│   ├── static
│   │   ├── bootstrap.min.css
│   │   ├── bootstrap.min.js
│   │   ├── css
│   │   │   ├── bootstrap.css
│   │   │   ├── bootstrap.css.map
│   │   │   ├── bootstrap.min.css
│   │   │   ├── bootstrap.min.css.map
│   │   │   ├── bootstrap-theme.css
│   │   │   ├── bootstrap-theme.css.map
│   │   │   ├── bootstrap-theme.min.css
│   │   │   └── bootstrap-theme.min.css.map
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
│   │   ├── _index.html
│   │   ├── _login.html
│   │   ├── _welcome.html
│   │   ├── base.html
│   │   └── login.html
│   └── users
│       ├── __init__.py
│       ├── templates
│       │   └── login.html
│       └── views.py
├── run.py
├── sample.db
├── sql.py
└── test.py

21. User Authentication.
	pip install flask-wtf
	
#http://wtforms.simplecodes.com/docs/0.6/fields.html