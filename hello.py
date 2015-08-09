from flask import Flask
import os
import RPi.GPIO
import time
from temperature import temperature_humidity


app = Flask(__name__)

def setup_board():
	RPi.GPIO.setmode(RPi.GPIO.BOARD)
	RPi.GPIO.setup(11,RPi.GPIO.IN)
	RPi.GPIO.setup(11,RPi.GPIO.OUT)
	RPi.GPIO.output(11,False)
	print "Board Setup"


@app.route('/ON')
def turn_on():
	result = ""
	try:
		RPi.GPIO.output(11,True)
		time.sleep(0.1)
		result = str(RPi.GPIO.input(11))
	except Exception as inst:
		result = str(inst)
	return result 

@app.route('/OFF')
def turn_off():
	RPi.GPIO.output(11,False)
	time.sleep(0.1)
	return str(RPi.GPIO.input(11))


@app.route('/status')
def status():
	input_status = RPi.GPIO.input(11)
	return str(input_status)


@app.route('/temperature')
def temperature():
	return temperature_humidity(22,17)

    

if __name__ == '__main__':
	setup_board()
	app.run(host='0.0.0.0',debug=True)




