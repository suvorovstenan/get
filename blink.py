import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)
GPIO.setup(24, GPIO.IN)

try:
    while True:
        print(GPIO.input(24))
        GPIO.output( 25, GPIO.input(24))
except:
    pass

GPIO.cleanup()
