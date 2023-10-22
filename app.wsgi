#! /usr/bin/python3
import sys
import logging
 
sys.path.insert(0, '/var/www/binbash.site')
 
# Set up logging
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
 
# Import and run the Flask app
from app import app as application
application.config['SECRET_KEY'] = 'flask_web_app'
