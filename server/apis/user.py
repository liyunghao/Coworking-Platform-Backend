from flask_restx import Api, Resource
from flask import request, jsonify, make_response
import jwt
from werkzeug.security import generate_password_hash, check_password_hash
from ..db.model import Users
import datetime

class UserAPI(Resource):
    def get(self, account=None):
        if not account:
            return ("", 500)
        return ("", 500)
    
    # register
    def post(self):
        data = request.get_json()
        exist = Users.query.filter_by(username=data['username']).first()
        if not exist:
            newuser = Users(data['username'], data['password'], data['email'], data['admin'])
            newuser.save()
            return make_response(jsonify({'message': 'Suscessfully registered.'}), 200)
        else:
            return make_response(jsonify({'message': 'User already exists.'}), 202)

    def put(self, id):
        return ("", 500)
    
    def delete(self, id):
        return ("", 500)


class LoginAPI(Resource):
    def post(self):
        data = request.get_json()
        login_user = Users.query.filter_by(username=data['username']).first()
        if login_user:
            if check_password_hash(login_user.password, data['password']):
                token = jwt.encode({
                    'username': login_user.username,
                    'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30),
                    'iat': datetime.datetime.utcnow()},
                    "test")
                return make_response(jsonify({'token': token}), 200)
            else:
                return make_response(jsonify({'message': 'Wrong Credential'}), 401)
        else:   
            return make_response(jsonify({'message': 'User don\'t exists.'}), 202)
