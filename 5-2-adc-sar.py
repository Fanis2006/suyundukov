import RPi.GPIO as GPIO
import time
dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)
def convert(chislo):
    ret = []
    while chislo != 0:
        ret.append(chislo % 2)
        chislo = chislo // 2
    for i in range(8 - len(ret)):
        ret.append(0)
    return ret[::-1]

def adc():
    k = 0
    for i in range(7, -1, -1):
        k += 2 ** i
        GPIO.output(dac, convert(k))
        time.sleep(0.05)
        if GPIO.input(comp) == 1:
            k -= 2 ** i
    return k

try:
    while True:
        number = adc()
        if number != 0:
            print(number, "{:.2f} Volts".format(3.3 * number / 256))
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup()