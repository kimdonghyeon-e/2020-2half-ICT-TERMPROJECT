

from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import paho.mqtt.client as mqtt

def detect(img, cascade):
    scaleFactor=1.3,     
    minNeighbors=4,    
    minSize=(30, 30),   
    rects = cascade.detectMultiScale(img, scaleFactor=1.3, minNeighbors=4, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE) 

    if len(rects) == 0: 

        return []

    return rects



def draw_rects(img, rects, color): 

    for x, y, w, h in rects:  

        cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)


camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(640, 480))

cascade = cv2.CascadeClassifier("/usr/local/lib/python3.7/dist-packages/cv2/data/haarcascade_frontalface_alt.xml")



time.sleep(0.1)

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):

    img = frame.array     
    #img = cv2.flip(img, 0) 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    gray = cv2.equalizeHist(gray) 



    rects = detect(gray, cascade) 

    vis = img.copy()

    

    key = cv2.waitKey(1) & 0xFF



    

    rawCapture.truncate(0)

    #print(len(rects))
    import paho.mqtt.client as mqtt
    mqtt = mqtt.Client("test")
    mqtt.connect("localhost", 1883)
    if len(rects)==0:
        mqtt.publish("message", "얼굴이 인식되지 않아요.")
    else:
        mess=str(len(rects))+"명이 앞에 있어요."
        mqtt.publish("message", mess)
    mqtt.loop(2)
    time.sleep(1)




    if key == ord("q"):
        break

