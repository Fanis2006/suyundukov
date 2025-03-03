import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac, GPIO.OUT)
def bin2dec(num):
    return [int(i) for i in bin(num)[2:].zfill(8)]
try:
    times = int(input('время периода: '))
    a = 0
    down = True
    while True:
        if a == 0:
            down = False
        elif a == 255:
            down = True
        for i in range(8):

            GPIO.output(dac[i], bin2dec(int(a))[i])
        time.sleep(times/255/2)
        if down:
            a = a - 1
        else:
            a = a + 1
    for _ in dac:
        GPIO.output(_, 0)
    GPIO.cleanup()