import flask
from flask import request, jsonify
import json
import signal
from flask_cors import CORS
from pymongo import MongoClient
from utils.index_csv import *
from core import argsparser
import atexit


app = flask.Flask(__name__)
CORS(app)
app.config["DEBUG"] = True

ARGS = argsparser.prepare_args()
mongo_url = 'mongodb://%s:%s@%s:%s' % (ARGS.mongo_user,ARGS.mongo_password,ARGS.mongo_host,ARGS.mongo_port)
client = MongoClient(mongo_url)
dbname=ARGS.db_name
coll_name=ARGS.collection_name


@app.before_first_request
def before_first_request_func():
    print("Building Mongo")
    ids = mongoimport('%s' % ARGS.dummy_data_path, dbname, coll_name, client)

@atexit.register
def cleanup():
    print("Cleaning up")
    db=client[dbname]
    db.drop_collection(coll_name)


@app.route('/get_patient_list', methods=['GET'])
def get_patient_list():
    result=mongofind_all_specific_col(dbname,client,coll_name,column='Name')
    return jsonify(result)


#Get patients with specific name and specific dob
@app.route('/get_patients', methods=['GET'])
def get_patient_list():
    request_args = request.get_json(force=True)
    name,dob=request_args['name'], request_args['dob']
    result=mongofind_all_specific_cond(dbname,client,coll_name,{'Name':name,'DoB':dob})
    return jsonify(result)

app.run(host=ARGS.host, port=5000)

atexit.register(cleanup)
signal.signal(signal.SIGTERM, cleanup)
signal.signal(signal.SIGINT, cleanup)

