// Store our API endpoint inside queryUrl
var queryUrl = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson";

function getColor(mag) {
    return mag <= 1 ? '#BFED3D' :
           mag <= 2 ? '#FFD800' :
           mag <= 3 ? '#F4C72A' :
           mag <= 4 ? '#FFA222' :
           mag <= 5 ? '#F76017' :
                   '#DC3E10';
};

function getOptions(mag) {
  var geojsonMarkerOptions = {
    radius: mag * 5,
    fillColor: getColor(mag),
    color: "#666",
    weight: 1,
    opacity: 1,
    fillOpacity: 0.8
  }

  return geojsonMarkerOptions
};

// Perform a GET request to the query URL
d3.json(queryUrl, function(data) {
  // Once we get a response, send the data.features object to the createFeatures function
  createMap(data.features);
});

function onEachFeature(feature, layer) {
    layer.bindPopup("<h3>" + feature.properties.place +
    "</h3><hr><p>" + new Date(feature.properties.time) + "</p>");
};

function createMap(earthquakeData) {
  var myMap = L.map("map", {
    center: [
      37.09, -95.71
    ],
    zoom: 5
  });
    
  var streetmap = L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
    attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
    maxZoom: 18,
    id: "mapbox.streets",
    accessToken: API_KEY
  }).addTo(myMap);

  L.geoJSON(earthquakeData, {
    onEachFeature: onEachFeature,
    pointToLayer: function (feature, latlng) {
      return L.circleMarker(latlng, getOptions(feature.properties.mag));
    }
  }).addTo(myMap);

  var legend = L.control({position: 'bottomright'});

  legend.onAdd = function (map) {
    var div = L.DomUtil.create('div', 'info legend'),
      mags = [0, 1, 2, 3, 4, 5],
      labels = [];

      // loop through our density intervals and generate a label with a colored square for each interval
      for (var i = 0; i < mags.length; i++) {
        div.innerHTML +=
            '<i style="background:' + getColor(mags[i] + 1) + '"></i> ' +
            mags[i] + (mags[i + 1] ? '&ndash;' + mags[i + 1] + '<br>' : '+');
      }

      return div;
    };

    legend.addTo(myMap);
};
