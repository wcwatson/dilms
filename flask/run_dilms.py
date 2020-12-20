# run_dilms.py

"""
Runs the DILMS Flask app.
"""

from dilms import app

"""
NOTE: Only one app.run() line should be uncommented at any time. If you are running DILMS locally as part of active
development efforts, uncomment the line with debug=True to enable that functionality. NEVER push new code to AWS
with debug=True active.
"""

# For interactive development
app.run(debug=True)

# For production
#app.run()