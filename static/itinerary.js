$(document).ready(function() {
  for (var i = 0; i < itinerary.length; i++) {
    var db_obj = itinerary[i]
    console.log(db_obj)
    var image = db_obj["Main Image"]
    var name = db_obj["Name"]
    var rating = db_obj["Rating"]
    var num_ratings = db_obj["Number Ratings"]

    var row = $("<div>", {class: "row"})

    var img_col = $("<div>", {class: "col-md-2"})
    var content_col = $("<div>", {class: "col-md-10"})

    var img_tag = '<img class="place-img" src="' + image + '">'
    img_col.append(img_tag)
    row.append(img_col)

    var name_span = $("<span>", {class: "name-txt"})
    name_span.html(name)
    content_col.append(name_span)

    content_col.append("<br>")

    var rating_span = $("<span>", {class: "rating-txt"})
    rating_span.html(rating)
    content_col.append(rating_span)

    content_col.append("<br>")

    var num_rating_span = $("<span>", {class: "num-rating-txt"})
    num_rating_span.html(num_ratings)
    content_col.append(num_rating_span)

    row.append(content_col)

    $("#itinerary-container").append(row)
  }
})
