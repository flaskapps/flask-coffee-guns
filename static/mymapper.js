function makemap(accesstoken, places){
  L.mapbox.accessToken = accesstoken;
  var mapLeaflet = L.mapbox.map('the-map', 'mapbox.light')
    .setView([37.8, -96], 4);

  L.marker([38.913184, -77.031952]).addTo(mapLeaflet);
  L.marker([37.775408, -122.413682]).addTo(mapLeaflet);

  mapLeaflet.scrollWheelZoom.disable();
}


