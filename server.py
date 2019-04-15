from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
import json
app = Flask(__name__)

itinerary = []

@app.route('/')
def map():
	return render_template('map.html')

@app.route('/itinerary', methods=['GET', 'POST'])
def add_to_itinerary():
	


if __name__ == '__main__':
	app.run(debug = True)