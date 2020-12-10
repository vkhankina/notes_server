from functools import wraps
from flask import request


def get_user(f):
    @wraps(f)
    def _get_user(*args, **kwargs):
        try:
            header = request.headers.get('Authorization')
            _, token = header.split(' ')
        except:
            return {'error': 'Authorization error'}, 401
        result = f(*args, **kwargs)
        return result

    return _get_user
