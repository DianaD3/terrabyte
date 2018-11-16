from flask import Flask
from Terrabyte import get, prepare

app = Flask(__name__)

@app.route('/')
def index():
    return "Terrabyte"

@app.route('/get/collection')
def get_collections():
    return prepare.data_to_json(get.get_collection())

@app.route('/get/layer/<layer_name>')
def get_layer(layer_name):
    return prepare.data_to_json(get.get_layer(str(layer_name)))

@app.route('/get/layer/location/<layer_name>/<latmin>/<latmax>/<longmin>/<longmax>')
def get_layer_by_location(layer_name,latmin,latmax,longmin,longmax):
    return prepare.data_to_json(get.get_layer_by_location(str(layer_name),float(latmin),float(latmax),float(longmin),float(longmax)))

@app.route('/get/layer/time/<layer_name>/<datestart>/<timestart>/<datestop>/<timestop>')
def get_layer_by_time(layer_name, datestart, timestart, datestop, timestop):
    start = datestart + " " + timestart
    stop = datestop + " " + timestop
    return prepare.data_to_json(get.get_layer_by_timestamp(str(layer_name),str(start),str(stop)))

if __name__ == "__main__":
    app.run(debug=True)