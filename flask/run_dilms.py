# run_dilms.py

"""
Runs the DILMS Flask app.

--------

If you are running DILMS locally as part of active development efforts, run this module to open a local version
of the Flask app.
"""

from dilms import app
app.run(debug=True)