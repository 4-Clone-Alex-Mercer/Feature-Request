from app import db
from app.models import FeatureRequest, ProductArea, Client


def getRequests():
    requests = FeatureRequest.query.all()
    requestsList = []
    for request in requests:
        requestsList.append(request.serialize)
    return requestsList
 

def getClientName(name):
    return Client.query.filter(Client.name == name).first().id
    

def getAreaName(name):
    return ProductArea.query.filter(ProductArea.name == name).first().id


def addFeatueRequest(req):
    clientId = str(getClientName(req['client']))
    areaId = str(getAreaName(req['product_area']))
    featureRequest = FeatureRequest(title=req['title'], description=req['description'],
                             target_date=req['target_date'], client_priority=req['client_priority'], client_id=clientId, product_area_id=areaId)
    db.session.add(featureRequest)
    db.session.commit()
    return req