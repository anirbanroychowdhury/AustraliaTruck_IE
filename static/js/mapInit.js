// This example requires the Places library. Include the libraries=places
// parameter when you first load the API. For example:
// <script
// src="https://maps.googleapis.com/maps/api/js?key=YOUR_API_KEY&libraries=places">
let infoWindow;
let locInfoWindow;
let pos;
function initMap() {
    //Declare direction and render services
    const directionsService = new google.maps.DirectionsService();
    const directionsRenderer = new google.maps.DirectionsRenderer();
    //create a map centred on melbourne
    const map = new google.maps.Map(document.getElementById("map"), {
      mapTypeControl: false,
      zoom: 13,
    });
    //get current location
    getCurrentLocation(map);
    //create a infowindow for locate me services
    infoWindow = new google.maps.InfoWindow();
    locInfoWindow = new google.maps.InfoWindow({
        pixelOffset: new google.maps.Size(0,-50)
    });
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
    //set conditional styling
    map.data.setStyle((feature)=>{
        if (feature['i']['RESTAREATYPE'].includes('TRUCK')){
            return {icon: {url: '/static/img/icon/bed.png'}}
        }else if(feature['i']['RESTAREATYPE'].includes('WEIGHBRIDGE')){
            return {icon: {url: '/static/img/icon/highway.png'}}
        }else if(feature['i']['RESTAREATYPE'].includes('CARS ONLY')){
            return {icon: {url: '/static/img/icon/car.png'}}
        }else if(feature['i']['RESTAREATYPE'].includes('SERVICE CENTRE')){
            return {icon: {url: '/static/img/icon/service.png'}}
        }else if(feature['i']['RESTAREATYPE'].includes('AREA')){
            return {icon: {url: '/static/img/icon/camping.png'}}
        }
        return {}
    });
    //Listener to show info window on hover
    map.data.addListener('mouseover', function(event) {
        //taking required data
        restAreaName = event['feature']['i']['RESTAREANAME'];
        restAreaType = event['feature']['i']['RESTAREATYPE'];
        roadName = event['feature']['i']['DECLAREDROADNAME'];
        localityName = event['feature']['i']['LOCALITY'];
        caravanAccess = event['feature']['i']['CARAVANACCESS'];
        campingAccess = event['feature']['i']['CAMPING'];
        parkingRating = event['feature']['i']['DELINEATEDPARKING'];
        siteAmeneties = event['feature']['i']['SITEAMENITY'];
        //creating string to display required data
        const contentString = '<div id="content">'+
       ' <div id = "bodyContent">'+
       '<ol>'+
       '<li>'+'<h5>'+'Rest Area: '+restAreaName+'</h4>'+'</li>' +
       '<li>'+'<h5>'+'Rest Area Type: '+restAreaType+'</h4>'+'</li>' +
       '<li>'+'<h5>'+'Road Name: '+roadName+'</h4>'+'</li>' +
       '<li>'+'<h5>'+'Locality Name: '+localityName+'</h4>'+'</li>' +
       '<li>'+'<h5>'+'Caravan Access: '+caravanAccess+'</h4>'+'</li>' +
       '<li>'+'<h5>'+'Camping Access: '+campingAccess+'</h4>'+'</li>' +
       '<li>'+'<h5>'+'Parking Rating: '+parkingRating+'</h4>'+'</li>' +
       '<li>'+'<h5>'+'Site Ameneties Rating: '+siteAmeneties+'</h4>'+'</li>' +
       '</ol>'+
       '</div>'+
       '</div>';
       //create a invisible marker to display the inforwindow on top pff
        const marker = new google.maps.Marker({
            position: {lat: event['latLng'].lat(), lng: event['latLng'].lng()},
            map: map,
            visible: false
        });
        //set content
        locInfoWindow.setContent(contentString);
        //display
        locInfoWindow.open(map, marker);
    });
    //Get route between current location and one of the nearby rest stops on clicking
    map.data.addListener('click',function(event) {
        destinationLoc = new google.maps.LatLng(event['latLng'].lat(), event['latLng'].lng());
        startLoc = new google.maps.LatLng(pos['lat'], pos['lng']);
        route(directionsService, directionsRenderer, startLoc, destinationLoc)
    });
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

