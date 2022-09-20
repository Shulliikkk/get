import RPi.GPIO as GPIO
import time

sleep = 1

pins = [26, 19, 13, 6, 5, 11, 9, 10]
number = [0, 1, 0, 1, 0, 1, 0, 1]

GPIO.setmode(GPIO.BCM)
GPIO.setup(pins, GPIO.OUT)

GPIO.output(pins, number)
time.sleep(sleep)

GPIO.output(pins, 0)

number = [0, 0, 0, 0, 0, 0, 1, 0]
GPIO.output(pins, number)
time.sleep(sleep)

numbers = [255, 127, 64, 32, 5, 0, 256]

for n in numbers:
    binar = bin(n)[2:len(bin(n))]
    binar = (8 - len(binar)) * '0' + binar
    binar = list(binar)
    binar = [int(i) for i in binar]
    GPIO.output(pins, binar)
    time.sleep(5)



