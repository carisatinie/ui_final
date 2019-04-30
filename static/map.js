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
        "location_name": "Boudin Sourdough Bakery & Cafe",
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
    },
    {
      "type": "Feature",
      "properties": {
        "location_name": "Chinatown",
        "id": 6
      },
      "geometry": {
        "type": "Point",
        "coordinates": [-122.4078, 37.7941]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "location_name": "Legion of Honor",
        "id": 7
      },
      "geometry": {
        "type": "Point",
        "coordinates": [-122.5008, 37.7845]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "location_name": "Coit Tower",
        "id": 8
      },
      "geometry": {
        "type": "Point",
        "coordinates": [-122.4058, 37.8024]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "location_name": "PIER 39",
        "id": 9
      },
      "geometry": {
        "type": "Point",
        "coordinates": [-122.4098, 37.8087]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "location_name": "Union Square",
        "id": 10
      },
      "geometry": {
        "type": "Point",
        "coordinates": [-122.4075, 37.7880]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "location_name": "San Francisco City Hall",
        "id": 11
      },
      "geometry": {
        "type": "Point",
        "coordinates": [-122.4193, 37.7793]
      }
    }
  ]
}

function addPopupContent(feature) {
  var id = parseInt(feature.properties.id)

  var name_txt = $("<span>", {class: "name_text", text: feature.properties.location_name})
  var place_link = "http://127.0.0.1:5000/item/" + id
  var seemore_link = '<br> <a class="more_link" href="' + place_link + '">' + "More" + '</a>'
  var add_btn = $("<button>", {class: "add_btn light_green", text: "Add"})

  $(add_btn).mouseover(function() {
    $(add_btn).removeClass("light_green")
    $(add_btn).addClass("dark_green")
    $(add_btn).css( 'cursor', 'pointer' );
  })

  $(add_btn).mouseout(function() {
    $(add_btn).removeClass("dark_green")
    $(add_btn).addClass("light_green")
  })

  var popup_div = $("<div>")
  popup_div.append(name_txt)
  popup_div.append(seemore_link)
  popup_div.append(add_btn)

  $(add_btn).on("click", function() {
    var add_obj = places[id - 1]

    save_item(add_obj, function(result) {
      if (result == 0) { // error
        popup_div.empty()
        var err_text = $("<span>", {class: "err_text", text: "Something went wrong... couldn't add :/ "})
        popup_div.append(err_text)
        setTimeout(function(){
          popup_div.empty()
          popup_div.append(name_txt)
          popup_div.append(seemore_link)
          popup_div.append(add_btn)
          location.reload()
        }, 1000);
      }
      else { // success
        popup_div.empty()
        var success_text = $("<span>", {class: "success_text", text: "Successfully added to itinerary!"})
        popup_div.append(success_text)
        setTimeout(function(){
          popup_div.empty()
          popup_div.append(name_txt)
          popup_div.append(seemore_link)
          popup_div.append(add_btn)
          location.reload()
        }, 1000);
      }
    })
  })

  return popup_div
}

function onEachFeature(feature, layer) {
    popup_div = addPopupContent(feature)

    layer.bindPopup(popup_div[0]);
}

var save_item = function(location, callback){
	var data_to_save = location
	$.ajax({
        type: "POST",
        url: "/",
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(data_to_save),
        success: function(result){
            callback(1)
        },
        error: function(request, status, error){
            callback(0)
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
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
