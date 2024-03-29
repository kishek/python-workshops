from flask import Blueprint
from random import randint

# The health API exposes endpoints for understanding the status
# of the web application - i.e. if it is running as expected.
health_api = Blueprint('health', __name__)

# /healthcheck: a simple HTTP-request/response based check.
@health_api.route("/healthcheck")
def healthcheck():
    return 'ok'

# /deepcheck: a more involved check which hits internal and
# external dependencies of the web application. E.g. database,
# web APIs, downstream microservices.
@health_api.route("/deepcheck")
def deepcheck():
    evaluation = get_evaluation()
    if evaluation == False:
        return 'not ok', 500
    else:
        return 'ok', 200


def get_evaluation():
    num_random = randint(0, 10)
    num_remainder = num_random % 2
    evaluation = (num_remainder == 1)
    return evaluation
