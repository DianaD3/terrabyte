import React from 'react'
import ReactDOM from 'react-dom'
import mapboxgl from 'mapbox-gl'
import data from './sample_data.json'
//import mapboxSdk from '@mapbox/mapbox-sdk'
//import Geocoder from 'react-map-gl-geocoder'

mapboxgl.accessToken = 'pk.eyJ1IjoiZGlhbmFkMyIsImEiOiJjam9qdTVpODUwOGQ2M2xwanBrcnNrczdoIn0.17CYLLGtE45Y3rkNkSCSSA';

class Application extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      lng: 5,
      lat: 34,
      zoom: 2.5,
    };
  }

  componentDidMount() {

    /*  fetch('https://github.com/paubric/terrabyte/blob/master/Terrabyte/get.py')
     .then(res => res.json()); */
    const { lng, lat, zoom } = this.state;
   
    const map = new mapboxgl.Map({
      container: this.mapContainer,
      style: 'mapbox://styles/mapbox/dark-v9',
      center: [lng, lat],
      zoom,
      pitchWithRotate: false,
      touchZoomRotate: false,
    });

    map.on('move', () => {
      const { lng, lat } = map.getCenter();

      this.setState({
        lng: lng.toFixed(4),
        lat: lat.toFixed(4),
        zoom: map.getZoom().toFixed(2)
      });
    });

    //LOCALIZATE USER
    map.addControl(new mapboxgl.GeolocateControl({
      positionOptions: {
        enableHighAccuracy: true
      },
      trackUserLocation: true
    }));

    //DRAG DISABLED
    map.dragRotate.disable();
    map.touchZoomRotate.disableRotation();

    map.on('load', function () {

      map.addSource('earthquakes', {
        type: 'geojson',
        data
      })

      map.addLayer({
        "id": "earthquakes-heat",
        "type": "heatmap",
        "source": "earthquakes",
        "maxzoom": 9,
        "paint": {
            // Increase the heatmap weight based on frequency and property magnitude
            "heatmap-weight": [
                "interpolate",
                ["linear"],
                ["get", "mag"],
                0, 0,
                6, 1
            ],
            // Increase the heatmap color weight weight by zoom level
            // heatmap-intensity is a multiplier on top of heatmap-weight
            "heatmap-intensity": [
                "interpolate",
                ["linear"],
                ["zoom"],
                0, 1,
                9, 3
            ],
            // Color ramp for heatmap.  Domain is 0 (low) to 1 (high).
            // Begin color ramp at 0-stop with a 0-transparancy color
            // to create a blur-like effect.
            "heatmap-color": 'red',
            // Adjust the heatmap radius by zoom level
            "heatmap-radius": [
                "interpolate",
                ["linear"],
                ["zoom"],
                0, 2,
                9, 20
            ],
            // Transition from heatmap to circle layer by zoom level
            "heatmap-opacity": [
                "interpolate",
                ["linear"],
                ["zoom"],
                7, 1,
                9, 0
            ],
        }
    }, 'waterway-label');

    map.addLayer({
        "id": "earthquakes-point",
        "type": "circle",
        "source": "earthquakes",
        "minzoom": 7,
        "paint": {
            // Size circle radius by earthquake magnitude and zoom level
            "circle-radius": [
                "interpolate",
                ["linear"],
                ["zoom"],
                7, [
                    "interpolate",
                    ["linear"],
                    ["get", "mag"],
                    1, 1,
                    6, 4
                ],
                16, [
                    "interpolate",
                    ["linear"],
                    ["get", "mag"],
                    1, 5,
                    6, 50
                ]
            ],
            // Color circle by earthquake magnitude
            "circle-color": [
                "interpolate",
                ["linear"],
                ["get", "mag"],
                1, "rgba(33,102,172,0)",
                2, "rgb(103,169,207)",
                3, "rgb(209,229,240)",
                4, "rgb(253,219,199)",
                5, "rgb(239,138,98)",
                6, "rgb(178,24,43)"
            ],
            "circle-stroke-color": "white",
            "circle-stroke-width": 1,
            // Transition from heatmap to circle layer by zoom level
            "circle-opacity": [
                "interpolate",
                ["linear"],
                ["zoom"],
                7, 0,
                8, 1
            ]
        }
    }, 'waterway-label');
    
    });

   /*  var mapboxClient = mapboxSdk({ accessToken: mapboxgl.accessToken });

    mapboxClient.geocoding.forwardGeocode({
      query: 'Wellington, New Zealand',
      autocomplete: false,
      limit: 1
  })
      .send()
      .then(function (response) {
          if (response && response.body && response.body.features && response.body.features.length) {
              var feature = response.body.features[0];
  
              var map = new mapboxgl.Map({
                  container: 'map',
                  style: 'mapbox://styles/mapbox/streets-v9',
                  center: feature.center,
                  zoom: 10
              });
              new mapboxgl.Marker()
                  .setLngLat(feature.center)
                  .addTo(map);
          }
      }); */
  } 

  render() {
    const { lng, lat, zoom, imageURL } = this.state;
    return (
      <div>
        <div className="inline-block absolute top left mt12 ml12 bg-darken75 color-white z1 py6 px12 round-full txt-s txt-bold">
          <div>{`Longitude: ${lng} Latitude: ${lat} Zoom: ${zoom}`}</div>
        </div>
        <div ref={el => this.mapContainer = el} className="absolute top right left bottom" />
        {/* <img src={this.state.imageURL} alt="img" /> */}
      </div>
    );
  }
}

ReactDOM.render(<Application />, document.getElementById('app'));

