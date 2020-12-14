from flask import Blueprint, g
from middlewares.auth import get_user

users_bp = Blueprint('users', __name__)


@users_bp.route('/', methods=['DELETE'])
@get_user
def delete():
    user = g.get('user')
    user.delete()
    return '', 204
