// Function that reads field data
function calculateAndDisplay(service, display){
  var start = document.getElementById("start").value;
  var end = document.getElementById("end").value;
  service.route({
    origin: start, 
    destination: end,
    travelMode: "DRIVING"
  }, function(response, status){
    if (status === "OK"){
      display.setDirections(response);
    } else {
      window.alert("directions cannot be found " + status);
    }
  });
}

function initMap() {
  var display = new google.maps.DirectionsRenderer;
  var service = new google.maps.DirectionsService;
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 7,
    center: {lat: 41.85, lng: -87.65}
  });  
  display.setMap(map);
  display.setPanel(document.getElementById("right-panel"));

  var control = document.getElementById("floating-panel");
  control.style.display = "block";

  map.controls[google.maps.ControlPosition.TOP_CENTER].push(control);

  var onChange = function(){
    calculateAndDisplay(service, display);
  };  
  document.getElementById("start").addEventListener("change", onChange);
  document.getElementById("end").addEventListener("change", onChange);
}  

