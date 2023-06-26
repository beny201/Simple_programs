from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from . import db, ma
from datetime import datetime


class Film(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    # opinion = db.relationship("Opinion", backref='film')
    children = relationship("Opinion")

    def __init__(self, name, date):
        self.name, self.date = name, date


class Opinion(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    opinion = db.Column(db.String(80), nullable=False)
    date = db.Column(db.DateTime, default=datetime.utcnow(), nullable=False)
    film_id = db.Column(db.Integer, ForeignKey('film._id'), nullable=False)

    def __init__(self, opinion, film_id):
        self.opinion = opinion
        self.date = datetime.utcnow()
        self.film_id = film_id
