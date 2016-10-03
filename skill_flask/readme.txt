# 13. 
### many to one
### one to many

>>> bo=Blog.query.filter_by(admin=2, name='saza').first()
>>> us=User.query.filter_by(id=bo.admin).first()
>>> us.id
2
>>> us.email
u'saza_thi@hotmail.com'
>>> us.fullname
u'sahai srichock'
>>> py = Category("Python")
>>> po = Post(bo, us, "python is cool", "This is why", py, 'python-is-cool')
>>> po
<Post 'python is cool'>
>>> db.session.add(po)
>>> db.session.commit()
>>> db.session.add(py)
>>> db.session.commit()
>>> po.author.email
u'saza_thi@hotmail.com'

>>> po.author
<User u'saza'
>>> po.author.email
u'saza_thi@hotmail.com'

>>> for x in py.posts:
...     x.id
...
1
>>>

14..:  python-slugify


14
from wtforms.ext.sqlalchemy import QuerySelectField
