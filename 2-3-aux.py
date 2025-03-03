import RPi.GPIO as GPIO
leds = [2, 3, 4, 17, 27, 22, 10, 9]
aux = [21, 20, 26, 16, 19, 25, 23, 24]
GPIO.setmode(GPIO.BCM)

GPIO.setup(leds, GPIO.OUT)
GPIO.setup(aux, GPIO.IN)

while True:
    for j in range(8):
        GPIO.output(leds[j], GPIO.input(aux[j]))
