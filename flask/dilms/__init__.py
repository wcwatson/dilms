# dilms/__init__.py

"""
Initializes the DILMS Flask app.
"""

__version__ = '0.1.0'

from flask import Flask
app = Flask(__name__)
from dilms import routes