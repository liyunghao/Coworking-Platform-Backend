from flask_restx import Api, Resource


class Note(Resource):
    
    def get(self, id=None):
        if not id:
            return {'data': 'Get all Notes'}
        return {'data': 'Get note'+id }
    
    def post(self):
        return

    def put(self, id):
        return

    def delete(self, id):
        return
