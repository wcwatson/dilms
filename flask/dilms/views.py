# dilms/views.py

"""
This module enacts a high-level manager for the interactive functionality of DILMS. It renders pages and passes
requests to the [[somekindofSQL]] database through the appropriate functions in sql.py.

--------

The pages perform the following functions.

/index --- DILMS's homepage
"""

"""
Imports
"""

# Flask functionality
from flask import render_template, request
from dilms import app

# SQL imports
# TODO: Decide on details of SQL functionality

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