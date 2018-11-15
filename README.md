# Terrabyte

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

**GET** Get pinpoint array based on layer

### Web Interface
### Advanced Analysis

## TODO
### Day 1
### Day 2
### Day 3
