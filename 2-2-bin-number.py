import RPi.GPIO as GPIO
import time

dac = [8, 11, 7, 1, 0, 5, 12, 6]
num = '01110011'
print(num)
number = [int(num[i]) for i in range(len(num))]
GPIO.setmode(GPIO.BCM)
for i in dac:
    GPIO.setup(i, GPIO.OUT)
for j in range(8):
    GPIO.output(dac[j], number[j])
time.sleep(10)
for k in dac: GPIO.output(k, 0)
print(number)

