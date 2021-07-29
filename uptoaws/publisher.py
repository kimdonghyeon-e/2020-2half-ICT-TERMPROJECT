import time, json, ssl
import paho.mqtt.client as mqtt
from datetime import datetime
import serial
import time

bluetooth = serial.Serial('/dev/rfcomm0',9600)
usb = serial.Serial('/dev/ttyACM0',9600)

ENDPOINT = 'a3kb109oy8xa3g-ats.iot.us-west-2.amazonaws.com'
THING_NAME = 'RaspberryPi'

cycle=0

mqtt_awsclient = mqtt.Client(client_id=THING_NAME)
mqtt_awsclient.tls_set('./demo-cert/aws-root-cert.pem', certfile='./demo-cert/iot-cert.pem.crt',
        keyfile='./demo-cert/private-key.pem.key', tls_version=ssl.PROTOCOL_TLSv1_2, ciphers=None)
mqtt_awsclient.connect(ENDPOINT, port=8883)
mqtt_awsclient.loop_start() # threaded network loop

mqtt = mqtt.Client("test2")
mqtt.connect("localhost", 1883)
mqtt.loop_start()

while 1:
          bser = bluetooth.readline()
          user = usb.readline()
          
          bdata=bser.split(",")
          udata=user.split(",")
          

          bt="Outdoor "+bdata[0]+"'C"
          mqtt.publish("outside/temp", bt)

          bh=bdata[1]+"%"
          mqtt.publish("outside/humi", bh)

          ut="Indoor "+udata[0]+"'C"
          mqtt.publish("inside/temp", ut)

          uh=udata[1]+"%"
          mqtt.publish("inside/humi", uh)
          
          cycle=cycle+1
          if (cycle==60) :
              now=datetime.now()
              nowtime='%s-%s-%s %s:%s' % (now.year, now.month, now.day, now.hour, now.minute)
              pload=json.dumps({'outdoor temp':bdata[0], 'outdoor humi':bdata[1], 'indoor temp':udata[0], 'indoor humi':udata[1], 'time':nowtime})
              mqtt_awsclient.publish('mirror/ht', pload, qos=1)
              cycle=0

