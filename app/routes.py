from flask import render_template, Blueprint, jsonify, request
routes = Blueprint('routes', __name__, static_folder='./app/static')


@routes.route("/")
def index():
    return render_template('index.html')


@routes.route('/requests', methods=['GET'])
def getRequests():
    from app.helpers import getRequests
    return jsonify(getRequests())


@routes.route('/clients', methods=['GET'])
def getClients():
    from app.helpers import getClients
    return jsonify(getClients())


@routes.route('/areas', methods=['GET'])
def getAreas():
    from app.helpers import getAreas
    return jsonify(getAreas())


@routes.route('/request/create', methods=['POST'])
def createRequests():
    print(1)
    from app.helpers import validatePostRequest, addFeatueRequest
    data = request.get_json()
    if request.method == "POST" and validatePostRequest(data):
        return jsonify(addFeatueRequest(data)) 
  

@routes.route('/request/update', methods=['PUT'])
def updateRequests():
    print(2)
    from app.helpers import validatePostRequest, updateRequest
    data = request.get_json()
    if request.method == "PUT" and validatePostRequest(data):
        return jsonify(updateRequest(data))


@routes.route('/request/delete', methods=['DELETE'])
def deleteRequests():
    print(3)
    if request.method == "DELETE":
        data = request.get_json()
        from app.helpers import deleteRequest
        return jsonify(deleteRequest(data))
