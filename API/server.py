from flask import Flask # Flask
from flask import request
from flask_cors import CORS
from Terrabyte import get, prepare, insert # our functions
import numpy as np
from ML import ml

app = Flask(__name__) # init flask
CORS(app)

@app.route('/') # home roune
def index():
    return "Terrabyte"

@app.route('/get/collection') # get pinpoint collection
def get_collections():
    return prepare.data_to_json(get.get_collection())

@app.route('/get/layer/<layer_name>') # get single layer
def get_layer(layer_name):
    return prepare.data_to_json(get.get_layer(str(layer_name)))

@app.route('/get/layer/location/<layer_name>/<latmin>/<latmax>/<longmin>/<longmax>') # get specific location pinpoints from layer
def get_layer_by_location(layer_name,latmin,latmax,longmin,longmax):
    return prepare.data_to_json(get.get_layer_by_location(str(layer_name),float(latmin),float(latmax),float(longmin),float(longmax)))

@app.route('/get/layer/time/<layer_name>/<datestart>/<timestart>/<datestop>/<timestop>') # get specific time pinpoint from layer
def get_layer_by_time(layer_name, datestart, timestart, datestop, timestop):
    start = datestart + " " + timestart
    stop = datestop + " " + timestop
    json_data = get.get_layer_by_timestamp(str(layer_name),str(start),str(stop))
    geojson =  {
        'type': 'FeatureCollection',
        'features': list()
    }
    for point in json_data['pinpoints']:
        geojson['features'].append(prepare.json_to_geojson(point))
    
    return prepare.data_to_json(geojson)

@app.route('/get/layers')
def get_layers():
    data = get.get_collection()
    layers = {
        'layers': list()
    }
    for row in data['pinpoints']:
        layers['layers'].append(row['layer'])
    layers['layers'] = set(layers['layers'])
    return prepare.data_to_json(layers)

@app.route('/insert/single', methods=['POST'])
def insert_single():
    data = request.get_json()
    if insert.insert_data_point(data['location']['lat'],data['location']['long'],data['value'],data['layer'],data['timestamp']):
    	return 'Inserted'
    return 'Error'

@app.route('/insert/multiple', methods=['POST'])
def insert_multiple():
    data = request.get_json()
    insert_data = []
    for row in data['pinpoints']:
        insert_data = prepare.prepare_points(insert_data, row['location']['lat'], row['location']['long'], row['value'], row['layer'],row['timestamp'])
    if insert.insert_many_points(insert_data):
        return 'Insert'
    else:
        return 'Error'

@app.route('/ml/forecasting', methods=["POST"])
def forecasting():
    data = request.get_json()['input']
    output = ml.forecast(data, int(0.1*len(data)))
    return prepare.data_to_json({
        'output': output
    })

@app.route('/ml/anomaly', methods=["POST"])
def anomaly():
    data = request.get_json()['input']
    output = ml.anomaly_detection(data).tolist()
    return prepare.data_to_json({
        'output': output
    })
# run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0")
