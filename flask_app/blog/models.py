from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.inspection import inspect
from ..extentions import db, ma



class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(800), unique=True, nullable=False)
    author = db.Column(db.String(120), unique=True, nullable=False)

    def __init__(self, text = None, author = None) -> None:
        self.text = text
        self.author = author

    def __repr__(self):
        return '<Post by %r>' % self.author


class PostSchema(ma.Schema):
    class Meta:
        model = Post
        fields = ("id", "text", "author")