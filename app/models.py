from app import db
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime


class Client(db.Model):

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    feature_requests = db.relationship('FeatureRequest', backref='client', lazy=True)

    def __repr__(self):
            return 'name: %s' % (self.name)


class ProductArea(db.Model):

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    feature_requests = db.relationship('FeatureRequest', backref='product_area', lazy=True)

    def __repr__(self):
            return 'name: %s' % (self.name)


class FeatureRequest(db.Model):

    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    description = Column(String(1500), nullable=False)
    target_date = Column(DateTime, default=datetime.utcnow, nullable=False)
    client_priority = Column(Integer, nullable=False )
    client_id = Column(Integer, ForeignKey('client.id'), nullable=False)
    product_area_id = Column(Integer, ForeignKey('product_area.id'), nullable=False)

    @property
    def serialize(self):

        return {
            'title': self.title,
            'description': self.description,
            'target_date': self.target_date,
            'client_priority': self.client_priority,
            'client': self.client.name,
            'product_area': self.product_area.name     
        }

    def __repr__(self):

            return 'title: %s  description: %s target_date: %s client_priority: %s client_id: %s product_area_id %s' % (self.title, self.description, self.target_date, self.client_priority, self.client_id, self.product_area_id )
