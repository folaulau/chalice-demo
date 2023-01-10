from chalice import Blueprint
from chalice import Response
from resources.UserResource import UserResource
import logging

log = logging.getLogger("chalice-demo")

blueprint = Blueprint(__name__)

@blueprint.route('/name', methods=["GET"])
def get_name():
    log.info("get_status")
    resp = UserResource().get_status()
    log.info("get_status")

    log.info("headers={}".format(blueprint.current_app.current_request.headers))
    log.info("query_params={}".format(blueprint.current_app.current_request.query_params))
    log.info("json_body={}".format(blueprint.current_app.current_request.json_body))

    return Response(body=resp, status_code=200, headers={"Content-Type": "application/json"})

@blueprint.route('/name', methods=["POST"])
def create():
    log.info("create")
    resp = UserResource().get_status()

    log.info("headers={}".format(blueprint.current_app.current_request.headers))
    log.info("query_params={}".format(blueprint.current_app.current_request.query_params))
    log.info("json_body={}".format(blueprint.current_app.current_request.json_body))

    return Response(body=resp, status_code=200, headers={"Content-Type": "application/json"})