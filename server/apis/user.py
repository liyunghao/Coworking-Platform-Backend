from flask_restx import Api, Resource

class User(Resource):
    def get(self, account=None):
        if not account:
            return ("", 500)
        return ("", 500)

    def post(self):
        return ("", 500)

    def put(self, id):
        return ("", 500)
    
    def delete(self, id):
        return ("", 500)


class Login(Resource):
    def post(self):
        return ("", 500)
