var geojsonFeature = {
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {
        "location_name": "Golden Gate Park"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [-122.4862, 37.7694]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "location_name": "Fisherman's Wharf"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [-122.4177, 37.8080]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "location_name": "Boudin Baker Cafe"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [-122.4149, 37.8085]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "location_name": "Presidio"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [-122.4662, 37.7989]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "location_name": "Baker Beach"
      },
      "geometry": {
        "type": "Point",
        "coordinates": [-122.4836, 37.7936]
      }
    }
  ]
}

function onMapClick(latlng, map, name) {
	console.log("latlng: ", latlng)
	console.log("location_name: ", name)
	var popup = L.popup()
    .setLatLng(latlng)
    .setContent('<p>Golden Gate Park</p><p>See more </p>')
    .openOn(map);
}

function onEachFeature(feature, layer) {
    console.log("feature: ", feature);
    layer.bindPopup(feature.properties.location_name);
}

$( document ).ready(function() {
	// markers = [[37.7694, -122.4862], [37.8080, -122.4177], [37.8085, -122.4149], [37.7989, -122.4662], [37.7936, -122.4836]]
 //    names = ["Golden Gate Park", "Fisherman's Wharf", "Boudin Baker Cafe", "Presdio", "Baker Beach"]
    var map = L.map('mapid', {
	    center: [37.7649, -122.431297],
	    zoom: 13
	});

	var layer = new L.TileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png');
	map.addLayer(layer);

	L.geoJSON(geojsonFeature, {
		pointToLayer: function(feature, latlng) {
	        console.log(latlng, feature);
	        return L.marker(latlng);
	    },
	    onEachFeature: onEachFeature
	}).addTo(map);

});