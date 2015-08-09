#!/usr/bin/env python3
from flask import Flask, request
import os
import json
import time
from smarthomemongo import SmartHomeDB

app = Flask(__name__)
smartDB = SmartHomeDB()


@app.route('/')
def index():
	records = smartDB.getTemperaturePoints()
	print(records)
	return json.dumps(records)


@app.route('/add', methods=['POST'])
def add():
	recordJson = request.get_json()
	smartDB.insertTemperaturePoint(recordJson)
	return 'Success', 200

@app.route('/update_stats', methods=['POST'])
def update_stats():
	recordJson = request.get_jsom()
	smartDB.updateCurrentStats(recordJson)
	return 'Success', 200

@app.route('get_current_stats',methods=['GET'])
def get_current_stats():
	record = smartDB.getCurrentStats()
	return json.dumps(record)



if __name__ == '__main__':
	app.run(host='0.0.0.0',debug=True)




