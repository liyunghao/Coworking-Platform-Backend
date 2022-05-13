from flask_restx import Api, Resource


class Bulletin(Resource):

    def get(self, id=None):

        if not id:
            return ("", 500)
        return ("", 500)

    def post(self):
        return ("", 500)

    def put(self, id):
        return ("", 500)

    def delete(self, id):
        return ("", 500)
