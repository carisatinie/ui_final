var order_global

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
            console.log("DATA: " + data)
            loadItineraries(data)
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

	if (itin.length == 0) {

		var newlines = "<br><br><br><br><br><br>"
		var text = $("<span>", {id: "status_text", text: "Your itinerary is empty!"})
		var map_link = "<br> <a id='maplink' href='http://127.0.0.1:5000/'>Add some from the map.</a>"
		$("#status").append(newlines)
		$("#status").append(text)
		$("#status").append(map_link)
	}

  $("#sortable").empty()

  for (var i = 0; i < itin.length; i++) {
    var db_obj = itin[i]
    var image = db_obj["Main Image"]
    var name = db_obj["Name"]
    var rating = db_obj["Rating"]
    var num_ratings = db_obj["Number Ratings"]

    var li_el = $("<li>", {class: "ui-state-default place_hover", id: name})

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
		var rating_total = $("<span>")
    rating_span.html(rating)
		rating_total.html(" out of 5")
    content_col.append(rating_span)
		content_col.append(rating_total)

    content_col.append("<br>")

    var num_rating_span = $("<span>", {class: "num-rating-txt"})
    num_rating_span.html(num_ratings)
    content_col.append(num_rating_span)

    row.append(content_col)

    var del_btn = $("<button>", {class: "btn", id: "del-btn", text: "X"})
    $(del_btn).on("click", {'idx': db_obj["Id"]}, function(e) {
      console.log("i: " + e.data.idx)
      delete_item(e.data.idx)
    })

    edit_col.append(del_btn)
    row.append(edit_col)

    $(li_el).append(row)
    $("#sortable").append(li_el)
  }
}

function save_shuffle() {
  $( "#sortable" ).sortable({
    update: function() {
      var order = $("#sortable").sortable("toArray");
      var order_global = order

      var data_to_save = {"order": order_global}
      $.ajax({
            type: "POST",
            url: "shuffle_itinerary",
            dataType : "json",
            contentType: "application/json; charset=utf-8",
            data : JSON.stringify(data_to_save),
            success: function(result){
                var all_data = result["itinerary"]
                data = all_data
            },
            error: function(request, status, error){
                console.log("Error");
                console.log(request)
                console.log(status)
                console.log(error)
            }
        });
    }
  })
  $( "#sortable" ).disableSelection()
}

$(document).ready(function() {
  save_shuffle()
  loadItineraries(itinerary)
})
