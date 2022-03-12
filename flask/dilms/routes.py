"""This module manages routes and backend logic for DILMS.

The pages have the following functions:
/home | DILMS homepage
/database | UI for querying the dilms postgresql database
/results | displays the results of a user's query
"""

from flask import render_template, request

from dilms import app
from dilms.sql import execute_query, get_db_connection


# Tags to be inserted into every rendered table of results
# NB: this is intended to be inserted right after the "<table" characters that
# begin an HTML table, so it begins with a space to avoid "<tableid=..."
TABLE_INSERT = (
    ' id="results" data-show-export="true" data-pagination="true"'
    ' data-side-pagination="server" data-click-to-select="true"'
    ' data-toolbar="#toolbar" data-show-toggle="true" data-show-columns="true"'
)


# Connection to PostgreSQL database, using credentials stored in the app
# configurations
db_connection = get_db_connection(
    db_name=app.config.get('POSTGRES_DB_NAME'),
    user=app.config.get('POSTGRES_USER'),
    password=app.config.get('POSTGRES_PW')
)


@app.route('/')
@app.route('/home')
@app.route('/index')
def home():
    """Renders the DILMS home page."""
    return render_template('home.html')


@app.route('/database')
def database():
    """Renders the database UI."""
    return render_template('database.html')


@app.route('/result', methods=['GET', 'POST'])
def result():
    """Retrieves and displays the result of a user's query."""
    query = request.form.get('query')
    query_result = execute_query(query=query, conn=db_connection)
    query_result = query_result.to_html(
        index=False,
        na_rep='NULL',
        render_links=True
    )
    query_result = query_result[:6] + TABLE_INSERT + query_result[6:]
    return render_template(
        'result.html',
        query=query,
        query_result=query_result
    )
