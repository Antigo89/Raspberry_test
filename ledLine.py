import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
pwmoutR = GPIO.PWM(13,100)
pwmoutB = GPIO.PWM(12,100)
pwmoutG = GPIO.PWM(26,100)
pwmoutR.start(0)
pwmoutG.start(0)
pwmoutB.start(0)

try:
    while True:
        #pwmoutR.ChangeDutyCycle(100)
        #pwmoutG.ChangeDutyCycle(100)
        #pwmoutB.ChangeDutyCycle(100)
        for duteCycle in range(0,100,1):
            pwmoutB.ChangeDutyCycle(duteCycle)
            pwmoutG.ChangeDutyCycle(100-duteCycle)
            time.sleep(0.1)
        for duteCycle in range(100,0,-1):
            pwmoutB.ChangeDutyCycle(duteCycle)
            pwmoutG.ChangeDutyCycle(100-duteCycle)
            time.sleep(0.1)
except KeyboardInterrupt:
    pwmoutR.stop()
    pwmoutG.stop()
    pwmoutB.stop()
    GPIO.cleanup()
    print('exeting')
