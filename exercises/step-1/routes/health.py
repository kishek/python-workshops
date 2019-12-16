from flask import Blueprint
from random import randint

# The health API exposes endpoints for understanding the status
# of the web application - i.e. if it is running as expected.
health_api = Blueprint('health', __name__)

# /healthcheck: a simple HTTP-request/response based check.
@health_api.route("/healthcheck")
def healthcheck():
    # TODO: return a response with 'ok'
    return ''

# /deepcheck: a more involved check which hits internal and
# external dependencies of the web application. E.g. database,
# web APIs, downstream microservices.
@health_api.route("/deepcheck")
def deepcheck():
    # TODO: return an 'ok' response half the time (http_status of 200)
    # and a response which is 'not ok' half the time (http_status of 500).
    return ''
