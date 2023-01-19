import json

class ClassEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj,'__dict__'):
            return obj.__dict__
        return super().default(obj)