from picamera import PiCamera
from time import sleep
from random import randint
import sys

video = randint(0, 999)

videoDuration = sys.argv[1]

camera = PiCamera()

camera.start_preview()
camera.start_recording('/home/pi/' + video + '.h264')
sleep(videoDuration)
camera.stop_recording()
camera.stop_preview()
