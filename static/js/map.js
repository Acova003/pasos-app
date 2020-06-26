
mapboxgl.accessToken = 'pk.eyJ1IjoiYWNvdmEwMDMiLCJhIjoiY2tiZnR4NHhiMHo1bDMwbXptbzVpa2ZqYiJ9.-3yiof0FhfqNoWeqMsa-dw';

var map = new mapboxgl.Map({
  container: 'map',
  style: 'mapbox://styles/acova003/ckbfuohe64i6o1in70tmp7rdt',
  // center will be the user location
  center: [window.currentLocation.latitude, window.currentLocation.longitude],
  zoom: 4.5
});

var geojson = {
  type: 'FeatureCollection',
  features: [{
    type: 'Feature',
    geometry: {
      type: 'Point',
      coordinates: [-8.544630, 42.880761]
    },
    properties: {
      title: 'Mapbox',
      description: 'Santiago de Compostela'
    }
  }]
};

console.log([window.currentLocation.longitude, window.currentLocation.latitude])
var user_location = {
  type: 'FeatureCollection',
  features: [{
    type: 'Feature',
    geometry: {
      type: 'Point',
      coordinates: [window.currentLocation.latitude, window.currentLocation.longitude]
    },
    properties: {
      title: 'Mapbox',
      description: 'User progress on the camino'
    }
  }]
};


// add markers to map
geojson.features.forEach(function(marker) {

  // create a HTML element for each feature
  var el = document.createElement('div');
  el.className = 'santiago';

  // make a marker for each feature and add to the map
  new mapboxgl.Marker(el)
    .setLngLat(marker.geometry.coordinates)
    .addTo(map);
});

user_location.features.forEach(function(marker) {

  // create a HTML element for each feature
  var el = document.createElement('div');
  el.className = 'currentLocation';

  // make a marker for each feature and add to the map
  new mapboxgl.Marker(el)
    .setLngLat(marker.geometry.coordinates)
    .addTo(map);
});

map.addControl(new mapboxgl.NavigationControl());
