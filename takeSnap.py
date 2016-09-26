from picamera import PiCamera
from time import sleep
from random import randint

camera = PiCamera()

randomNumber = randint(0, 999)

camera.start_preview()
sleep(5)
camera.capture('/home/pi/Desktop/' + randomNumber + '.jpg')
camera.stop_preview()
