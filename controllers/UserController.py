# Python Imports

#Custom Imports
import logging
import os
from threading import Thread
from services.UserService import UserService
from services.ApiThread import ApiThread

class UserController(object):
    def __init__(self, app):
        self.logger = logging.getLogger("chalice-demo")
        self.app = app
        self.user_service = UserService()

    def get_status(self):
        self.logger.info("get status")
        thread =  ApiThread(target=self.__calculate,args=({}, {}, None))
        thread.start()
        return_value = thread.join()

        self.logger.info("return_value:{}".format(return_value))
        return {'status':'Folau'}

    def __calculate(self, params, return_value, name):
        # return_value = 5
        self.logger.info("__calculate")
        return 6

    def get_name(self):
        self.logger.info("get name")
        return {'name':self.user_service.get_name()}

