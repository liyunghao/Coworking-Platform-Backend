from flask import request, jsonify
import jwt
from functools import wraps
from .db.model import Users

# define a decorator for requiring token
def token_required(f):
    @wraps(f)
    def dec(*args, **kwargs):
        token = None
        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']

        if not token:
            return jsonify({'message': 'a valid token is missing'})

        data = jwt.decode(token, 'test', algorithms='HS256')
        user = Users.query.filter_by(username=data['username']).first()
        if not user:
            return jsonify({'message': 'token is invalid'})
        return f(*args, **kwargs)
    return dec


