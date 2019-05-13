from flask import render_template, Blueprint, jsonify, request

routes = Blueprint('routes', __name__, static_folder='./app/static')


@routes.route("/")
def index():
    return render_template('index.html')


@routes.route('/requests', methods=['GET'])
def getRequests():
    from app.helpers import getRequests
    return jsonify(getRequests())


@routes.route('/request/create', methods=['GET', 'POST'])
def createRequest():
    if request.method == "POST":
        data = request.form.to_dict()
        from app.helpers import addFeatueRequest
        return jsonify(addFeatueRequest(data))


@routes.route('/request/update', methods=['GET', 'PUT'])
def updateRequest():
    print(request.form)    
    if request.method == "PUT":
       print(2)



@routes.route('/request/delete', methods=['GET', 'DELETE'])
def deleteRequest():
    print(request.form)
    if request.method == "DELETE":
       print(1)        