# dilms/__init__.py

"""
Initializes the DILMS Flask app.
"""

from flask import Flask
app = Flask(__name__)
from dilms import views