# dilms/routes.py

"""
This module enacts a high-level manager for the interactive functionality of DILMS. It renders pages and passes
requests to the postgresql database through the appropriate functions in sql.py.

--------

The pages have the following functions.

/home --- DILMS homepage
"""

# Imports

# Flask functionality
from flask import render_template, request
from dilms import app
# from dilms.sql import TODO: add functions

# SQL functionality
import dilms.sql as sql

# TODO: other imports

#Auxiliary functions

# TK


#App functionality

@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
    """Renders the DILMS home page."""
    return render_template('home.html')