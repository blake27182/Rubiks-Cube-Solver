from picamera import PiCamera
import RPi.GPIO as GPIO
import time

camera = PiCamera()
camera.start_preview()
time.sleep(5)
camera.capture('tester.jpg')
camera.stop_preview()
