from app import create_app,db
from app.models import FeatureRequest, Client,ProductArea
from datetime import datetime


app = create_app()
app.app_context().push()
with app.app_context():
    db.create_all()
    db.session.add(Client(name='Client A'))
    db.session.add(Client(name='Client B'))
    db.session.add(Client(name='Client C'))
    db.session.add(ProductArea(name='Policies'))
    db.session.add(ProductArea(name='Billings'))
    db.session.add(ProductArea(name='Claims'))
    db.session.add(ProductArea(name='Reports'))
    featureRequest = FeatureRequest(
        title='First Title',
        description='First Description',
        target_date=datetime.strptime('2019/05/24', '%Y/%m/%d'),
        client_priority=1,
        client_id=3,
        product_area_id=2
    )
    db.session.add(featureRequest)
    featureRequest = FeatureRequest(
        title='Second Title',
        description='Second Description',
        target_date=datetime.strptime('2019/05/31', '%Y/%m/%d'),
        client_priority=1,
        client_id=2,
        product_area_id=3

    )
    db.session.add(featureRequest)
    featureRequest = FeatureRequest(
        title='Third Title',
        description='Third Description',
        target_date=datetime.strptime('2019/06/15', '%Y/%m/%d'),
        client_priority=1,
        client_id=1,
        product_area_id=1

    )
    db.session.add(featureRequest)
    db.session.commit()