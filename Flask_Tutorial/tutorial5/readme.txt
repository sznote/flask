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
 