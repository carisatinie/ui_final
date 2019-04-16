var places = [
  {
    "Id": 1,
    "Name": "Golden Gate Park",
    "Main Image": "https://media.cntraveler.com/photos/543d39fd00ac583c0af232fb/4:5/w_767,c_limit/golden%2520gate%2520park-17.jpg",
    "Rating": 4.8,
    "Number Ratings": "5 ratings",
    "Reviews": [
      {
        "Rating": 5,
        "Review": "Golden Gate Park is one of the most awesome places in San Francisco. It is to San Francisco the same as Central Park is to New York City. It is home to the De Young Museum and the California Academy of Science among other things. You can visit the Botanical Gardens the Aquarium of The Bay and the Conservatory of Flowers , the Japanese Tea Gardens and many other places. It's one of the most beautiful places in the City."
      },
      {
        "Rating": 5,
        "Review": "We went to the science museum in golden gate park. There are many attractions there to choose from, but the science museum is by far my favorite!! So so so much to do, see, and learn there! I love it and my kids love it. Amazing in so many ways. I cannot emphasize enough how much I LOVE this place. I would recommend this place to every person!!"
      },
      {
        "Rating": 5,
        "Review": "A public park extending for a few miles to the Pacific Ocean, with a massive art museum, science museum, arboretum, gorgeous giant trees with two highways going through the length and dozens of trails for walking, cycling.skating and rollerblading. There's a spacious Japanese garden and tea house and much more. A gorgeous metropolitan park, a jewel of San Francisco."
      },
      {
        "Rating": 5,
        "Review": "Such a great place to walk in the rain, because of all the trees and foliage. The rain was just a mist yet the gardens around the park are somewhat memorial. Great place to plan an outdoor event it seems. First time here. So big"
      },
      {
        "Rating": 4,
        "Review": "Very different from parks we are used to. We thought this would be a fairly walkable park but were definitely mistaken, it is a lot bigger than we were led to believe and there are a lot of roads throughout which made it quite hard to get fully lost and enjoy the park experience. We had also read there was plenty of places to rent bikes (around and in the park) to ride through on but this wasn’t the case either, we were half way through the park when we found a bike rental and had already decided to leave. Over all it was nice, pretty and clean but not what we were expecting at all. I would call it more of a collection of small parks or gardens with stuff in between, than an actual park."
      }
    ]
  },
  {
    "Id": 2,
    "Name": "Fisherman's Wharf",
    "Main Image": "http://fishermanswharf.org/wp-content/uploads/2018/05/shutterstock_730404997.jpg",
    "Rating": 4.33,
    "Number Ratings": "6 ratings",
    "Reviews": [
      {
        "Rating": 5,
        "Review": "Visit M-F, 8:9:30AM, to avoid tourists & have the place all to yourself. Great time to take photos of the seals, Alcatraz, and all other sights at Fisherman’s Wharf."
      },
      {
        "Rating": 3,
        "Review": "A nice area with lots going on and lots of good food. It is completely geared for tourists now but we still had an enjoyable time. Our son got a crab cake from one of the stands that he said was delicious. I much prefer this wharf to Pier 39 which is too commercial and packed full of people."
      },
      {
        "Rating": 5,
        "Review": "We enjoyed Fishermans wharf! Very cosy area, good restaurants and sealions watch at Pier 39. Bubba Gump restaurant was very good with a nice view."
      },
      {
        "Rating": 5,
        "Review": "Our hotel was only 5 minutes walk from Fishermans Wharf so we were there everyday. Lots of people just enjoying the atmosphere, taking pictures or just enjoying a bite to eat with the multitude of places to eat. Visit the famous Boudin Bakehouse there, or stroll along further to Pier 39"
      },
      {
        "Rating": 4,
        "Review": "Fisherman's Wharf is a nice area of San Francisco. Although touristy, with the several souvenir shops and restaurants, it is still a beautiful place to walk along the water with great views. The sea lions on Pier 39 are a must-see! I would definitely recommend this area if you are in San Francisco!"
      },
      {
        "Rating": 4,
        "Review": "This is a happening area; it is littered with tourists, street performers, and actual litter. It is a fairly eclectic area and offers something for everyone. There's shopping, entertainment, restaurants, street vendors, art galleries, coffee shops, etc. It is a good way to spend a few hours if you don't have anything specific on your agenda. It also has other neighboring attractions that are easily accessible from this area."
      }
    ]
  }
]

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
    var row = $("<div>", {class: "review-row"})
    var review_text = $("<span>", {class: "review-text"})
    review_text.html(review)
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
            // var db = result["itin_list"]
            // id =  db[db.length - 1]["Id"]
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
		$("#status").text("Unsuccessful – please check again!")
	}
	else {
		$("#status").text("Success! View your itinerary: ")
    $("#status").append('<a href="http://127.0.0.1:5000/itinerary">Itinerary Link</a>')
	}
}

$(document).ready(function () {
  int_id = parseInt(item_id)
  console.log("int id: ", int_id)
  db_obj = places[int_id - 1]
  console.log("db obj: ", db_obj)

  display_place(db_obj)

  $("#add_btn").on("click", function() {
    var add_obj = places[int_id - 1]
    save_item(add_obj)
  })
})
