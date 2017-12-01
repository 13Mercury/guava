var i = 0;

var map;
var map1;
var markers = [];

var markersNew;
var all,si,adopcion,peticion;

$('#newModal').on('shown.bs.modal', function () {
  map = new google.maps.Map(document.getElementById('map1'), {
      center: { lat: 32.4966818, lng: -117.0878919 },
      zoom: 13
  });
      google.maps.event.addListener(map, 'click', function(event) {
          addMarker(event.latLng);
      });
})

function initMap() {

  all = {
      url: "/static/img/marker.svg",
      scaledSize: new google.maps.Size(50, 50)
  };

  si = {
      url: "/static/img/marker6.svg",
      scaledSize: new google.maps.Size(50, 50)
  };

  adopcion = {
      url: "/static/img/marker2.svg",
      scaledSize: new google.maps.Size(50, 50)
  };

  peticion = {
      url: "/static/img/marker3.svg",
      scaledSize: new google.maps.Size(50, 50)
  };

    map = new google.maps.Map(document.getElementById('map'), {
        center: { lat: 32.4966818, lng: -117.0878919 },
        zoom: 13
    });

    var element = document.getElementById('controlMap');
    if (typeof(element) != 'undefined' && element != null) {

            mapReload();
    }
}
// Adds a marker to the map and push to the array.
function addMarker(location) {
  if (document.getElementById("ubicacion").value != "")
    markersNew.setMap(null);

   markersNew = new google.maps.Marker({
        position: location,
        map: map,
        draggable: true,
        animation: google.maps.Animation.DROP,
        title: 'Hello World!',
        icon: all,
        page: i
    });
    document.getElementById("ubicacion").value  = location.lat() + ', ' + location.lng();

}

// Sets the map on all markers in the array.
function setMapOnAll(map) {
    for (var i = 0; i < markers.length; i++) {
        markers[i].setMap(map);
    }
}

// Removes the markers from the map, but keeps them in the array.
function clearMarkers() {
    setMapOnAll(null);
}

// Shows any markers currently in the array.
function showMarkers() {
    setMapOnAll(map);
}

// Deletes all markers in the array by removing references to them.
function deleteMarkers() {
    clearMarkers();
    markers = [];
}


function mapReload() {
  var image;
    var ul = document.getElementById('ul');
    for (var i = 0; i < ul.childElementCount; i++) {
      if (ul.children[i].className == "todas") image = all;
      else if (ul.children[i].className == "si")  image = si;
      else if (ul.children[i].className == "adopcion")  image = adopcion;
      else if (ul.children[i].className == "peticion")  image = peticion;


        var myLatLng = { lat: Number(ul.children[i].children[0].textContent.split(',')[0]), lng: Number(ul.children[i].children[0].textContent.split(',')[1]) };
        var marker = new google.maps.Marker({
            position: myLatLng,
            animation: google.maps.Animation.DROP,
            title: ul.children[i].children[2].textContent,
            icon: image,
            page:ul.children[i].children[1].textContent
        });

        markers.push(marker);
        marker.addListener('click', function() {
                document.location.href = '/areas/'+this.page;
});

    }
    setMapOnAll(map);
    var element = document.getElementById('centerMap');
    if (typeof(element) != 'undefined' && element != null) {
      var center = document.getElementById('centerMap').value;

      var myLatLng = { lat: Number(center.split(',')[0]), lng: Number(center.split(',')[1]) };

            map.setCenter(myLatLng);
    }
}

/*    marker.addListener('click', function() {
        map.setZoom(13);
        map.setCenter(marker.getPosition());
        console.log(this.page);
    });*/

//google.maps.event.addDomListener(window, "load", initMap);
