function initialize() {
        var fenway = {lat: window.currentLocation.latitude, lng: window.currentLocation.longitude};
        var sVS = new google.maps.StreetViewService();
        sVS.getPanoramaByLocation(fenway, 500,
          function (streetViewPanoramaData, status) {
            if (status === google.maps.StreetViewStatus.OK) {

              document.getElementById('googleSVLocation').innerHTML = streetViewPanoramaData.location.description;
              var panorama = new google.maps.StreetViewPanorama(
                  document.getElementById('pano'), {
                    position: streetViewPanoramaData.location.latLng,
                    pov: {
                      heading: 34,
                      pitch: 10
                    },
                    motionTracking: true,
                    motionTrackingControl: true
                  });
                  var image = {
                    url: '../static/img/trail_marker.png',
                    scaledSize : new google.maps.Size(100, 100),
                };
                  var cafeMarker = new google.maps.Marker({
                    position: { lat: window.currentLocation.latitude, lng: window.currentLocation.longitude },
                    map: panorama,
                    icon: image,
                    title: "Cafe"
                  });
            } else {
              console.log('Location does not exist', streetViewPanoramaData);
            }
          }
        )
      }
