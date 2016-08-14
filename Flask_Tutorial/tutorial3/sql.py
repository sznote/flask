import sqlite3
with sqlite3.connect('sample.db') as connection:
	c = connection.cursor()
	# drop table
	c.execute(''' drop table posts''')
	# create table
	c.execute('''create table posts(title TEXT, description TEXT)''')
	c.execute('insert into posts values("Good","I\'m good.")')
	c.execute('insert into posts values("Well","I\'m well.")')

connection.commit
connection.close