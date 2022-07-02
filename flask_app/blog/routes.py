
from . import blog_bp
from .models import Post, PostSchema
from ..extentions import db

from flask import redirect, jsonify


@blog_bp.route('/')
def index():
    posts = Post.query.all()
    responce = PostSchema(many=True)
    print(responce.dump(posts))
    return jsonify({'posts': responce.dump(posts)})

@blog_bp.route('/post')
def add_post():
    return {'aboba':'acacadcac'}