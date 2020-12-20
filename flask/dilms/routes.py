# dilms/routes.py

"""
This module enacts a high-level manager for the interactive functionality of DILMS. It renders pages and passes
requests to the postgresql database through the appropriate functions in sql.py.

--------

The pages perform the following functions.

/index --- DILMS homepage
"""

"""
Imports
"""

# Flask functionality
from flask import render_template, request
from dilms import app

# SQL functionality
import dilms.sql as sql

# TODO: other imports

"""
Auxiliary functions
"""

# TK

"""
App functionality
"""

@app.route('/')
@app.route('/index')
def index():
    """Renders the DILMS home page."""
    return render_template('index.html')