"""This module defines a few handy functions that execute queries against the
PostgreSQL database, effectively sequestering all of DILMS's SQL functionality
away from its Flask functionality.
"""

import pandas as pd
import psycopg2


def get_db_connection(db_name, user, password):
    conn = psycopg2.connect(
        host='localhost',  # TODO (WW): change if necessary
        database=db_name,
        user=user,
        password=password
    )
    return conn


def execute_query(query, conn):
    """Executes a query submitted by a user on database.html.

    Args:
        query (str): a query entered by the user
        conn (psycopg2.connection): a connection to the dilms database

    Returns:
        list: either the results of the user's query, or a single row indicating
            an error (if the query failed to execute or return results)
    """

    with conn.cursor() as cur:
        try:
            cur.execute(query)
            result = cur.fetchall()
            column_names = [d.name for d in cur.description]
        # If the query cannot be successfully executed or returns no results,
        # return a warning and roll back the connection
        except psycopg2.ProgrammingError:
            error_msg = (
                'Either your query has a syntax error or it failed to return '
                'any results'
            )
            result = [error_msg]
            column_names = ['Error']
            conn.rollback()

    # Converting the query's results to a pandas DataFrame allows for easy
    # handling elsewhere in the app
    result_df = pd.DataFrame(result, columns=column_names)
    return result_df
