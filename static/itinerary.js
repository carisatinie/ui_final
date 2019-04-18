function delete_item(i) {
	var data_to_save = {"idx": i}

	$.ajax({
        type: "POST",
        url: "delete_item",
        dataType : "json",
        contentType: "application/json; charset=utf-8",
        data : JSON.stringify(data_to_save),
        success: function(result){
            var all_data = result["itinerary"]
            data = all_data
            loadItineraries(itinerary)
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }
    });
}

function loadItineraries(itin) {
  $(".itinerary-container").empty()

  for (var i = 0; i < itin.length; i++) {
    var db_obj = itin[i]
    var image = db_obj["Main Image"]
    var name = db_obj["Name"]
    var rating = db_obj["Rating"]
    var num_ratings = db_obj["Number Ratings"]

    var row = $("<div>", {class: "row", id: "id-"+(i+1)})

    var img_col = $("<div>", {class: "col-md-2"})
    var content_col = $("<div>", {class: "col-md-5"})
    var edit_col = $("<div>", {class: "col-md-5"})

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

    var del_btn = $("<button>", {class: "btn", text: "X"})
    $(del_btn).on("click", {'idx': i}, function(e) {
      console.log("i: " + e.data.idx)
      // itin.splice(e.data.idx, 1)
      delete_item(e.data.idx)
      loadItineraries()
    })

    edit_col.append(del_btn)
    row.append(edit_col)

    $(".itinerary-container").append(row)
  }
}

$(document).ready(function() {
  loadItineraries()
})
