# Terrabyte

![](https://github.com/paubric/terrabyte/blob/master/Terrabyte.png)

## Main Components
### Database

- timestamp
- location (lat, long)
- value
- layer

### API

**POST** Add pinpoint array

```
{
  pinpoints: [
    {
      timestamp: '2018-11-15',
      location: {
        lat: 44.439663,
        long: 26.096306
      },
      value: 30,
      layer: 'air_temperature'
    },
    {
      timestamp: '2018-11-15',
      location: {
        lat: 46.770439,
        long: 23.591423
      },
      value: 27,
      layer: 'air_temperature'
    }
  ]
}
```

**GET** <br>
#### Gets all pinpoints
```
/get/collection
```
#### Gets all data from a layer
```
/get/layer/*layer_name*
```
#### Gets all data from a layer at a specific location
```
/get/layer/location/*layer_name*/*latmin*/*latmax*/*longmin*/*longmax*
```
#### Gets all data from a layer at a specific time
datestart/datestop - expects a date in the format yyyy-mm-dd <br>
timestart/timestop - expects an hour in the format hh:mm:ss
```
/get/layer/time/*layer_name*/*datestart*/*timestart*/*datestop*/*timestop*
```
### Web Interface
### Advanced Analysis

## TODO
### Day 1
- Created insert, get, prepare functions
- Started working on front-end
### Day 2
- Created API
- More front-end
### Day 3
