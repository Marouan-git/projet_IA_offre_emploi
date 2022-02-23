carto(data)

function carto(bdd){

    var mymap = L.map('mapid').setView([45.587788, 5.276005], 6);
  
    L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 15,
    id: 'mapbox/streets-v11',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: 'pk.eyJ1Ijoia2FtczMxIiwiYSI6ImNrd2YyamVtdTBhbGwyb3F2eDZrNWppYngifQ.iYH-fiJkiQmQ41R-w5C_uA'
}).addTo(mymap);


var markerClusters = L.markerClusterGroup();
for (var i = 0; i < data['lng'].length; i++){

  var popup = '<br/><b>Offre:</b> '+ bdd['int'][i]+
              '<br/><b>Date:</b> ' + bdd['date'][i]+
              '<br/><b><a href='+ bdd['origine'][i]+' target="_blank">Lien Offre</a>'
              '<br/><b>Description:</b> ' +bdd['desc'][i];

  if ( "Non renseigné"!= bdd['lat'][i] ) {
    var float_lat = parseFloat(bdd['lat'][i]) 
    var float_long = parseFloat(bdd['lng'][i])

}

var m = L.marker( [float_lat,float_long,])
.bindPopup(popup);
markerClusters.addLayer(m);


}
mymap.addLayer(markerClusters);
L.marker([45.587788, 5.276005]).addTo(mymap)
.bindPopup("<Adresse!</b><br />My home.");
L.circle([45.587788, 5.276005], 9000, {
  color: 'red',
  fillColor: '#f03',
  fillOpacity: 0.5
}).addTo(mymap).bindPopup("Zone.");



}
  
