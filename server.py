import sys
from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
import json
app = Flask(__name__)

itin_list = []

places = [
  {
    "Id": 1,
    "Name": "Golden Gate Park",
    "Main Image": "https://25va3qc1hw-flywheel.netdna-ssl.com/wp-content/uploads/2011/03/Conservatory-Of-Flowers-San-Francisco-1280x640.jpg",
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
  },
  {
    "Id": 3,
    "Name": "Boudin Sourdough Bakery & Cafe",
    "Main Image": "https://media-cdn.tripadvisor.com/media/photo-s/05/19/77/b7/boudin-sourdough-bakery.jpg",
    "Rating": 4.5,
    "Number Ratings": "8 ratings",
    "Reviews": [
      {
        "Rating": 5,
        "Review": "Spent a lot of time wandering around this huge bakery. Lots of things to buy as well as souvenirs. Loved seeing the bread in the shape of the animals like turtles, teddy bears, aligators etc"
      },
      {
        "Rating": 3,
        "Review": "Having arrived in SF from the airport, we stopped in here earlier as it was a little too early to check into our hotel. The service was very slow; they served someone behind us first (the other customer didn’t push in). The coffee was OK, the pastry OK but nothing to write home about. And - worst of all - no restrooms. We won’t be dropping in here again."
      },
      {
        "Rating": 5,
        "Review": "Always stop in here for breakfast when I visit San Francisco, the food is great, the atmosphere great, and the hot chocolates are amazing... but it is all about the bread and you can’t beat the breakfast of scrambled eggs and bacon served in a sour dough roll! Super tasty and fun! The staff are friendly, there is plenty to see in the shop, and the bread is worth it!"
      },
      {
        "Rating": 5,
        "Review": "We came twice to do the self guided bread factory tour. You pass through a small \"museum\" and then on to the balcony where you can overlook the workers making bread and read placards to educate yourself on the process. We saw the mixing, the dumping of the dough, the cutting and shaping and handling of the dough, and then it was brought to the bread rising area before baking. Fascinating to watch!"
      },
      {
        "Rating": 5,
        "Review": "The upstairs restaurant is more fancy than below and I think that some do not realize it's up there! It is DELICIOUS. My daughter had the obligatory chowder bread bowl. She LOVED it and she doesn't like soup!!! I had the Crab Louis Salad and it was ABSOLUTELY DELICIOUS. Fresh and so yum. The view of Fishermans wharf & the harbor area is just stunning. SO fun and well worth the extra money."
      },
      {
        "Rating": 4,
        "Review": "Everytime we come to SF we have to stop at the Wharf and get a bread bowl with clam chowder. My daughter demands it and I don't mind meeting that demand since it is very good. You can get more of the bread and just eat that. The only thing I wish was that I could pack up the smell of the baking bread to take home (fewer carbs ;-) )"
      },
      {
        "Rating": 4,
        "Review": "As with the name, it is obvious that this place sells sourdough, but it is THE place to get sourdough in SF. Before going on a bay cruise, I had some time to walk down to Boudin’s to get fresh sourdough to take home. They have workers in the front window making the bread and you can watch them knead and shape the dough. Inside the cafe, the nice gentleman at the bread counter helped me pick out the best loaves for taking home with me. I got a 1/2 pound loaf, an Asiago loaf and a small turtle. The Asiago loaf is actually individual rolls all together so it made for easy eating and the small loaf was easy to cut and tasted great. Good choice."
      },
      {
        "Rating": 5,
        "Review": "Wonderful sourdough that fresh from the oven clamchowder and fresh seafood. “We love it” recommend clam-chowder, Bake Spinach, fried calamari and french onion soup."
      }
    ]
  },
  {
    "Id": 4,
    "Name": "Presidio",
    "Main Image": "https://img1.10bestmedia.com/Images/Photos/190887/p-presidio_54_990x660_201404231528.jpg",
    "Rating": 4.6,
    "Number Ratings": "5 ratings",
    "Reviews": [
      {
        "Rating": 5,
        "Review": "Beautiful trails and abundant natural habitat make this an ideal antidote for any urban overload. Possible wild parrot sighting and astonishing views of the SF Bay and wild Pacific Ocean."
      },
      {
        "Rating": 5,
        "Review": "Very beautiful! We got here early and there was plenty of parking. We enjoyed the Disney Family Museum and walking around taking in the beautiful historic buildings."
      },
      {
        "Rating": 4,
        "Review": "The Presidio in San Francisco was a previous Army post that closed in 1994 and was transferred over to the National Park Service. Since then it’s been converted into a massive living and recreational area. It’s essentially a very large park now with hiking trials, rental housing, museums, a fitness center, a camp ground, beaches, a golf course, a cemetery and so much more. The coastal hiking trails above Baker beach heading towards the Golden Gate Bridge and down in Crissy Field offer some of the best views in the entire bay area. The Presidio is a great place to bike as well and will need to go through it to be able to bike across the Golden Gate Bridge. Things get quite busy on the weekends or events such as Fleet Week and the Blue Angels events in October. The Presidio is definitely worth a visit when in San Francisco."
      },
      {
        "Rating": 4,
        "Review": "Beautiful part of the city. Originally sand dunes, it is incredibly beautiful now. Views of the Golden Gate bridge, Alcatraz and the bay are fantastic. However, dress up well as there is a cold wind normally in this area."
      },
      {
        "Rating": 5,
        "Review": "Lovely place to go for a leisurely hike with family, friends, dogs or on your own. Sun filters through trees and dogs love the freedom. Never very crowded. Children’s park. There are restaurants down below at bottom of park in old Army buildings."
      }
    ]
  },
  {
    "Id": 5,
    "Name": "Baker Beach",
    "Main Image": "https://www.californiabeaches.com/wp-content/uploads/2014/09/bigstock-Baker-Beach-San-Francisco-Large-1000x644.jpg",
    "Rating": 4.43,
    "Number Ratings": "7 ratings",
    "Reviews": [
      {
        "Rating": 4,
        "Review": "Parking was scarce. The beach was not overly crowded, but the parking was a little scarce. Looks like a local favorite. Great place for some photos and to put your toes in the sand or ocean."
      },
      {
        "Rating": 4,
        "Review": "I don’t know that it’s likely you’ll spend too much time here, but a leg stretch while you head down to the water, feel the sand between your toes and get that great photo of the Golden Gate Bridge makes this a nice stop if you are in the area."
      },
      {
        "Rating": 5,
        "Review": "This was a fantastic place for viewing the Golden Gate Bridge. There is a nice parking lot and boardwalk down to the beach. This spot, in my opnion offers one of the best picture spots in the city."
      },
      {
        "Rating": 4,
        "Review": "We were walking through the Presidio and stopped at Baker Beach to get a view of The Golden Gate Bridge. Beautiful big beach with plenty of space for spending the day and enjoying the landscape."
      },
      {
        "Rating": 5,
        "Review": "We come here often to walk our dog. Each time is different. The last time we went, there was a couple wearing their having a photo shoot for their wedding. There were all sorts of folks enjoying the area, some of which even went into the water. The most surprising was the sighting of approximately 5 dolphins... It was just beautiful. And of course, the view of the Golden Gate Bridge. Just a bit of caution to some as there can be some nudist folks towards the farther end of the beach."
      },
      {
        "Rating": 5,
        "Review": "Not a photo, but a postcard. Ideal place to get pictures of The Golden Gate bridge from every angle you may wish. If you have time, and of course the day is clear, wait for the sunset. The view of the bridge is impressive with the falling of the sun. You can go by bus which stops just in front of the bridge."
      },
      {
        "Rating": 4,
        "Review": "This big beach is outside the Bay and therefore exposed to lots of fog and ocean-caused weather. Still it's a huge beautiful beach, great for a long walk, but bundle up for cold weather!"
      }
    ]
  },
  {
    "Id": 6,
    "Name": "Chinatown",
    "Main Image": "https://media.timeout.com/images/102875459/630/472/image.jpg",
    "Rating": 4.57,
    "Number Ratings": "7 ratings",
    "Reviews": [
      {
        "Rating": 5,
        "Review": "Love coming to Chinatown. The one here in San Francisco is one of the largest and oldest in the United States. Founded in 1848, destroyed in the 1906 fire, and then rebuilt. It is filled with shops with items you might not find elsewhere. At a corner market I even found Durian Fruit....not an item you'll ever find at Safeway. We made sure we visited a couple foot massage spots....we were spoiled when we lived in SE Asia and there is nothing quite relaxing as a nice foot massage. Best to just wander about and discover."
      },
      {
        "Rating": 5,
        "Review": "There are two different areas of Chinatown. One is on Grant and it is definitely a tourist area. Good food and fun shops. But if you want the real Chinatown experience then go to the northern end of Chinatown-Stockton/Pacific/Broadway area. That is where the really interesting stuff is. We saw the neatest stores, tried some super interesting foods (most of which we have no idea what it was because nothing is written in English and the employees don't speak English well). That area was much more interesting and fun to visit."
      },
      {
        "Rating": 4,
        "Review": "I was lucky and stumbled upon a fortune cookie factory in an alley, some old bank buildings in traditional style, and a park in which locals were doing tai chi. Strong smells and crowds in busy locations."
      },
      {
        "Rating": 4,
        "Review": "Is it a tourist trap on Grant Ave? Yes, do I mind no not really as the food and prices for their tourist items were so delcious and well marked it was well worth the trip! My favorite was just turning into little side streets and finding different murals along the walls, strolling the streets with some potstickers or ice cream rolls in your hand was quite a fun afternoon. (For sure a daytime experience as at night the atmosphere changes drastically)"
      },
      {
        "Rating": 5,
        "Review": "We managed to take a tour of the place on a whim and were blown away! The place is huge, with hundreds of shops to buy souvenirs, plus markets selling foodstuffs (and other things!!) that I hadn't even heard of before. Managed to get samples of many eastern dishes and now plan to make them at home myself, what a great experience."
      },
      {
        "Rating": 5,
        "Review": "I've visited many Chinatowns in many cities, but this is the original one and you will be pleased with the shopping, eating, people-watching and atmosphere. We walked all over, popping in and out of shops. We walked down little alleys and got a taste of life there. There was a fair amount of art/murals that I fell in love with too!"
      },
      {
        "Rating": 4,
        "Review": "Chinatown in SF is popular the most famous one in all of the US. I walked through it multiple times on my trip to SF and I felt like a minority while I was there. All the signs are in English and Chinese (a few may have been just in Chinese). They had fruit stands, dried fish and lots of other fresh goods. It reminded me a lot of my visits to China but just a little something was missing. Fun place to wander around."
      }
    ]
  },
  {
    "Id": 7,
    "Name": "Legion of Honor",
    "Main Image": "https://legionofhonor.famsf.org/sites/default/files/styles/collections640x480/public/nav-highlights/lh_visit_top_right.jpg?itok=HLwki_8j",
    "Rating": 4.83,
    "Number Ratings": "6 ratings",
    "Reviews": [
      {
        "Rating": 5,
        "Review": "The views alone from the exterior of this museum are worth the visit! Then inside- treasures of art from all centuries & world-wide countries, all in an atmosphere reminiscent of a museum in Paris! Not to be missed!"
      },
      {
        "Rating": 5,
        "Review": "We came by for the Rubens exhibit and got right in. I always like to stop by the Rodin sculptures at the entry plaza (The Thinker) and in the gallery. This fine museum looks and acts like a world class museum. Get the membership-it pays for itself with a couple of visits"
      },
      {
        "Rating": 4,
        "Review": "This museum has a good blend of classical and contemporary art compared to the others in San Francisco. There are also special exhibits featuring artists during some months."
      },
      {
        "Rating": 5,
        "Review": "We arrived at this wonderful museum less than half and hour before closing and they let up in for free. Usually $15. What a great display of art and sculptures and such. We were amazed. This building is very unique and quite the structure. The outside grounds are fun to walk and the view of the Golden Gate Bridge is wonderful. Must see if you are in the area."
      },
      {
        "Rating": 5,
        "Review": "If you come here for a special exhibit, parking will be a challenge but it'll be worth it. If you go in the afternoon, stay for the organ concert! The pipe organ is four manuals and it lasts between 30-45 minutes. If you've been walking around the museum for any length of time, sitting for the concert will be a nice rest. It's on a hill with beautiful views of the GG Bridge, there's also a piece of artwork outside to commemorate the holocaust, that is a must see, if anything to be sure we don't forget. As it's in San Francisco, wear layers!"
      },
      {
        "Rating": 5,
        "Review": "It’s worth the effort to travel to this gallery. A bus (fares payable on board) runs from the San Francisco CBD to a stop within easy walking distance of the entrance to the gallery. The building and the location itself, set high over the bay with views to the Golden Gate bridge, are worth the trip on their own. The collection is a delight, ranging from Egyptian artefacts through to the works of impressionist artists. The café is excellent."
      }
    ]
  },
  {
    "Id": 8,
    "Name": "Coit Tower",
    "Main Image": "https://www.tripsavvy.com/thmb/7mvBRfo0sDL3LZCB0O2qCbS1O8U=/960x0/filters:no_upscale():max_bytes(150000):strip_icc()/20100425_012-1000x1500-56a387c45f9b58b7d0d2744a.jpg",
    "Rating": 4.67,
    "Number Ratings": "3 ratings",
    "Reviews": [
      {
        "Rating": 5,
        "Reviews": "We went on a Saturday afternoon and the wait was about 20 minutes to go up the tower. $9 entrance for adults. The view was definitely worth it - got to see San Francisco from all angles. We stayed there for about 30 min but you can stay as long as you want in the tower. There's parking at the tower but I would recommend walking to the tower if possible because the view on the walk is wonderful"
      },
      {
        "Rating": 5,
        "Review": "There is very limited parking, so I would plan ahead.  You can walk to it from Little Italy or the hillside facing the Piers, but it is a hefty hike.  Even though a bit of a hike to take on, it is very enjoyable and worth it for the experience.  For those who may have health issues, I would say to not even attempt it. Avoid the weekends, because it is busier then.  Not sure what times of day is best, but we went after lunch and it was a bit busy, but manageable.  You might have to wait a little for the elevator ride due to the age and capacity of the lift, but it moves right along."
      },
      {
        "Rating": 4,
        "Review": "Enjoyed the views from the top of Coit Tower in San Francisco.  A little pricey at $9 to go the top of this old small scale tower.  Great pictures of entire city, however so not too bad"
      }
    ]
  },
  {
    "Id": 9,
    "Name": "PIER 39",
    "Main Image": "https://media-cdn.tripadvisor.com/media/photo-s/06/4a/17/02/pier-39.jpg",
    "Rating": 4.5,
    "Number Ratings": "4 ratings",
    "Reviews": [
      {
        "Rating": 4,
        "Review": "A must see place...at least once. Having grown up in SF but having not been back in a while I was surprised at the changes. I guess I miss it when it was a bit more quaint. However, the stores were fun and of course, you can't miss the amazing sea lions. It was a nice stroll. We stopped in one of the restaurants for really yummy garlic bread on sourdough and good cocktails."
      },
      {
        "Rating": 5,
        "Review": "Best hangout places in San Francisco. Visited multiple times with friends and family. Everyone loves it. Great souvenir shops all along the pier. "
      },
      {
        "Rating": 4,
        "Review": "Great place to spend few hours while in San Francisco. Loads to do and visit, one of the biggest attraction is the sea lions which was fun and different experience. Plenty of dining options and shops with some interesting things at sale. This pier have fantastic views to Golden Gate Bridge and bay bridge. There is always some live music being played which is fun and entertaining."
      },
      {
        "Rating": 5,
        "Review": "A must visit place in Fisherman’s Wharf. The view is breathtaking. A very good time spent here. There are lots of places nearby for shopping, food and entertainment. If you want to have a good seafood then this place is perfect for you. Will definitely visit this place again. Overall a very good and memorable experience."
      }
    ]
  },
  {
    "Id": 10,
    "Name": "Union Square",
    "Main Image": "https://www.tripsavvy.com/thmb/fqIAjZaVUoY6GQ8sA3WBgVTksTg=/960x0/filters:no_upscale():max_bytes(150000):strip_icc()/GettyImages-109287627-5b66fb4f46e0fb0050fabc66.jpg",
    "Rating": 3.8,
    "Number Ratings": "5 ratings",
    "Reviews": [
      {
        "Rating": 3,
        "Review": "Nothing special, an average square. High end shops all around it. There were quite a few homeless hanging out in the square."
      },
      {
        "Rating": 3,
        "Review": "Used to be my favourite part of San Francisco, I'd stay here and wander around just soaking up the heart of the city. Today, it feels more like a concrete jungle; it's not that big and has little emotional appeal."
      },
      {
        "Rating": 5,
        "Review": "Union Square was a shopping heaven with lots of brands, shops, restaurants, and not-to-be-missed: the famous cable car station at the corner of Market St. and Hyde St."
      },
      {
        "Rating": 4,
        "Review": "The Union Square area is where all the high-end shops appear to be in SF (they had a Burberry and a Harry Winston within a couple blocks of it other. There is an actual square there which the shops are all centered around. In the middle of the Square is a monument dedicated to Admiral Dewey and his victory at the Battle of Manila Bay. So go to shop or go to enjoy the lovely square."
      },
      {
        "Rating": 4,
        "Review": "This is a great place to spend an afternoon with kids ice skating. There is a cafe with cute bistro tables to get sandwiches, pastries and drinks right at Union Square! The gigantic holiday tree is a big hit with the kids."
      }
    ]
  },
  {
    "Id": 11,
    "Name": "San Francisco City Hall",
    "Main Image": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/18/SFCityHall.png/325px-SFCityHall.png",
    "Rating": 4.67,
    "Number Ratings": "3 ratings",
    "Reviews": [
      {
        "Rating": 5,
        "Review": "Gorgeous architecture. Easy to enter through standard security. Rotunda is impressive and worthwhile!"
      },
      {
        "Rating": 4,
        "Review": "Beautiful building and hard to imagine this is just a city hall building. Warning to any tourists, this was not the safest area. There are 2 modern playgrounds in front of the building. This is technically part of the tenderloin, though it feels safe initially, use caution when exploring particularly with children."
      },
      {
        "Rating": 5,
        "Review": "Join the 1 hour tour that runs a few times during the day - it’s simply amazing! We were lucky to have Rich and only a small group so we ended up spending 2 hours exploring the building and reliving Rich’s vivid recounts of his 40 year experience of working in this magnificent palace. Nothing really comes close to rivalling this building in the US - simple astonishing"
      }
    ]
  }

]

