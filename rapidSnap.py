from picamera import PiCamera
from time import sleep
import sys

numberOfSnaps = sys.argv[1]

camera = PiCamera()

camera.start_preview()
for i in range(numberOfSnaps):
    sleep(5)
    camera.capture('/home/pi/Desktop/image%s.jpg' % i)
camera.stop_preview()
