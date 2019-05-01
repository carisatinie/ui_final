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
            // add_item_status(1)
            console.log("success")
        },
        error: function(request, status, error){
            // add_item_status(0)
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });

}

$(document).ready(function() {
  $("#submit-btn").click(function (e) {
    e.preventDefault()
    var name = $("#name").val()
    var img_link = $("#imglink").val()
    var longitude = parseFloat($("#longitude").val())
    var latitude = parseFloat($("#latitude").val())
    var rating = parseInt($("#rating").val())
    var review = $("#review").val()

    places_obj = create_place(name, img_link, rating, review)
    geojson_obj = create_geojson(name, longitude, latitude)

    add_item(places_obj, geojson_obj)

    console.log("before")
    location.href = 'http://127.0.0.1:5000/'
    console.log("after")
  })
})
