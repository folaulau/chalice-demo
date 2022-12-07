
# Python Imports
import logging

class UserService(object):

    def __init__(self):
        self.logger = logging.getLogger("chalice-demo")

    def get_name(self):
        self.logger.info("get_name")
        return "Folau"