let map, infoWindow;
//Funciton to initalize map
function initMap() {
    //initalize google services
    const directionsService = new google.maps.DirectionsService();
    const directionsRenderer = new google.maps.DirectionsRenderer();

    map = new google.maps.Map(document.getElementById("map"), {
        // Melbounre lat and long
        center: { lat: -37.8136, lng: 144.9631 },
        zoom: 10,
    });
    infoWindow = new google.maps.InfoWindow();
    const locationButton = document.createElement("button");
    locationButton.textContent = "Pan to current location";
    locationButton.classList.add("custom-map-control-button");

    map.controls[google.maps.ControlPosition.LEFT_TOP].push(locationButton);
    //set map on init
    directionsRenderer.setMap(map);
    // call onchange function whenever start and end values change
    const onChangeHandler = function () {
        calculateAndDisplayRoute(directionsService, directionsRenderer);
    };

    //listeners for change event on the input fields
    document.getElementById("start").addEventListener("change", onChangeHandler);
    document.getElementById("end").addEventListener("change", onChangeHandler);
    locationButton.addEventListener("click",getCurrentLocation(map));

}
//Function to calculate distance between start and end
function calculateAndDisplayRoute(directionsService, directionsRenderer){
    //Set route details and settings
    directionsService.route(
        {
            origin: {
                query: document.getElementById("start").value,
            },
            destination: {
                query: document.getElementById("end").value,
            },
            travelMode: google.maps.TravelMode.DRIVING,
        },
        // check for response and status
        (response, status) => {
            if(status === "OK") {
                // set the directions
                directionsRenderer.setDirections(response);
            } else {
                window.alert("Direction request failed"+status);
            }
        }
    );
}
//Fetch current location, throw error if permission not granted
function getCurrentLocation(map){
    //Check permission
    if (navigator.geolocation){
        navigator.geolocation.getCurrentPosition(
            (position) => {
                // Current location lat & Lng
                const pos = {
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
