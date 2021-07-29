import paho.mqtt.client as mqtt
import time
import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)

trig=18
echo=24

gpio.setup(trig, gpio.OUT)
gpio.setup(echo, gpio.IN)

gpio.cleanup()

