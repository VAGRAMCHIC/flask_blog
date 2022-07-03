from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.inspection import inspect
from ..extentions import db, ma, fields



class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(800), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=False)
    author = db.relationship('Author', backref=db.backref('post', lazy='dynamic'))

    def __init__(self, text, author_id) -> None:
        self.text = text
        self.author_id = author_id

    def __repr__(self):
        return '<Post by %r>' % self.author_id


class Author(db.Model):
    __tablename__ = 'author'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self,name = None) -> None:
        self.name = name

    def __repr__(self):
        return '<User with name %r>' % self.name


class AuthorSchema(ma.Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()


class PostSchema(ma.Schema):    
    id = fields.Int(dump_only=True)
    text = fields.Str()
    author = fields.Nested(AuthorSchema)
