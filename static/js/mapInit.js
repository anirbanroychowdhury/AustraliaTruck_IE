// This example requires the Places library. Include the libraries=places
// parameter when you first load the API. For example:
// <script
// src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=places">
let infoWindow;
function initMap() {
    //create a map centred on melbourne
    const map = new google.maps.Map(document.getElementById("map"), {
      mapTypeControl: false,
      center: { lat: -37.8136, lng: 144.9631 },
      zoom: 13,
    });
    //create a infowindow for locate me services
    infoWindow = new google.maps.InfoWindow()
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
        getCurrentLocation(map)
    }
    //Add listener
    locationButton.addEventListener("click",onLocationChangeHandler);
    //Create a new autocomplete handler
    new AutocompleteDirectionsHandler(map);
  }
  
  //Class for auto complete direction handlers
  class AutocompleteDirectionsHandler {
    //PARAM: map; Google Map Type
    //Creates a map with autocomplete suggestions
    constructor(map) {
        //Set initial values.
        //Map to be shown
        this.map = map;
        //Origin ID
        this.originPlaceId = "";
        //Destination ID
        this.destinationPlaceId = "";
        //Define travel mode
        this.travelMode = google.maps.TravelMode.DRIVING;
        //Declare direction and render services
        this.directionsService = new google.maps.DirectionsService();
        this.directionsRenderer = new google.maps.DirectionsRenderer();
        //set the direction renderer on the map
        this.directionsRenderer.setMap(map);
        //Get origin input
        const originInput = document.getElementById("origin-input");
        //Get destination input
        const destinationInput = document.getElementById("destination-input");
        //Set autocomplete on origin
        const originAutocomplete = new google.maps.places.Autocomplete(originInput);
        //Specify just the place data fields that you need.
        originAutocomplete.setFields(["place_id"]);
        //Set autocomplete for destination
        const destinationAutocomplete = new google.maps.places.Autocomplete(destinationInput);
        // Specify just the place data fields that you need.
        destinationAutocomplete.setFields(["place_id"]);
        //Setting up  listeners
        this.setupPlaceChangedListener(originAutocomplete, "ORIG");
        this.setupPlaceChangedListener(destinationAutocomplete, "DEST");
        //Setting search boxes to top left.
        this.map.controls[google.maps.ControlPosition.TOP_LEFT].push(originInput);
        this.map.controls[google.maps.ControlPosition.TOP_LEFT].push(destinationInput);
        }
        //PARAM:autocomplete obj, origin or destination mode
        //Function to setup listeners to the text fields
        setupPlaceChangedListener(autocomplete, mode) {
        //bind the autocomplete to this map
        autocomplete.bindTo("bounds", this.map);
        //add a listener for autocomplete
        autocomplete.addListener("place_changed", () => {
            //Get the place suggested by auto complete
            const place = autocomplete.getPlace();

                if (!place.place_id) {
                    window.alert("Please select an option from the dropdown list.");
                    return;
                }
                //check if autocomplete is on origion or destination text box
                if (mode === "ORIG") {
                    //set on origion text box
                    this.originPlaceId = place.place_id;
                } else {
                    //set on destination text box
                    this.destinationPlaceId = place.place_id;
                }
                //call the route function when change is detected
                this.route();
            });
        }
        //Function to map and display the route on the map
        route() {
            //Check if both the origin and destination is in place, if not return
            if (!this.originPlaceId || !this.destinationPlaceId) {
                return;
            }
            const me = this;
            // Call the route function
            this.directionsService.route(
                {
                    //set required inputs
                    origin: { placeId: this.originPlaceId },
                    destination: { placeId: this.destinationPlaceId },
                    travelMode: this.travelMode,
                },
                //Checkf for the response
                (response, status) => {
                    //if status ok
                    if (status === "OK") {
                        //Render the route received
                        me.directionsRenderer.setDirections(response);
                    } else {
                        //Displa alert
                        window.alert("Directions request failed due to " + status);
                    }
                }
            );
        }   
  }

//PARAM: map object
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