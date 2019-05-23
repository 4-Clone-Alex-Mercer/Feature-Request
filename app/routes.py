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


@routes.route('/request/create', methods=['GET', 'POST'])
def createRequests():
    print(1)
    if request.method == "POST":
        print(request.get_json())
        data = request.get_json()
        from app.helpers import addFeatueRequest
        return jsonify(addFeatueRequest(data))


@routes.route('/request/update', methods=['GET', 'PUT'])
def updateRequests():
    print(2)    
    if request.method == "PUT":
        data =  request.get_json()
        from app.helpers import updateRequest
        return jsonify(updateRequest(data))



@routes.route('/request/delete', methods=['GET', 'DELETE'])
def deleteRequests():   
    print(3)
    if request.method == "DELETE":
        data =  request.get_json()
        from app.helpers import deleteRequest
        return jsonify(deleteRequest(data))
     