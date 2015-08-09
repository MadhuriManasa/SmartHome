from Adafruit_Python_DHT  import Adafruit_DHT
import time
import json
import httplib
import sys

URL='bb-smart-home.herokuapp.com'
DEVICE_NAME ='raspberry'

def temperature_humidity(sensor,pin):
	humidity, temperature = Adafruit_DHT.read_retry(sensor,pin)
	if humidity is not None and temperature is not None:
		return [temperature,humidity]
	else:
		return []


def upload_temp():
	points = temperature_humidity(22,17)
	if len(points) != 0:
		record = {
		'temperature' : points[0],
		'humidity' : points[1],
		'device_name' : DEVICE_NAME,
		'timestamp' : long(time.time())

		}
		conn = httplib.HTTPConnection(URL)
		conn.request("POST",'/add',json.dumps(record),{'Content-Type':'application/json'})
		response = conn.getresponse()
		print response.status, response.reason
		conn.close()

def upload_current_stats():
	points = temperature_humidity(22,17)
	if( len(points) != 0):
		record = {
		'cur_temperature' : points[0],
		'cur_humidity' : points[1],
		'device_name' :DEVICE_NAME,
		'timestamp' : long(time.time())
		}=
		conn = httplib.HTTPConnection(URL)
		con.request("POST",'/update_stats',json.dumps(record),{'Content-Type':'application/json'})
		response = conn.getresponse()
		print response.status, response.reason
		conn.close()



if __name__=='__main__':

	operation = sys.argv[0]
	if( operation=='add_reading'):
		upload_temp()
	else if( operation == 'cur_reading'):
		upload_current_stats()
		

