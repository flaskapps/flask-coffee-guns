function makemap(accesstoken, place){
  L.mapbox.accessToken = accesstoken;
  var coords = [place['latitude'], place['longitude']];
  var mapLeaflet = L.mapbox.map('the-map', 'mapbox.light')
                           .setView(coords, 5);

  L.marker(coords).addTo(mapLeaflet);

  mapLeaflet.scrollWheelZoom.disable();
}


