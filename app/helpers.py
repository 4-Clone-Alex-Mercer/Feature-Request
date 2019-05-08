from app import db
from app.models import FeatureRequest, ProductArea, Client


def getRequests():
    requests = FeatureRequest.query.all()
    requestsList = []
    for request in requests:
        requestsList.append(request.serialize)
    return requestsList