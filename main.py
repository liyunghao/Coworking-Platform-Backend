from server import *

app = create()
api = Api(app, doc='/api/doc')

api.add_resource(BulletinAPI, '/bulletin', '/bulletin/<string:id>')
api.add_resource(UserAPI, '/users', '/users/<string:id>')
api.add_resource(LoginAPI, '/login')

if __name__ == '__main__':
    app.run()
