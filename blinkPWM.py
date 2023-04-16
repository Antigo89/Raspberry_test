import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(33,GPIO.OUT)
pwmout = GPIO.PWM(33,100)
pwmout.start(0)

try:
    while True:
        for duteCycle in range(0,100,1):
            pwmout.ChangeDutyCycle(duteCycle)
            time.sleep(0.1)
        for duteCycle in range(100,0,-1):
            pwmout.ChangeDutyCycle(duteCycle)
            time.sleep(0.1)
except KeyboardInterrupt:
    pwmout.stop()
    GPIO.cleanup()
    print('exeting')