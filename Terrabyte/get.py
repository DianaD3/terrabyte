from pymongo import MongoClient # connection
import json
# create client
client = MongoClient(json.load(open('./config.json'))['endpoint'])

# API call to visualize a single collection from a database
def get_collection():
    # create return dict
    return_dict = {
        'pinpoints': list()
    }
    db = client['admin']
    col = db['pinpoints']
    # print all the contents inside the collection
    for data in col.find({}):
        return_dict['pinpoints'].append(data)
    return return_dict

def get_layer(layer_name):
    # create return dict
    return_dict = {
        'pinpoints': list()
    }
    db = client['admin']
    col = db['pinpoints']
    # print all the contents inside the collection
    for data in col.find({}):
        if data['layer'] == layer_name:
            return_dict['pinpoints'].append(data)
    return return_dict

def get_layer_by_location(layer_name, latmin, latmax, longmin, longmax):
    # create return dict
    return_dict = {
        'pinpoints': list()
    }
    db = client['admin']
    col = db['pinpoints']
    # print all the contents inside the collection
    for data in col.find({}):
        # check for a specific layer
        if data['layer'] == layer_name:
            # search all pinpoints in the latmin-latmax and longmin-longmax range
            if data['location']['lat'] >= latmin and data['location']['lat'] <= latmax:
                if data['location']['long'] >= longmin and data['location']['long'] <= longmax:
                    return_dict['pinpoints'].append(data)

    # return all the pinpoints
    return return_dict