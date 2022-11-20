# Python Imports

#Custom Imports
import logging


class UserController(object):
    def __init__(self, app):
        self.logger = logging.getLogger("chalice-demo")
        self.app = app

    def get_status(self):
        self.logger.info("get status")
        return {'status':'good'}

