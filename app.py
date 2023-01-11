from chalice import Chalice, Response
import logging
import sys
from chalice import ChaliceUnhandledError
from resources.UserResource import UserResource
from chalice import BadRequestError
from blueprints.user_blueprint import blueprint as user_blueprint

from services.ApiException import ApiException

app = Chalice(app_name='chalice-demo', configure_logs=True, debug=True)
# Set logging format
formatter = logging.Formatter('%(asctime)s %(processName)s %(threadName)s %(filename)s %(funcName)s %(lineno)d %(levelname)-8s %(message)s')
app.log.handlers[0].setFormatter(formatter)
app.register_blueprint(blueprint=user_blueprint, url_prefix="/users")
# @app.middleware('all')
# def my_middleware(event, get_response):
#     app.log.info("Before calling my main Lambda function.")
#     response = get_response(event)
#     app.log.info("After calling my main Lambda function.")
#     return response

@app.middleware('http')
def middleware(event, get_response):
    app.log.info("Start middleware!")
    response = get_response(event)

    if response.status_code == 500:
        # app.log.error("".format(response.body))
        response.body = {
            'message': 'Something went wrong'
        }
        response.headers = {'Content-Type': 'application/json'}
    elif response.status_code == 400:
        body = response.body
        response.body = {
            'message': body['Message']
        }
        app.log.error("body={}, type={}".format(response.body, type(response.body)))

    app.log.info("End middleware!")
    return response

@app.route('/', methods=['GET'])
def home():
    resp = {'message':'Welcome to Chalice Learning'}
    return Response(body=resp, status_code=200, headers={"Content-Type": "application/json"})

@app.route('/user/status', methods=['GET'])
def get_status():
    app.log.info("get_status")
    resp = UserResource().get_status()
    app.log.info("return Response")
    return Response(body=resp, status_code=200, headers={"Content-Type": "application/json"})

# @app.middleware('all')
# def handle_errors(event, get_response):
#     app.log.info("Before handle_errors.")
#     # print("event={}".format(event))
#     app.log.info("event={}".format(event.method))
#     response = None
#     try:
#         response = get_response(event)
#         app.log.info("no issue")
#     except BadRequestError as e:
#         app.log.info("BadRequestError, error=%s" % str(e))
#         return Response(status_code=400, body=str(e),
#                         headers={'Content-Type': 'text/plain'})
#     except Exception as e:
#         app.log.info("Exception, error=%s" % str(e))
#         return Response(status_code=400, body=str(e),
#                         headers={'Content-Type': 'text/plain'})
#     except ChaliceUnhandledError as e:
#         app.log.info("ChaliceUnhandledError, error=%s" % str(e))
#         return Response(status_code=400, body=str(e),
#                         headers={'Content-Type': 'text/plain'})
#     except ApiException as e:
#         app.log.info("ApiException, error=%s" % str(e))
#         return Response(status_code=400, body=str(e),
#                         headers={'Content-Type': 'text/plain'})
#     except:
#         app.log.info("Something went wrong")
#     #else block lets you execute code when there is no error.
#     else:
#         app.log.info("Nothing went wrong")
#     app.log.info("response.status_code={}".format(response.status_code))
#
#     app.log.info("response.body={}".format(response.body))
#     app.log.info("response.headers={}".format(response.headers))
#     app.log.info("After handle_errors.")
#     return response

# @app.middleware('all')
# def handle_errors(event, get_response):
#     app.log.info("Before handle_errors.")
#     # print("event={}".format(event))
#     response = get_response(event)
#
#     app.log.info("response.headers={}".format(response.headers))
#     app.log.info("response.body={}, end of body".format(response.body))
#     app.log.info("response.status_code={}".format(response.status_code))
#
#     body = response.body
#
#     if response.status_code == 500:
#         response.body = {
#             'message' : 'Something went wrong',
#             'error': body
#         }
#     elif response.status_code == 400:
#         response.body = {
#             'message': body['Message']
#         }
#
#     response.headers = {'Content-Type': 'application/json'}
#
#     app.log.info("After handle_errors.")
#
#     return response

# @app.route('/user/name', methods=['GET'])
# def get_name():
#     app.log.info("get_name")
#     resp = UserResource(app).get_name()
#     app.log.info("return Response")
#     return Response(body=resp, status_code=200, headers={"Content-Type": "application/json"})




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
