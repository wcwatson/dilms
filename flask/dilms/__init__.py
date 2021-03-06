# dilms/__init__.py

"""
Initializes the DILMS Flask app.
"""

__version__ = '0.1.2'

from flask import Flask
app = Flask(__name__)
from dilms import routes