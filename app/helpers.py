from app import db
from app.models import FeatureRequest, ProductArea, Client


def getRequests():
    requests = FeatureRequest.query.all()
    requestsList = []
    for request in requests:
        requestsList.append(request.serialize)
    return requestsList
 

def getClientId(name):
    return Client.query.filter(Client.name == name).first().id
    

def getAreaId(name):
    return ProductArea.query.filter(ProductArea.name == name).first().id


def addFeatueRequest(req):
    # clientId = str(getClientId(req['client']))
    # areaId = str(getAreaId(req['product_area']))
    # featureRequest = FeatureRequest(title=req['title'], description=req['description'],
    #                          target_date=req['target_date'], client_priority=req['client_priority'], client_id=clientId, product_area_id=areaId)                   
    # checkPriority(req['client_priority'], clientId)                         
    # db.session.add(featureRequest)
    # db.session.commit() 
    return req


def checkPriority(priority, clientId):
    requests = FeatureRequest.query.all()
    for request in requests:
        if int(priority) <= request.client_priority and int(clientId) == request.client_id: 
            request.client_priority += 1
            db.session.commit()


def updateRequest(req):
    request = FeatureRequest.query.filter(FeatureRequest.id == req['requestId']).first()
    
    clientId = getClientId(req['client'])
    areaId = getAreaId(req['product_area'])

    request.title = req['title']
    request.description = req['description']
    request.target_date = req['target_date']                                                      
    request.client_priority = req['client_priority']                            
    request.client_id = clientId
    request.product_area_id = areaId 
    
    
    db.session.commit()

    return req

def deleteRequest(req):
    request = FeatureRequest.query.filter(FeatureRequest.id == req['requestId']).first()
    db.session.delete(request)
    db.session.commit()
    return req