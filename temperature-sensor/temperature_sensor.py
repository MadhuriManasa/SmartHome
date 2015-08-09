#from Adafruit_Python_DHT  import Adafruit_DHT
import time
import json
import httplib

URL='bb-smart-home.herokuapp.com'

# def temperature_humidity(sensor,pin):
# 	humidity, temperature = Adafruit_DHT.read_retry(sensor,pin)
# 	if humidity is not None and temperature is not None:
# 		return [temperature,humidity]
# 	else:
# 		return []


def upload_temp():
	#points = temperature_humidity(22,17)
	points = [57.0,66.0]
	if len(points) != 0:
		record = {
		'temperature' : points[0],
		'humidity' : points[1],
		'device_name' : 'raspberry',
		'timestamp' : long(time.time())

		}
		conn = httplib.HTTPConnection(URL)
		conn.request('POST',URL+'/add',json.dumps(record),{'Content-Type':'application/json'})
		response = conn.getresponse()
		print response.status, response.reason
		conn.close()





if __name__=='__main__':
	upload_temp()

