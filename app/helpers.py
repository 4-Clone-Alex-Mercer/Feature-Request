from app import db
from app.models import FeatureRequest, ProductArea, Client


def validatePostRequest(req):

    if len(req['title']) <= 50:
        if len(req['description']) <= 1500:
            if type(req['target_date']) == str:
                if type(int(req['client_priority'])) == int and req['client_priority'] > 0:
                    if type(int(getClientId(req['client']))) == int:
                        if type(int(getAreaId(req['product_area']))) == int:
                            return True
    return False

def getRequests():
    requests=FeatureRequest.query.all()
    requestsList=[]
    for request in requests:
        requestsList.append(request.serialize)
    return requestsList


def getClients():
    clients=Client.query.all()
    clientList=[]
    for client in clients:
        clientList.append(client.name)
    return clientList


def getAreas():
    areas=ProductArea.query.all()
    areaList=[]
    for area in areas:
        areaList.append(area.name)
    return areaList


def getClientId(name):
    return Client.query.filter(Client.name == name).first().id


def getAreaId(name):
    return ProductArea.query.filter(ProductArea.name == name).first().id


def addFeatueRequest(req):
    clientId=str(getClientId(req['client']))
    areaId=str(getAreaId(req['product_area']))
    featureRequest=FeatureRequest(
        title = req['title'],
        description = req['description'],
        target_date = req['target_date'],
        client_priority = req['client_priority'],
        client_id = clientId,
        product_area_id = areaId)

    db.session.add(featureRequest)
    db.session.commit()
    db.session.refresh(featureRequest)
    requestId=featureRequest.serialize['requestId']
    checkPriority(req['client_priority'], clientId, requestId)
    return req


def checkPriority(priority, clientId, requestId):
    requests=FeatureRequest.query.filter(
        FeatureRequest.client_id == clientId)
    for request in requests:
        if request.serialize['requestId'] != requestId and int(priority) <= request.client_priority:
            request.client_priority += 1
            db.session.commit()


def updateRequest(req):
    request=FeatureRequest.query.filter(
        FeatureRequest.id == req['requestId']).first()

    clientId=getClientId(req['client'])
    areaId=getAreaId(req['product_area'])

    request.title=req['title']
    request.description=req['description']
    request.target_date=req['target_date']
    request.client_priority=req['client_priority']
    request.client_id=clientId
    request.product_area_id=areaId

    db.session.commit()
    checkPriority(req['client_priority'], clientId, req['requestId'])
    return req


def deleteRequest(id):
    request=FeatureRequest.query.filter(FeatureRequest.id == id).first()
    db.session.delete(request)
    db.session.commit()
    return str(request)
