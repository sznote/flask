from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
import os

from project import app, db

app.config.from_object('config.DevelopmentConfig')

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
	manager.run()

# python  manage.py  db init ;; create folder migrations
# 			create  new table on models.py
# python manage.py db migrate ;; create script .py to migrate database, On migrations -> versions -> xxx.py
# python manage.py  db  upgrade
# python manage.py runserver
