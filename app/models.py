from app import db
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime


class Client(db.Model):

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

    def __repr__(self):
            return 'name: %s' % (self.name)


class ProductArea(db.Model):

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

    def __repr__(self):
            return 'name: %s' % (self.name)