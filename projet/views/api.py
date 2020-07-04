from functools import wraps
import json
from cassandra.cqlengine import connection
from flask import Blueprint, Response
import flask
from models.user import City
import util

__author__ = 'hangvirus'

api = Blueprint("api", __name__)

connection.setup(['127.0.0.1'], "cqlengine", protocol_version=3)


def json_api(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        result = f(*args, **kwargs)  # Call Function
        json_result = util.to_json(result)
        return Response(response=json_result,
                        status=200,
                        mimetype="application/json")

    return decorated_function


@api.route('/', defaults={"path": ""})
@api.route('/<path:path>')
def index(path=None):
    return "Hello World"







@api.route("/add", methods=["POST"])
@json_api
def add_city():
    data = json.loads(flask.request.data)
      
    city = City.create(idcity=data["idcity"], cityname=data["cityname"], 
    latitude=data["latitude"], longitude=data["longitude"], population=data["population"])
    City.save()
    return city.get_data()


    @api.route("/update", methods=["PUT"])
@json_api
def update_city():
    data = json.loads(flask.request.data)
    city =City.objects(idcity=data["idcity"]).update( cityname=data["cityname"], 
    latitude=data["latitude"], longitude=data["longitude"], population=data["population"])
    City.save()
    return city.get_data()



@api.route("/Delete", methods=["DELETE"])
@json_api
    def delete_shopping_list(idcity):
    
        query = City.get(idcity=idcity)
        query.delete()
        return city.get_data()



@api.route("/get-all")
@json_api
def get_all():
    cities = City.objects().all()
    return [city.get_data() for city in cities]



@api.route("/drop_table")
@json_api
    def drop_tables():
    
    drop_table(City)