var geojsonFeature = {
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {
        "location_name": "Golden Gate Park",
        "id": 1
      },
      "geometry": {
        "type": "Point",
        "coordinates": [-122.4862, 37.7694]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "location_name": "Fisherman's Wharf",
        "id": 2
      },
      "geometry": {
        "type": "Point",
        "coordinates": [-122.4177, 37.8080]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "location_name": "Boudin Baker Cafe",
        "id": 3
      },
      "geometry": {
        "type": "Point",
        "coordinates": [-122.4149, 37.8085]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "location_name": "Presidio",
        "id": 4
      },
      "geometry": {
        "type": "Point",
        "coordinates": [-122.4662, 37.7989]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "location_name": "Baker Beach",
        "id": 5
      },
      "geometry": {
        "type": "Point",
        "coordinates": [-122.4836, 37.7936]
      }
    }
  ]
}

function onEachFeature(feature, layer) {
    console.log("feature: ", feature);
    var id = parseInt(feature.properties.id)
    var place_link = "http://127.0.0.1:5000/item/" + id
    var popup_content = feature.properties.location_name + '<br> <a href="' + place_link + '">' + "See More" + '</a>'
    layer.bindPopup(popup_content);
}

$( document ).ready(function() {
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


// http://bl.ocks.org/mpmckenna8/9395643
