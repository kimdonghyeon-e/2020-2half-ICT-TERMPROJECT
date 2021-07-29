try :
        import paho.mqtt.client as mqtt
        import time
        import RPi.GPIO as gpio

        gpio.setmode(gpio.BCM)

        trig=18
        echo=24

        gpio.setup(trig, gpio.OUT)
        gpio.setup(echo, gpio.IN)
        
        mqtt = mqtt.Client("test2")
        mqtt.connect("localhost", 1883, 1000)
        mqtt.loop_start()

        islast=0

        while 1:
         


              gpio.output(trig, False)
              time.sleep(0.5)
                         
              gpio.output(trig, True)
              time.sleep(0.5)
              gpio.output(trig, False)
                              
              while gpio.input(echo) == 0 :
                   pulse_start = time.time()
                              
              while gpio.input(echo) == 1 :
                   pulse_end = time.time()
                              
              pulse_duration = pulse_end - pulse_start
              distance = pulse_duration * 17000
              distance = round(distance, 2)
              
              if distance <= 70.00:
                  isit=1
              else:
                  isit=0
                  
              
              
              if islast!=isit:
                  if isit==1:
                      mqtt.publish("isdetected", "detected")

                  else:
                      mqtt.publish("isdetected", "notdetected")

                  islast=isit
                  
                  
              print(distance)
                  

                                     
except :
        gpio.cleanup()

