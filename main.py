from server import *

app = create()
api = Api(app, doc='/api/doc')

api.add_resource(Bulletin, '/bulletin', '/bulletin/<string:id>')
api.add_resource(User, '/users', '/users/<string:id>')
api.add_resource(Login, '/login')

if __name__ == '__main__':
    app.run()
