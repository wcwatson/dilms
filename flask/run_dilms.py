"""If you are running DILMS locally as part of active development efforts, you
can run this module to open a local version of the app.
"""

from dilms import app

if __name__ == '__main__':
    app.run(debug=True)
