from flask_restx import Api, Resource


class Bulletin(Resource):
    
    def get(self, id=None):
        if not id:
            return {'data': 'Get all bulletins'}
        return {'data': 'Get bulletin'+id }
    
    def post(self):
        return

    def put(self, id):
        return

    def delete(self, id):
        return
