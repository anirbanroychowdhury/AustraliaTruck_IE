// This example requires the Places library. Include the libraries=places
// parameter when you first load the API. For example:
// <script
// src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=places">
let infoWindow;
let pos;
// function getCurrentLocationInit(){
//     if(navigator.geolocation) {
//         navigator.geolocation.getCurrentPosition(success);
//     }
// }

// function success(position){
//     lat  = position.coords.latitude;
//     lng =  position.coords.longitude;
//     return [lat,lng]

// }

function initMap() {
    //Declare direction and render services
    const directionsService = new google.maps.DirectionsService();
    const directionsRenderer = new google.maps.DirectionsRenderer();
    //create a map centred on melbourne
    const map = new google.maps.Map(document.getElementById("map"), {
      mapTypeControl: false,
      center: { lat: 37.9145, lng: 145.1275 },
      zoom: 13,
    });
    //create a infowindow for locate me services
    infoWindow = new google.maps.InfoWindow()
    //set the direction renderer on the map
    directionsRenderer.setMap(map);
    directionsRenderer.setPanel(document.getElementById("right-panel"));
    //create the locate me button
    const locationButton = document.createElement("button");
    //Add text to the button
    locationButton.textContent = "Locate me";
    //Add class
    locationButton.classList.add("custom-map-control-button");
    //Push the button to the top left corner
    map.controls[google.maps.ControlPosition.TOP_LEFT].push(locationButton);
    //Set up listener
    const onLocationChangeHandler = function () {
        getCurrentLocation(map);
    }
    //Add listener
    locationButton.addEventListener("click",onLocationChangeHandler);
    //Add markers by loading geoJson
    map.data.loadGeoJson("../static/Rest_Area.geojson");
    // map.data.addListener('mouseover', function(event) {
    //     console.log(event['latLng'].lat());
    //     console.log(event['latLng'].lng());
    // });
    map.data.addListener('click',function(event) {
        destinationLat = event['latLng'].lat();
        destinationLng = event['latLng'].lng();
        destinationLoc = new google.maps.LatLng(destinationLat, destinationLng);
        originLat = pos['lat'];
        originLng = pos['lng'];
        startLoc = new google.maps.LatLng(originLat, originLng);
        route(directionsService, directionsRenderer, startLoc, destinationLoc)
    });
    console.log("At the end");
  }
  

  function route(directionsService, directionsRenderer, start, end) {
    //Check if both the origin and destination is in place, if not return
    if (!start || !end) {
        return;
    }
    // Call the route function
    directionsService.route(
        {
            //set required inputs
            origin: start,
            destination: end,
            travelMode: google.maps.TravelMode.DRIVING,
        },
        //Checkf for the response
        (response, status) => {
            //if status ok
            if (status === "OK") {
                //Render the route received
                directionsRenderer.setDirections(response);
            } else {
                //Displa alert
                window.alert("Directions request failed due to " + status);
            }
        }
    );
} 

//PARAM: map object
//Fetch current location, throw error if permission not granted
function getCurrentLocation(map){
    //Check permission
    if (navigator.geolocation){
        navigator.geolocation.getCurrentPosition(
            (position) => {
                // Current location lat & Lng
                pos = {
                    lat: position.coords.latitude,
                    lng: position.coords.longitude,
                };
                //Set position
                infoWindow.setPosition(pos);
                infoWindow.setContent("Location Found");
                // Set on map
                infoWindow.open(map);
                // Center map on location
                map.setCenter(pos);
            }, () => {
                handleLocationError(false, infoWindow, map.getCenter());
            }
        )
    }
}

