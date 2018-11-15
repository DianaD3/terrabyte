from pymongo import MongoClient # connection
import json
# create client
client = MongoClient(json.load(open('./config.json'))['endpoint'])

# API call for visualizing the whole mongo db
def visualize_mongo():
    # find all databases
    for db_name in client.list_database_names():
        # print current databse
        print("db:", db_name)
        db = client[db_name]
        # find all collections
        for col_name in db.command("listCollections")['cursor']['firstBatch']:
            # select the collection name
            col_name = col_name['name']
            # print currect collection
            print("col:", col_name)
            col = db[col_name]
            # print all the contents inside the collection
            for data in col.find({}):
                print(data)

# API call for visualizing a single database
def visualize_database(database):
    # print selected database
    print("db:", database)
    db = client[database]
    # find all collections
    for col_name in db.command("listCollections")['cursor']['firstBatch']:
        # select the collection name
        col_name = col_name['name']
        # print currect collection
        print("col:", col_name)
        col = db[col_name]
        # print all the contents inside the collection
        for data in col.find({}):
            print(data)
            
# API call to visualize a single collection from a database
def visualize_collection(database,collection):
    # print selected database
    print("db:", database)
    db = client[database]
    # print selected collection
    print("col:", collection)
    col = db[collection]
    # print all the contents inside the collection
    for data in col.find({}):
        print(data)
