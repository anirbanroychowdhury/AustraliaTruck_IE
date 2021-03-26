let map;
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
    //set map on init
    directionsRenderer.setMap(map)
    // call onchange function whenever start and end values change
    const onChangeHandler = function () {
        calculateAndDisplayRoute(directionsService, directionsRenderer);
    }
    //listeners for change event on the input fields
    document.getElementById("start").addEventListener("change", onChangeHandler);
    document.getElementById("end").addEventListener("change", onChangeHandler);

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