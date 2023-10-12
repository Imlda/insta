from app import db
from datetime import datetime


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    name = db.Column(db.String(128), nullable=True)
    bio = db.Column(db.String(256), nullable=True)
    profile_pic = db.Column(db.String(256), default="default.jpg", nullable=True)
    join_date = db.Column(db.DateTime, default=datetime.utcnow)
    user_status = db.Column(db.Boolean, default=True)
    email = db.Column(db.String(128), nullable=False, unique=True)
    # followers = db.relationship("Follower", backref="user")
    # followings = db.relationship("Following", backref="user")
    # posts = db.relationship("Post", backref="user")
    # comments = db.relationship("Comment", backref="user")
    # likes = db.relationship("Like", backref="user")

    def __repr__(self):
        return f"user: {self.username}"

class Relationship(db.Models):
    __tablename__ = "relationships"
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Boolean, deafult=True)
    following_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    follower_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    relation_date = db.Column(db.DateTime, default="default.jpg")

class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    caption = db.Column(db.String(256), nullable=False)
    image = db.Column(db.String(256), nullable=False)
    post_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    status = db.Column(db.Boolean, default=True)

class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    commentor_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    text = db.Column(db.Text, nullable=False)
    comment_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    comment_status = db.Column(db.Boolean, default=True)
    hidden = db.Column(db.Boolean, default=False)

class Like(db.Model):
    __tablename__ = "likes"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
    status = db.Column(db.Boolean, default=True)
    like_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
