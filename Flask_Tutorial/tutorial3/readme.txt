1 Setting up a static site, Hello world
2. create login page

https://www.youtube.com/watch?v=WfpFUmV1d0w&list=PLLjmbh6XPGK4ISY747FUHXEl9lBxre4mM

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
10. Config 