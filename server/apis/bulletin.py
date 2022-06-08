from flask_restx import Api, Resource
from flask import request, jsonify, make_response
from ..db.model import Bulletin
from ..auth import token_required, check_roles, get_user
import jwt

class BulletinAPI(Resource):
    # get list of bulletin or single post 
    @token_required
    def get(self, id=None):
        if not id:
            all_post = Bulletin.query.all()
            if all_post:
                payload = [post.as_dict() for i, post in enumerate(all_post)]
                return make_response(jsonify({'payload': payload}), 200)
            return make_response(jsonify({'message': 'No Post exists.'}), 202)
        post = Bulletin.query.filter_by(postId=id).first()
        if post:
            return make_response(jsonify({'payload': post.as_dict()}), 200)
        return make_response(jsonify({'message': 'Post don\'t exists.'}), 404)

    # add post
    @token_required
    def post(self):
        data = request.get_json()
        # do some checking in the future?
        if not (data['title'] and data['tag'] and data['content']):
            return make_response(jsonify({'message': 'Missing field.'}), 202)
        author = get_user()
        new_post = Bulletin(data['title'], data['content'], author, data['tag'])
        new_post.save()
        lastId = Bulletin.query.order_by(Bulletin.postId.desc()).first().postId
        return make_response(jsonify({'message': 'Suscessfully add post.', 'postId': lastId}), 200)

    # modify post
    @token_required
    def put(self, id=None):
        if not id:
            return make_response(jsonify({'message': 'Need to specify which post to delete.'}), 400)
        else:
            post = Bulletin.query.filter_by(postId=id).first()
            data = request.get_json()
            author = get_user()
            if post:
                if not check_roles(post.author):
                    return make_response(jsonify({'message': 'No Permission!'}), 401)
                post.update(data, author)
                return make_response(jsonify({'message': 'Suscessfully updated.'}), 200)
            else:
                return make_response(jsonify({'message': 'Post don\'t exists.'}), 404)
                    

    # delete post
    @token_required
    def delete(self, id=None):
        if not id:
            return make_response(jsonify({'message': 'Need to specify which post to delete.'}), 400)
        post = Bulletin.query.filter_by(postId=id).first()

        if post:
            if not check_roles(post.author):
                return make_response(jsonify({'message': 'No Permission!'}), 401)
            post.remove()
            return make_response(jsonify({'message': 'Successfully deleted'}), 200)
        return make_response(jsonify({'message': 'Post don\'t exists.'}), 404)
