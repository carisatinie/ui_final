import sys
from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
import json
app = Flask(__name__)

itin_list = []

@app.route('/')
def map():
	return render_template('map.html')

@app.route('/item/<item_id>')
def item(item_id=None):
	return render_template('viewplace.html', item_id=item_id, itinerary=itin_list)

@app.route('/item/<item_id>', methods=['GET', 'POST'])
def add_item(item_id=None):
	global itin_list
	json_data = request.get_json()
	for place in itin_list:
		print(place["Name"], " ", json_data["Name"])
		if place["Name"] == json_data["Name"]:
			abort(400)
	itin_list.append(json_data)
	return jsonify({'itinerary': itin_list})

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
			print("ENTERED", file=sys.stderr)
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
