from flask_restx import Api, Resource


class Issue(Resource):
    
    def get(self, id=None):
        if not id:
            return {'data': 'Get all Issue'}
        return {'data': 'Get Issue'+id }
    
    def post(self):
        return

    def put(self, id):
        return

    def delete(self, id):
        return
