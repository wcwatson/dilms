"""The DILMS Flask app."""

__version__ = '0.1.1'

from flask import Flask
import os

app = Flask(__name__)
env_config = os.getenv('APP_SETTINGS', 'dilms.config.DevelopmentConfig')
app.config.from_object(env_config)
from dilms import routes
