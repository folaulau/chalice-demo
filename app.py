from chalice import Chalice, Response
import logging
import sys
from controllers.UserController import UserController

app = Chalice(app_name='chalice-demo', configure_logs=True, debug=True)
# Set logging format
formatter = logging.Formatter('%(asctime)s %(processName)s %(threadName)s %(filename)s %(funcName)s %(lineno)d %(levelname)-8s %(message)s')
app.log.handlers[0].setFormatter(formatter)

@app.route('/', methods=['GET'])
def home():
    resp = {'message':'Welcome to Chalice Learning'}
    return Response(body=resp, status_code=200, headers={"Content-Type": "application/json"})

@app.route('/user/status', methods=['GET'])
def home():
    resp = UserController(app).get_status()
    return Response(body=resp, status_code=200, headers={"Content-Type": "application/json"})

@app.route('/user/name', methods=['GET'])
def home():
    resp = UserController(app).get_name()
    return Response(body=resp, status_code=200, headers={"Content-Type": "application/json"})


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
