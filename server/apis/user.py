from flask_restx import Api, Resource
from flask import request, jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
import jwt
from ..db.model import Users
from ..auth import token_required 

class UserAPI(Resource):
    @token_required
    def get(self, account=None):
        if not account:
            all_user = Users.query.all()
            payload = {i: user.as_dict() for i, user in enumerate(all_user)}
            if all_user:
                return make_response(jsonify({'payload': payload}), 200)
            else:
                return make_response(jsonify({'message': 'No User exists.'}), 202)
                
        user = Users.query.filter_by(username=account).first()
        if user:
            return make_response(jsonify({'payload': user.as_dict()}), 200)
        else:
            return make_response(jsonify({'message': 'User don\'t exists.'}), 202)
            
    
    # register
    def post(self):
        data = request.get_json()
        exist = Users.query.filter_by(username=data['username']).first()
        if not exist:
            newuser = Users(data['username'], data['nickname'], data['password'], data['email'], data['admin'])
            newuser.save()
            return make_response(jsonify({'message': 'Suscessfully registered.'}), 200)
        else:
            return make_response(jsonify({'message': 'User already exists.'}), 202)
    
    @token_required
    def put(self, account=None):
        if not account:
            return make_response(jsonify({'message': 'Need to specify which account.'}), 400)
        permit = self.check_roles(account)
        data = request.get_json()
        user = Users.query.filter_by(username=account).first()
        if not permit:
            return make_response(jsonify({'message': 'No permission !'}), 401)
        if user:
            user.update(data)
            return make_response(jsonify({'message': 'Suscessfully updated.'}), 200)
        else:
            return make_response(jsonify({'message': 'User don\'t exists.'}), 202)

    
    @token_required
    def delete(self, account=None):
        if not account: 
            return make_response(jsonify({'message': 'Need to specify which account.'}), 400)

        permit = self.check_roles(account)
        if not permit:
            return make_response(jsonify({'message': 'No permission !'}), 401)
        user = Users.query.filter_by(username=account).first()
        if user:
            user.remove()
            return make_response(jsonify({'message': 'Suscessfully deleted.'}), 200)
        else:
            return make_response(jsonify({'message': 'User don\'t exists.'}), 202)

    def check_roles(self, target):
        token = request.headers['x-access-tokens']
        data = jwt.decode(token, 'test', algorithms='HS256')
        user = Users.query.filter_by(username=data['username']).first()
        return (target == user.username) or (user.admin == True)
        
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
                    'test',
                    algorithm='HS256'
                    )
                return make_response(jsonify({'token': token}), 200)
            else:
                return make_response(jsonify({'message': 'Wrong Credential'}), 401)
        else:   
            return make_response(jsonify({'message': 'User don\'t exists.'}), 202)
