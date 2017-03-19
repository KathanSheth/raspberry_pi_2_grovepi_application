import time
import paho.mqtt.client as mqtt
import Adafruit_DHT
import os

mqttc=mqtt.Client()
mqttc.connect("172.20.10.10",1883,60)
mqttc.loop_start()

print "inside Humidity sensor "
print "Inside Humidity sensor"

#read temperature
def read_temp_data():
	humidity, temperature = Adafruit_DHT.read_retry(11, 4)	
	print humidity
	return humidity
	#return random.randint(-50, 100)
#publish temperature
while 1:
	t=read_temp_data()
	print "Publish Humidity data "
	device_uuid=os.environ['RESIN_DEVICE_UUID'];
	#print device_uuid
	print t
	(result,mid)=mqttc.publish("topic/GeneralizedIoT/"+str(device_uuid),t,2)
	time.sleep(1)

mqttc.loop_stop()
mqttc.disconnect()
