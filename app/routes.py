from flask import render_template, Blueprint, jsonify

routes = Blueprint('routes', __name__, static_folder='./app/static')


@routes.route("/")
def index():
    return render_template('index.html')


@routes.route('/requests', methods=['GET'])
def getRequests():
    from app.helpers import getRequests
    return jsonify(getRequests())
