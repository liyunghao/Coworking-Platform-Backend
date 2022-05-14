from flask import request, jsonify
import jwt
from functools import wraps
from .db.Model import User

def token_required(f):
    @wraps(f)
    def dec(*args, **kwargs):
        token = None
        if 'x-access-tokens' in request.headers:
         token = request.headers['x-access-tokens']

      if not token:
         return jsonify({'message': 'a valid token is missing'})

      try:
         data = jwt.decode(token, 'test')
         user = User.query.filter_by(username=data['username']).first()
      except:
         return jsonify({'message': 'token is invalid'})

        return f(user, *args, **kwargs)
   return dec


def genera
