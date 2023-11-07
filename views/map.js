const iconBase =
  "https://developers.google.com/maps/documentation/javascript/examples/full/images/";
function myMap() {
  var mapProp = {
    center: new google.maps.LatLng(37.38283, -5.97317),
    mapId: "972c534fcb452a5e",
    zoom: 12,
  };

  var map = new google.maps.Map(document.getElementById("googleMap"), mapProp);
  new google.maps.Marker({
    position: { lat: 37.38283, lng: -5.97317 },
    map,
    icon: iconBase + "info-i_maps.png",
    title: "INFORMASION DEL MAPA",
  });
}
