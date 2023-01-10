
from chalice import BadRequestError

class ApiException(BadRequestError):
    def __init__(self, message: str, errors: list):
        super().__init__(message)
