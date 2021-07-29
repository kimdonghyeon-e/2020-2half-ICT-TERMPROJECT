import paho.mqtt.client as mqtt
import time
import serial

bluetooth = serial.Serial('/dev/rfcomm0',9600)
usb = serial.Serial('/dev/ttyACM0',9600)

while 1:
          bser = bluetooth.readline()
          user = usb.readline()
          
          bdata=bser.split(",")
          udata=user.split(",")
          
          import paho.mqtt.client as mqtt
          mqtt = mqtt.Client("test2")
          bt="Outdoor "+bdata[0]+"'C"
          mqtt.connect("localhost", 1883)
          mqtt.publish("outside/temp", bt)
          mqtt.loop(2)
          bh=bdata[1]+"%"
          mqtt.connect("localhost", 1883)
          mqtt.publish("outside/humi", bh)
          mqtt.loop(2)
          ut="Indoor "+udata[0]+"'C"
          mqtt.connect("localhost", 1883)
          mqtt.publish("inside/temp", ut)
          mqtt.loop(2)
          uh=udata[1]+"%"
          mqtt.connect("localhost", 1883)
          mqtt.publish("inside/humi", uh)
          mqtt.loop(2)
          