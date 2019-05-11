function display_place(db_obj) {
  var name = db_obj["Name"]
  var img_tag = '<img id="place-img" src="' + db_obj["Main Image"] + '">'
  var rating = parseFloat(db_obj["Rating"])
  var num_ratings = db_obj["Number Ratings"]
  var review_obj = db_obj["Reviews"]

  $("#name-div").append(name)
  $("#main-img-div").append(img_tag)
  $("#rating-div").append(rating)
  $("#num-rating-div").append(num_ratings)

  for (var i = 0; i < db_obj["Reviews"].length; i++) {
    var review = db_obj["Reviews"][i]["Review"]
    var review_rating = db_obj["Reviews"][i]["Rating"]

    var row = $("<div>", {class: "review-row"})
    var rating_text = $("<span>", {class: "rating-text"})
    rating_text.html("Rating: " + review_rating + "/5")
    var review_text = $("<span>", {class: "review-text"})
    review_text.html(review)
    row.append(rating_text)
    row.append("<br>")
    row.append(review_text)
    $("#reviews-container").append(row)
  }
}

var save_item = function(location){
	var data_to_save = location

	$.ajax({
        type: "POST",
        url: "item",
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(data_to_save),
        success: function(result){
            add_item_status(1)
        },
        error: function(request, status, error){
            add_item_status(0)
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

var add_item_status = function(status_bool){
	if (!status_bool) {
		$("#status").text("Unsuccessful – please check for duplicates!")
	}
	else {
    $("#status").append('<a href="http://127.0.0.1:5000/itinerary">Updated Itinerary!</a>')
	}
}

$(document).ready(function () {
  int_id = parseInt(item_id)
  db_obj = places[int_id - 1]

  display_place(db_obj)

  $("#add_btn").on("click", function() {
    var add_obj = places[int_id - 1]
    save_item(add_obj)
  })
})
