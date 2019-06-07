from app import db
from app.models import FeatureRequest, ProductArea, Client



def getAllRequests():
    """Returns A List Of All The Feature Requests"""
    requests = FeatureRequest.query.all()
    requestsList = []
    for request in requests:
        requestsList.append(request.serializeModel)
    return requestsList


def getAllClients():
    """Returns A List Of All The Clients"""
    clients = Client.query.all()
    clientList = []
    for client in clients:
        clientList.append({'id': client.id, 'name': client.name})
    return clientList


def getAllAreas():
    """Returns A List Of All The Product Areas"""
    areas = ProductArea.query.all()
    areaList = []
    for area in areas:
        areaList.append({'id': area.id, 'name': area.name})
    return areaList


def createFeatueRequest(req):
    """Saves A Feature Request To The DB"""
    featureRequest = FeatureRequest(
        title=req['title'],
        description=req['description'],
        target_date=req['target_date'],
        client_priority=req['client_priority'],
        client_id=req['client'],
        product_area_id=req['product_area'])

    db.session.add(featureRequest)
    db.session.commit()
    # Refresh The Inserted Request To Get Its ID Back
    db.session.refresh(featureRequest)
    requestId = featureRequest.serializeModel['requestId']
    updateClientPriority(req['client'], req['client_priority'], requestId)
    return req

# Will Update Priority While Keeping Gaps Between The Priorities


def updateClientPriority(clientId, priority, requestId):
    """Change The Priorities For A Spcefic Client Depened On The Newly Added/Updated Request With Gaps"""
    requests = FeatureRequest.query.filter(
        FeatureRequest.client_id == clientId).order_by(FeatureRequest.client_priority)
    for request in requests:
        if request.client_priority == int(priority) and request.serializeModel['requestId'] != requestId:
            request.client_priority += 1
            priority += 1
            db.session.commit()

        # def updateClientPriority(clientId, priority, requestId):
        #  """Change The Priorities For A Spcefic Client Depened On The Newly Added/Updated Request Without Gaps """
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
    """Update A spesfic Feature Request"""
    request = FeatureRequest.query.filter(
        FeatureRequest.id == req['id']).first()

    request.title=req['title']
    request.description=req['description']
    request.target_date=req['target_date']
    request.client_priority=req['client_priority']
    request.client_id=req['client']
    request.product_area_id=req['product_area']

    db.session.commit()
    updateClientPriority(
        req['client'], req['client_priority'], req['id'])
    return req


def deleteFeatureRequest(id):
    """Deletes A Spesfic Feature Request"""
    request = FeatureRequest.query.filter(FeatureRequest.id == id).first()
    db.session.delete(request)
    db.session.commit()
    return str(request)
