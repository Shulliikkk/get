import RPi.GPIO as GPIO
import time

pins = [21, 20, 16, 12, 7, 8, 25, 24]

GPIO.setmode(GPIO.BCM)
GPIO.setup(pins, GPIO.OUT)

while True:
    for i in range(3):
        for pin in pins:
            GPIO.output(pin, 1)
            time.sleep(0.2)
            GPIO.output(pin, 0)
    GPIO.cleanup()