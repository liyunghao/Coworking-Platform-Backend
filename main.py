from server import *

app = create()
api = Api(app, doc='/api/doc')

api.add_resource(Bulletin, '/bulletin', '/bulletin/<string:id>')

if __name__ == '__main__':
    app.run()