geojsonFeature = {
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


@app.route('/')
def map():
	global places
	return render_template('map.html', places=places, geojsonFeature = geojsonFeature)

@app.route('/', methods=['GET', 'POST'])
def direct_add_to_itin():
	global itin_list
	json_data = request.get_json()
	for place in itin_list:
		if place["Name"] == json_data["Name"]:
			abort(400)
	itin_list.append(json_data)
	return jsonify({'itinerary': itin_list})

@app.route('/item/<item_id>')
def item(item_id=None):
	return render_template('viewplace.html', item_id=item_id, places=places)

@app.route('/item/<item_id>', methods=['GET', 'POST'])
def add_to_itin(item_id=None):
	global itin_list
	json_data = request.get_json()
	for place in itin_list:
		if place["Name"] == json_data["Name"]:
			abort(400)
	itin_list.append(json_data)
	return jsonify({'itinerary': itin_list})

@app.route('/add_item')
def add_item():
	return render_template('add_item.html', places=places, geojsonFeature = geojsonFeature)

@app.route('/itinerary', methods=['GET', 'POST'])
def itinerary():
	global itin_list
	return render_template('itinerary.html', itinerary=itin_list)

@app.route('/delete_item', methods=['GET', 'POST'])
def delete_item():
	global itin_list
	json_data = request.get_json()
	idx = json_data["idx"]

	for place_idx in range(len(itin_list)):
		print("itin_list idx: ", itin_list[place_idx]["Id"], file=sys.stderr)
		if itin_list[place_idx]["Id"] == idx:
			del itin_list[place_idx]
			break

	return jsonify(itinerary = itin_list)

@app.route('/shuffle_itinerary', methods=['GET', 'POST'])
def shuffle_itinerary():
	global itin_list

	reshuffled_itin = []

	json_data = request.get_json()
	order = json_data["order"]

	reshuffled_itin = []
	# Reorder itin_list
	for i in range(len(order)):
		for j in range(len(itin_list)):
			if (order[i] == itin_list[j]["Name"]):
				reshuffled_itin.append(itin_list[j])

	itin_list = reshuffled_itin[:]

	return jsonify(itinerary = itin_list)

if __name__ == '__main__':
	app.run(debug = True)
