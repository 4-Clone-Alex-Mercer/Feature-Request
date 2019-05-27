from app import db
from app.models import FeatureRequest, ProductArea, Client


def validateRequests(req):

    if len(req['title']) <= 50:
        if len(req['description']) <= 1500:
            if type(req['target_date']) == str:
                if type(int(req['client_priority'])) == int and req['client_priority'] > 0:
                    if type(int(req['client'])) == int:
                        if type(int(req['product_area'])) == int:
                            return True
    return False


def getAllRequests():
    requests = FeatureRequest.query.all()
    requestsList = []
    for request in requests:
        requestsList.append(request.serializeModel)
    return requestsList


def getAllClients():
    clients = Client.query.all()
    clientList = []
    for client in clients:
        clientList.append({'id': client.id, 'name': client.name})
    return clientList


def getAllAreas():
    areas = ProductArea.query.all()
    areaList = []
    for area in areas:
        areaList.append({'id': area.id, 'name': area.name})
    return areaList


def createFeatueRequest(req):
    featureRequest = FeatureRequest(
        title=req['title'],
        description=req['description'],
        target_date=req['target_date'],
        client_priority=req['client_priority'],
        client_id=req['client'],
        product_area_id=req['product_area'])

    db.session.add(featureRequest)
    db.session.commit()
    db.session.refresh(featureRequest)
    requestId = featureRequest.serializeModel['requestId']
    updateClientPriority(req['client'], req['client_priority'], requestId)
    return req


def updateClientPriority(clientId, priority, requestId):
    requests = FeatureRequest.query.filter(
        FeatureRequest.client_id == clientId)
    flag = True
    previous = None 
    length = requests.count()
    while(flag):
        swap = False
        for request in requests:
            if request.serializeModel['requestId'] != requestId and request.client_priority == int(priority) and request.serializeModel['requestId'] != previous:
                    request.client_priority += 1
                    priority += 1
                    swap = True   
                    previous = request.serializeModel['requestId']   
                    db.session.commit()
                    break
        if swap == 0:
            flag = False


            # def updateClientPriority(clientId, priority, requestId):
            #     requests = FeatureRequest.query.filter(
            #         FeatureRequest.client_id == clientId).order_by(FeatureRequest.client_priority.desc())
            #     Count = requests.count()
            #     length = requests.count()
            #     first = requests[0].client_priority
            #     last = requests[length-1].client_priority

            #     if length == 1:
            #         requests[0].client_priority = 1
            #         db.session.commit()

            #     elif last - first != length-1 and last - length != 0:
            #         for request in requests:
            #             request.client_priority = length
            #             length -= 1
            #         db.session.commit()


def updateFeatureRequest(req):
    request = FeatureRequest.query.filter(
        FeatureRequest.id == req['requestId']).first()

    request.title = req['title']
    request.description = req['description']
    request.target_date = req['target_date']
    request.client_priority = req['client_priority']
    request.client_id = req['client']
    request.product_area_id = req['product_area']

    db.session.commit()
    updateClientPriority(clientId, req['client_priority'], req['requestId'])
    return req


def deleteFeatureRequest(id):
    request = FeatureRequest.query.filter(FeatureRequest.id == id).first()
    db.session.delete(request)
    db.session.commit()
    return str(request)


