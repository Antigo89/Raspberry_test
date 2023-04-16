import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(33,GPIO.OUT)

try:
	while True:
		GPIO.output(33,1)
		time.sleep(1)
		GPIO.output(33,0)
		time.sleep(1)
except KeyboardInterrupt:
	GPIO.cleanup()
	print ('exeting')
