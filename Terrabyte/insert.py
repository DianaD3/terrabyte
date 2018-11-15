from pymongo import MongoClient # connection
from datetime import datetime # time
import json

# create the mongo client
client = MongoClient(json.load(open('./config.json'))['endpoint'])

# API call for inserting a single data point
def insert_data_point(latitude, longitude, value, layer):
    # connect to a database
    db = client['admin']
    # select a table (if non existent it will automatically create one)
    col = db['test']
    # prepare the data for insertion
    data = {
        'timestamp': str(datetime.today()).split('.')[0],
        'location': {
            'lat': latitude,
            'long': longitude
        },
        'value': value,
        'layer': layer
    }
    # insert the data
    col.insert_one(data)

def insert_many_points(points):
    # connect to a database
    db = client['admin']
    # select a table (if non existent it will automatically create one)
    col = db['test']
    # insert the data
    col.insert_many(points)