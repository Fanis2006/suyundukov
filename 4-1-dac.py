import RPi.GPIO as GPIO
dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
def dec2bin(chislo):
    new = ''
    while chislo != 0:
        new = new + str(chislo % 2)
        chislo //= 2
    new = new + "0" * (8-len(new))
    return new[::-1]
def clean():
    for i in dac:
        GPIO.output(i, GPIO.LOW)
try:
    while True:
        a = input()
        k = True
        if a == 'q':
            break
        elif a.lstrip('-').isdecimal():
            a = int(a)
            if a < 0:
                print('Введено отрицательное число')
                clean()
            elif a > 255:
                print('Введено число, превышающее 255')
                clean()
            else:
                print('bin = {dec2bin(a)}')
                print('предполагаемое значение напряжения: {round(3.3 * a /255, 3)} B')
                for i in range(8): GPIO.output(dac[i], GPIO.HIGH) if dec2bin(a)[i] == '1' else GPIO.output(dac[i], GPIO.LOW)
            k = False
        if k:
            a = ''.join(a.split('.'))
            a = a.lstrip('-')
            if a.isdecimal():
                print('Введено нецелое число')
                clean()
            else:
                print('введено не число')
                clean()
finally:
    for i in dac:
        GPIO.output(i, GPIO.LOW)
    GPIO.cleanup()