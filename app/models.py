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


class FeatureRequest(db.Model):

    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    description = Column(String(1500), nullable=False)
    target_date = Column(DateTime, default=datetime.utcnow, nullable=False)
    client_priority = Column(Integer, nullable=False )
  
    def __repr__(self):

            return 'title: %s  description: %s target_date: %s client_priority: %s client_id: %s product_area_id %s' % (self.title, self.description, self.target_date, self.client_priority, self.client_id, self.product_area_id )
