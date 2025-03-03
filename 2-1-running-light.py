import RPi.GPIO as GPIO
import time
dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
def dec2bin(value):
    return [int(bit) for bit in bin (value)[2:].zfill(8)]

def adc():
    for i in range(256):
        signal = dec2bin(i)
        GPIO.output(dac, signal)
        v = (i / 256)* 3.3
        time.sleep(0.001)
        compV = GPIO.input(comp)
        if compV == 1:
            print(i, v, "Volts")
            break
        
try:
    while True:
        adc()

finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.output(troyka, 0)
    GPIO.cleanup()