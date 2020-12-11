from functools import wraps
from flask import request, g
from modules.google_auth import GoogleAuth
from models.users import Users


def get_user(f):
    @wraps(f)
    def _get_user(*args, **kwargs):
        try:
            token = request.headers.get('Authorization')
            p_key = GoogleAuth.verify_token(token)
            user = Users.upsert(p_key)
            g.user = user
        except Exception as err:
            print(err)
            return {'error': 'Authorization error'}, 401
        result = f(*args, **kwargs)
        return result

    return _get_user
