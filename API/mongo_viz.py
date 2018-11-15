from pymongo import MongoClient # get the client

# create client
client = MongoClient('mongo endpoint')

# find all databases
for db_name in client.list_database_names():
    # print current databse
    print("db", db_name)
    db = client[db_name]
    # find all collections
    for col_name in db.command("listCollections")['cursor']['firstBatch']:
        # select the collection name
        col_name = col_name['name']
        # print currect collection
        print("col", col_name)
        col = db[col_name]
        # print all the contents inside the collection
        for data in col.find({}):
            print(data)
