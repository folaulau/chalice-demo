from chalice import Blueprint
from chalice import Response
from resources.UserResource import UserResource
from models.User import User
from models.address import Address
import logging
import json
from utils.ClassEncoder import ClassEncoder
log = logging.getLogger("chalice-demo")

blueprint = Blueprint(__name__)

@blueprint.route('/name', methods=["GET"])
def get_name():
    log.info("get_name")
    # resp = UserResource().get_name()
    log.info("get_name")

    log.info("headers={}".format(blueprint.current_app.current_request.headers))
    log.info("query_params={}".format(blueprint.current_app.current_request.query_params))
    log.info("json_body={}".format(blueprint.current_app.current_request.json_body))

    user = User();
    user.last_name = 'test'
    user.address = Address("test-st")

    # print("lastName:{}".format(user.last_name))
    #
    # user_dumps = json.dumps(user, cls=ClassEncoder)
    #
    # print("user_dumps:{}, type={}".format(user_dumps, type(user_dumps)))
    #
    # user_dict = {'last_names': 'Laulau','first_name':'Folau', 'address': {'street': 'test-st'}}
    #
    # user.__dict__ = user_dict


    encoder = ClassEncoder()
    user_dict = encoder.default(user)
    print("user_dict={}, type={}".format(user_dict, type(user_dict)))

    return Response(body=json.loads(json.dumps(user, cls=ClassEncoder)), status_code=200, headers={"Content-Type": "application/json"})

@blueprint.route('/name', methods=["POST"])
def create():
    log.info("create")
    resp = UserResource().get_status()

    log.info("headers={}".format(blueprint.current_app.current_request.headers))
    log.info("query_params={}".format(blueprint.current_app.current_request.query_params))
    log.info("json_body={}".format(blueprint.current_app.current_request.json_body))

    return Response(body=resp, status_code=200, headers={"Content-Type": "application/json"})