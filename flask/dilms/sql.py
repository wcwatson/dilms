"""This module defines a few handy functions that sanitize and execute query
input, effectively sequestering all of DILMS's SQL functionality away from its
Flask functionality.
"""

import psycopg2


def _inspect_query(query):
    """Inspects a query submitted by the user; returns either the query
    stripped of comments (if the query is allowed) or a dummy query that
    produces one of a few preset warning messages (if the query violates any of
    the safety checks).

    Args:
        query (str): a query entered by the user

    Returns:
        str: either a stripped-down version of the user's query or a dummy query
            that returns a warning message, as appropriate

    Examples:
        TODO: illustrative examples
    """

    # TODO: all of it

    return query


def _execute_query(query, conn):
    """Executes a query validated by the safety checks and returns the results.

    Args:
        query (str): a validated query
        conn (psycopg2.connection): a connection to the dilms database

    Returns:
        list: either the results of the user's query or a single row indicating
            a syntax error if the query failed to execute

    Examples:
        TODO: illustrative examples
    """

    # Attempt to execute the query; if successful return the result, otherwise
    # return a syntax warning
    with conn.cursor() as cur:
        try:
            cur.execute(query)
            result = cur.fetchall()
        except psycopg2.ProgrammingError:
            error_msg = ('SQLError: either your query has a syntax error or it'
                ' failed to return any results')
            result = [error_msg]
    return result


def inspect_and_execute(query, conn):
    """Inspects and, if permitted, executes a query submitted by a user on
     database.html, returns either the results or a warning as appropriate.

    Args:
        query (str): a query entered by the user
        conn (psycopg2.connection): a connection to the dilms database

    Returns:
        list: either the results of the user's query, a single row indicating a
            syntax error (if the query passed the safety checks but failed to
            execute), or a single row containing a warning message (if the
            query failed to pass the safety checks)

    Examples:
        TODO: illustrative examples
    """

    safe_query = _inspect_query(query)
    result = _execute_query(safe_query, conn)
    return result
