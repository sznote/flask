#!/bin/bash
#exec . ./init.sh
source /opt/pyflask/bin/activate
export APP_SETTINGS='config.DevelopmentConfig'
export DATABASE_URL='sqlite:///posts.db'