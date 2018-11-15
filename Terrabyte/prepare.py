from datetime import datetime # time
import json

def prepare_points(points, latitude, longitude, value, layer):
    data = {
        'timestamp': str(datetime.today()).split('.')[0],
        'location': {
            'lat': latitude,
            'long': longitude
        },
        'value': value,
        'layer': layer
    }
    points.append(data)
    return points