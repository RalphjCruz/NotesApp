from . import db
# DOT IMPORTS FROM CURRENT PACKAGE, db is defined in init.py
from flask_login import UserMixin
from sqlalchemy.sql import func

#db.Model is inheriting

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) 
    
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    first_name = db.Column(db.String(150), nullable=False)
    notes = db.relationship('Note') # Tells flask and sql, do your magic, add into your notes table that note id. Stores all notes, will be able to access notes that a user owns

# when referencing relationship, has to be actual name,
# for foreign key, use lower case