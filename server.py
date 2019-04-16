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
	itin_list.append(json_data)
	return jsonify({'itinerary': itin_list})

@app.route('/itinerary', methods=['GET', 'POST'])
def itinerary():
	global itin_list
	return render_template('itinerary.html', itinerary=itin_list)

if __name__ == '__main__':
	app.run(debug = True)
