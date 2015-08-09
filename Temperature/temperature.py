import Adafruit_DHT


def temperature_humidity(sensor,pin):
	humidity, temperature = Adafruit_DHT.read_retry(sensor,pin)
	if humidity is not None and temperature is not None:
		tempString = '{0:0.1f}'.format(temperature)
		humdityString = '{0:0.1f}'.format(humidity)

		return '{"temp":' + tempString + ',"humidity":' + humdityString + '}'
	else:
		return 'ERROR'


if __name__=='__main__':
	print temperature_humidity(22,17)

