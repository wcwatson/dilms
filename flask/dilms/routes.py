"""This module enacts a high-level manager for the interactive functionality of
DILMS. It renders pages and passes user queries to the PostgreSQL database via
the appropriate functions in sql.py.

The pages have the following functions.
/home - DILMS homepage
/database - UI to query to the dilms postgresql database and view the results
"""

# Flask functionality
from flask import render_template, request
from dilms import app

# SQL functionality
import psycopg2
from dilms.sql import inspect_and_execute


# Initialize connection to PostgreSQL database
# TODO: uncomment once ready
#user = 'postgres'
#host = 'localhost'
#dbname = 'dilms'
#conn = None
#conn = psycopg2.connect(database=dbname, user=user)


@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
    """Renders the DILMS home page."""
    return render_template('home.html')


@app.route('/database', methods=['GET', 'POST'])
def database():
    """Renders the database UI and executes user queries."""

    # If the user submitted a query, retrieve and execute it
    result = None
    if request:
        query = request.args.get('query')
        result = inspect_and_execute(query)

    # TODO: making the interactive functionality work

    # Render the page with the results of the user's query
    return render_template('database.html', query=query, result=result)
