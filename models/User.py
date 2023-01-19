
from models.address import Address

class User(object):
    first_name: str
    last_name: str
    address: Address

    def __init__(self):
        pass

    def to_dict(self):
        return vars(self)