import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(25, GPIO.IN)

while True:
    GPIO.output( 17, GPIO.input(25))
