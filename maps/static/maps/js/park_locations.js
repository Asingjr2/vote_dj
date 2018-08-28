function initMap() {
  var display = new google.maps.DirectionsRenderer;
  var service = new google.maps.DirectionsService;
  var map = new google.maps.Map(document.getElementById("map"), {
    zoom: 11,
    center: {lat: 38.85, lng: -77.16},
  });
  display.setMap(map);
  display.setPanel(document.getElementById("bottom-panel"));

  
  var Alexandria_DP = new google.maps.Marker({
    position: {lat:38.83, lng: -77.10},
    map: map,
    title: 'Alexandria Dog Park!'
  });

  var Tysons_DP = new google.maps.Marker({
    position: {lat: 38.91, lng: -77.22},
    map: map,
    title: "Tyson's Corner Dog Park!"
  });

  var Falls_Church_DP = new google.maps.Marker({
    position: {lat: 38.88, lng: -77.17},
    map: map,
    title: 'Falls Church Dog Park!'
  });

  var Arlington_DP = new google.maps.Marker({
    position: {lat: 38.88, lng: -77.10},
    map: map,
    title: 'Arlington Dog Park!'
  });

  var Springfield_DP = new google.maps.Marker({
    position: {lat: 38.77, lng: -77.17},
    map: map,
    title: 'Springfield Dog Park'
  });

  var Washington_DP1 = new google.maps.Marker({
    position: {lat: 38.88, lng: -77.05},
    map: map,
    title: 'Washington Dog Park'
  });

  var Washington_DP2 = new google.maps.Marker({
    position: {lat: 38.87, lng: -77.03},
    map: map,
    title: 'Washington Dog Park'
  });
 
  }
