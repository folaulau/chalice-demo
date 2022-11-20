from chalice import Chalice, Response
import logging
import sys
from controllers.UserController import UserController

app = Chalice(app_name='chalice-demo', configure_logs=True, debug=True)
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(logging.Formatter("%(asctime)s %(lineno)d %(name)-12s %(levelname)-8s %(message)s"))
app.log.removeHandler(app.log.handlers[0])
app.log.addHandler(handler)
# app.log.basicConfig(
#         level=logging.DEBUG,
#         format="%(asctime)s %(lineno)d %(name)-12s %(levelname)-8s %(message)s",
#         handlers=[
#             logging.StreamHandler(sys.stdout)
#         ]
#     )

@app.route('/', methods=['GET'])
def home():
    resp = {'message':'Welcome to Chalice Learning'}
    return Response(body=resp, status_code=200, headers={"Content-Type": "application/json"})

@app.route('/user/status', methods=['GET'])
def home():
    resp = UserController(app).get_status()
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
