from flask import render_template, Blueprint, jsonify, request
routes = Blueprint('routes', __name__, static_folder='./app/static')


@routes.route("/")
def index():
    return render_template('index.html')


@routes.route('/requests', methods=['GET'])
def getAllRequests():
    from app.helpers import getAllRequests
    return jsonify(getAllRequests())


@routes.route('/clients', methods=['GET'])
def getAllClients():
    from app.helpers import getAllClients
    return jsonify(getAllClients())


@routes.route('/areas', methods=['GET'])
def getAllAreas():
    from app.helpers import getAllAreas
    return jsonify(getAllAreas())


@routes.route('/request/create', methods=['POST'])
def createFeatureRequests():
    from app.helpers import createFeatueRequest
    data = request.get_json()
    return jsonify(createFeatueRequest(data))

        

@routes.route('/request/update', methods=['PUT'])
def updateFeatureRequests():
    from app.helpers import updateFeatureRequest
    data = request.get_json()
    return jsonify(updateFeatureRequest(data))    


@routes.route('/request/delete', methods=['DELETE'])
def deleteFeatureRequests():
    data = request.get_json()
    from app.helpers import deleteFeatureRequest
    return jsonify(deleteFeatureRequest(data))
