from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy import Integer, String, Boolean, ForeignKey
from typing import List

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = "user"

    id = db.mapped_column(db.Integer, primary_key=True)
    email = db.mapped_column(db.String(120), nullable=False)
    username = db.mapped_column(db.String(20), nullable=False)
    favorites = db.relationship('Favorites', backref='user')

    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email
            # do not serialize the password, its a security breach
        }
    
class Planets(db.Model):
    __tablename__ = "planets"

    id = mapped_column(db.Integer, primary_key=True)
    name = mapped_column(db.String(50), nullable=False)
    size = mapped_column(db.Integer)

    def __repr__(self):
        return '<Planet %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "size": self.size
            # do not serialize the password, its a security breach
        }

class People(db.Model):
    __tablename__ = "people"

    id = db.mapped_column(db.Integer, primary_key=True)
    name = db.mapped_column(db.String(50), nullable=False)
    age = db.mapped_column(db.Integer)

    def __repr__(self):
        return '<Person %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age
            # do not serialize the password, its a security breach
        }

class Favorites(db.Model):
    __tablename__ = "favorites"

    id = db.mapped_column(db.Integer, primary_key=True)
    user_id = db.mapped_column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    people_id = db.mapped_column(db.Integer, ForeignKey('people.id'))
    planets_id = db.mapped_column(db.Integer, db.ForeignKey('planets.id'))

    def __repr__(self):
        return '<Fav %r>' % self.id

    def serialize(self):
        return {
            "user": self.user_id,
            "planets": self.planets_id,
            "people": self.people_id,
            # do not serialize the password, its a security breach
        }