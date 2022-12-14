# Python Imports

#Custom Imports
import logging
import os
from threading import Thread

from services.ApiException import ApiException
from services.UserService import UserService
from services.ApiThread import ApiThread
from chalice import BadRequestError
from chalice import ChaliceUnhandledError
import logging

class UserResource(object):
    def __init__(self):
        self.logger = logging.getLogger("chalice-demo")
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

        # num = 2/ 0
        #
        # print("num:{}".format(num))

        if 0==0:
            # raise ApiException("Something went wrong")
            # raise Exception("Something went wrong")
            # raise ChaliceUnhandledError("0==0")
            raise BadRequestError("Something went wrong")

        return {'name':'John'}

