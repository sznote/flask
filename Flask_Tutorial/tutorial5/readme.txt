2.  Basic setup
# apache config

 <VirutalHost *:80>
 WSGIScriptAlias / /var/www/FlaskApp/flaskapp.wsgi
 	<Directory /var/www/FlaskApp/FlaskApp/>
 			Order  allow,deny
 			Allow  from all
 	</Directory>
 	Alias /static  /var/www/FlaskApp/FlaskApp/static
 	<Directory /var/www/FlaskApp/FlaskApp/static/>
 			Order  allow,deny
 			Allow  from all
 	</Directory>
 	...
 </VirutalHost>

 3. Bootstrap and jinja Templates
 4. Staring The Homepage
 5. Home page  improvements
 6. Finishing Homepage
 7. Dynamic Dashboard
 8. Content Manamegment
 9. Error  handing
 10. Messages Flashing
 11. User System
 12. Get and Post.
 13. Mysql database
  create table users (uid INT(11) AUTO_INCREMENT PRIMARY KEY, username VARCHAR(20), password VARCHAR(100), email varchar(50), settings varchar(32500), tracking varchar(32500), rank int(3) );

 14. Conneting  to database
  pip install mysql-python

import MySQLdb

def connection():
	conn = MySQLdb.Connection(host="27.254.149.216",
								user = "flask",
								passwd = "flask",
								port = 3307,
								db = "pythonprogramming"
								)
	c = conn.cursor()
	return c, conn

 15. User registration Form.
 	pip install flask-wtf