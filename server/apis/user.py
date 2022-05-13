from flask_restx import Api, Resource

class User(Resource):
    def get(self, account=None):
        if not account:
            return
        return 

    def post(self):
        return

    def put(self, id):
        return
    
    def delete(self, id):
        return
