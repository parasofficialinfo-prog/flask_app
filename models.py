# models.py
from extensions import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    user_key = db.Column(db.String(200), unique=True)

    # One user → Many posts
    posts = db.relationship("Post", backref="user", lazy=True)


class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)

    # Foreign Key → links each post to a user
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    #hey here we using some test for pulling operatons