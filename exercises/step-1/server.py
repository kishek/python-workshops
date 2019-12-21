from flask import Flask
from logging import basicConfig, DEBUG
from routes.setup import setup_api
from routes.health import health_api

# Setup logger to log to stdout/stderr (by default) and a file.
basicConfig(filename='server.log', level=DEBUG)

# Register all route handlers
app = Flask(__name__)
app.register_blueprint(setup_api)
app.register_blueprint(health_api)


# If invoked from the command line as `python server.py`
# execute the web application on port 5000.
if __name__ == '__main__':
    app.run(debug=True)


# # v1
# print(3+6)

# # v2
# num_one = input()
# num_two = input()
# print(num_one + num_two)

# # v3
# operation = input()
# num_one = input()
# num_two = input()
# if operation == 'plus':
#     print(num_one + num_two)
# elif operation == 'multiply':
#     print(num_one * num_two)
# else:
#     print('Unsupported operation!')

# # v4
# operation = input()
# num_one = input()
# num_two = input()
# if operation == 'plus';
#     print(plus(x, y))
# elif operation == 'multiply':
#     print(multiply(x, y))
# elif 'gradient ascent':
#     sum = plus(x, y)
#     product = multiply(x, y)
#     print(plus(sum, product))
# else:
#     print('Unsupported operation!')


# def multiply(x, y):
#     return x * y
