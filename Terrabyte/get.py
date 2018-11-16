from pymongo import MongoClient # connection
import json
# create client
client = MongoClient(json.load(open('./config.json'))['endpoint'])

# API call for visualizing the whole mongo db
def visualize_mongo():
    # create return dict
    return_dict = {
        'pinpoints': list()
    }
    # find all databases
    for db_name in client.list_database_names():
        # select current databse
        db = client[db_name]
        # find all collections
        for col_name in db.command("listCollections")['cursor']['firstBatch']:
            # find the collection name
            col_name = col_name['name']
            # select collection
            col = db[col_name]
            # print all the contents inside the collection
            for data in col.find({}):
                return_dict['pinpoints'].append(data)
    return return_dict

# API call for visualizing a single database
def visualize_database(database):
    # create return dict
    return_dict = {
        'pinpoints': list()
    }
    # select database
    db = client[database]
    # find all collections
    for col_name in db.command("listCollections")['cursor']['firstBatch']:
        # select the collection name
        col_name = col_name['name']
        # select collection
        col = db[col_name]
        # save all the contents inside the collection
        for data in col.find({}):
            return_dict['pinpoints'].append(data)
    return return_dict
            
# API call to visualize a single collection from a database
def visualize_collection(database,collection):
    # create return dict
    return_dict = {
        'pinpoints': list()
    }
    db = client[database]
    col = db[collection]
    # print all the contents inside the collection
    for data in col.find({}):
        return_dict['pinpoints'].append(data)
    return return_dict
