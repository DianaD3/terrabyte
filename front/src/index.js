import React from 'react'
import ReactDOM from 'react-dom'
import mapboxgl from 'mapbox-gl'
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

      map.addLayer({
        "id": "points",
        "type": "symbol",
        "source": {
          "type": "geojson",
          "data": {
            "type": "FeatureCollection",
            "features": [{
              "type": "Feature",
              "geometry": {
                "type": "Point",
                "coordinates": [-77.03238901390978, 38.913188059745586]
              },
              "properties": {
                "title": "Mapbox DC",
                "icon": "monument"
              }
            }, 
          ]
          }
        },
        "layout": {
          "icon-image": "{icon}-15",
          "text-field": "{title}",
          "text-font": ["Open Sans Semibold", "Arial Unicode MS Bold"],
          "text-offset": [0, 0.6],
          "text-anchor": "top"
        }
      });
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

