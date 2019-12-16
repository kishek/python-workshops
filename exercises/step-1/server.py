from flask import Flask
from logging import basicConfig, DEBUG
from routes.setup import setup_api
# from routes.health import health_api

# TODO: setup logger to log to stdout/stderr (by default) and a file.

# Register all route handlers
app = Flask(__name__)
app.register_blueprint(setup_api)
# TODO: register the health API once it is ready!
# app.register_blueprint(health_api)


# If invoked from the command line as `python server.py`
# execute the web application on port 5000.
if __name__ == '__main__':
    app.run(debug=True)
