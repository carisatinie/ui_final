function create_place(name, img_link, rating, review) {
  // Add ID in ajax
  obj = {}
  obj["Name"] = name
  obj["Main Image"] = img_link
  obj["Rating"] = rating
  obj["Number Ratings"] = "1 rating"

  review_list = []
  review_obj = {}
  review_obj["Rating"] = rating
  review_obj["Review"] = review
  review_list.push(review_obj)

  obj["Reviews"] = review_list

  return obj
}

function create_geojson(name, longitude, latitude) {
  // Add ID in ajax
  obj = {}
  obj["type"] = "Feature"

  properties_obj = {}
  properties_obj["location_name"] = name
  obj["properties"] = properties_obj

  geometry_obj = {}
  geometry_obj["type"] = "Point"
  geometry_obj["coordinates"] = [longitude, latitude]
  obj["geometry"] = geometry_obj

  return obj
}

function add_item(place, geojson) {
	$.ajax({
        type: "POST",
        url: "add_item",
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify({'place': place, 'geojson': geojson}),
        success: function(result){
            console.log("Success")
            location.href = 'http://127.0.0.1:5000/'
        },
        error: function(request, status, error){
            console.log("Error: duplicate location name?");
            console.log(request)
            console.log(status)
            console.log(error)
            $("#error-div").text("Error: Did you try adding a duplicate location?")
        }
    });

}

$(document).ready(function() {
  var map = L.map('mapid', {
    center: [37.7649, -122.431297],
    zoom: 13
  });

  var layer = new L.TileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png');
  map.addLayer(layer);

  var lat_num = 0;
  var lng_num = 0;

  map.on('click', function(e){
    var coord = e.latlng.toString().split(',');
		var lat = coord[0].split('(');
	  var lng = coord[1].split(')');
    $("#coordinates").text(lat[1] + ", " + lng[0])
  });

  $("#submit-btn").click(function (e) {
    e.preventDefault()
    var name = $("#name").val()
    var img_link = $("#imglink").val()
    var coordinates = $("#coordinates").html()
    div = coordinates.indexOf(",")
    var latitude = parseFloat(coordinates.slice(0,div))
    var longitude = parseFloat(coordinates.slice(div+2, coordinates.length))
    var rating = parseInt($("#rating").val())
    var review = $("#review").val()

    places_obj = create_place(name, img_link, rating, review)
    geojson_obj = create_geojson(name, longitude, latitude)

    add_item(places_obj, geojson_obj)
  })
})
