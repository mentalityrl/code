# importing from the current package (or current folder)
from enum import unique
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

# a db.Model is a layout or a blueprint for a object that will stored in your database
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

# This object defines all the column that will be in this table etc. (Id, password, email)
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')