import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
pin = 24
GPIO.setup(pin, GPIO.OUT)
GPIO.setup(17, GPIO.OUT)
p1 = GPIO.PWM(pin, 1000)
p1.start(1)
p2 = GPIO.PWM(17, 1000)
p2.start(0)
try:
    while True:
        dc = float(input())
        p1.ChangeDutyCycle(dc)
        p2.ChangeDutyCycle(dc)
        v = 3.3 * dc / 100
        print(v, 'v')
finally:
    p1.stop()
    GPIO.cleanup()