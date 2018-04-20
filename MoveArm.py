import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

pwm=GPIO.PWM(11,50)

pwm.start(5)
time.sleep(1)

pwm.ChangeDutyCycle(12)
time.sleep(2)

pwm.ChangeDutyCycle(5)
time.sleep(1)
pwm.ChangeDutyCycle(5)


GPIO.cleanup()
