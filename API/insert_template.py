from pymongo import MongoClient # connection
from datetime import datetime # time
import numpy as np # random numbers

# create connection
client = MongoClient('mongo endpoint')
# connect to a database
db = client['db name']
# select a table (if non existent it will automatically create one)
col = db['col name']

# prepare the data for insertion
data = {
    'timestamp': str(datetime.today()).split()[0],
    'location': {
        'lat': np.random.randint(1,10),
        'long': np.random.randint(1,10)
    },
    'value': np.random.randint(1,10),
    'layer': "test"
}
# insert
col.insert_one(data)



