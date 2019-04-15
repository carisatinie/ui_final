from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
import json
app = Flask(__name__)

places = [
	{
		"Id": 1,

	}
]

itinerary = []

@app.route('/')
def map():
	return render_template('map.html')

@app.route('/item/<item_id>')
def item(item_id=None):
	return render_template('viewplace.html', item_id=item_id)
	


if __name__ == '__main__':
	app.run(debug = True)