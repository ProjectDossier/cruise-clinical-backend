import pandas as pd
from pymongo import MongoClient
import json

def mongoimport(csv_path, db_name, coll_name, client,sep='\t'):
    """ Imports a csv file at path csv_name to a mongo colection
    returns: IDs of the inserted document
    """
    db = client[db_name]
    coll = db[coll_name]
    data = pd.read_csv(csv_path,sep=sep)
    payload = json.loads(data.to_json(orient='records'))
    x=coll.insert_many(payload)
    return x.inserted_ids

def mongofind_all_specific_col(db_name,client,coll_name,column):
    db = client[db_name]
    coll = db[coll_name]
    docs = coll.find({}, {column: 1, '_id': 0,'ID':1 })
    final_list=[]
    for doc in docs:
        final_list.append(doc)
    return final_list

def mongofind_all_specific_cond(db_name,client,coll_name,conditions):
    db=client[db_name]
    coll = db[coll_name]
    cleaned_conditions={k: v for k, v in conditions.items() if v}
    docs = coll.find(cleaned_conditions,{'id':1,'_id':0,'name':1,'dob':1,'texts':1})
    final_list={}

    for doc in docs:
        final_list[doc['id']]={'name':doc['name'],'dob':doc['dob'],'texts':doc['texts']}
    return final_list

def mongoimport_onesent(pid,query1,query2,db_name,client,coll_name):
    db=client[db_name]
    coll = db[coll_name]
    oldquery={'id':pid,'query1':query1,'query2':query2}
    x=coll.insert_one(oldquery)
    return x.acknowledged



