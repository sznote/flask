#!/usr/bin/python
import sys
import logging
logging.basicConfig(Stream=sys.stderr)
sys.path.insert(0,"/var/www/FlaskApp/")

from FlaskApp import app as  application
application.secret_key='Hakxjpa2ha92uipzmjax'