#!/usr/bin/python3
""" This module contains a class User """

import bcrypt
from flask_sqlalchemy import SQLAlchemy
import app

db = SQLAlchemy()


class User(db.Model):
    """db table model for class user"""
    __tablename__ = "user"
    id = db.Column(db.Integer(), primary_key=True)
    # username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    hashed_password = db.Column(db.String(255), nullable=False)

    def set_password(self, pwd):
        """Generate password for new user"""
        salt = bcrypt.gensalt()
        self.hashed_password = bcrypt.hashpw(pwd.encode("utf-8"), salt)

    def validate_password(self, pwd):
        """Check if pwd is valid"""
        return bcrypt.checkpw(pwd.encode("utf-8"), self.hashed_password)


class Commodity(db.Model):
    """db table model for items for sale"""
    __tablename__ = "commodity"
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500))
    price = db.Column(db.Float, nullable=False)
    image_url = db.Column(db.String(200))
    category = db.Column(db.String(100), nullable=False)


class Orders(db.Model):
    """ db table model for items ordered """
    __tablename__ = "orders"
    id = db.Column(db.Integer(), primary_key=True)
    # link the id to the user id
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id'), nullable=False)
    commodity_id = db.Column(db.Integer(), db.ForeignKey('commodity.id'),
                             nullable=False)
    amount = db.Column(db.Integer(), nullable=False)
    date = db.Column(db.DateTime(), nullable=False)

    # relationship for accessing all orders made by a user
    # lazy loading of user orders only when a user is selected ot loaded
    user = db.relationship('User', backref=db.backref('orders', lazy=True))
    # relationship for accessing all orders for a particular commodity
    commodity = db.relationship(
        'Commodity', backref=db.backref('orders', lazy=True))


if __name__ == "__main__":
    app.run()
