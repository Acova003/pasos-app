function initialize() {
        var fenway = {lat: window.currentLocation.latitude, lng: window.currentLocation.longitude};
        console.log('fenway', fenway)

        var sVS = new google.maps.StreetViewService();
        sVS.getPanoramaByLocation(fenway, 500,
          function (streetViewPanoramaData, status) {
            if (status === google.maps.StreetViewStatus.OK) {
              console.log('Location exists', streetViewPanoramaData);
              document.getElementById('googleSVLocation').innerHTML = streetViewPanoramaData.location.description;
              var panorama = new google.maps.StreetViewPanorama(
                  document.getElementById('pano'), {
                    position: streetViewPanoramaData.location.latLng,
                    pov: {
                      heading: 34,
                      pitch: 10
                    }
                  });
              console.log('panorama', panorama);
            } else {
              console.log('Location does not exist', streetViewPanoramaData);
            }
          }
        )
        // map.setStreetView(panorama);
      }
      // window.currentLocation.latitude, window.currentLocation.longitude
      // current 43.0250000674278, -1.32930119521916]
      // santiago -8.545802067965269,"lat":42.88085061125457
// 43.04032562300563", "lon": "-1.281128469854593
      // [43.0250000674278, -1.32930119521916]
