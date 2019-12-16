from flask import Blueprint


# The setup API is a convenience API for checking if
# content is serveable to browser environments.
setup_api = Blueprint('setup', __name__)


# /: returns a simple HTML document composed of the age-old
# computing 'check'.
@setup_api.route("/")
def hello():
    return "Hello, World!"
