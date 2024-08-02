import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(33, GPIO.OUT)

print("Starting PWM on GPIO 13...")
pwm=GPIO.PWM(33, 50)
pwm.start(0)


print("Change Duty Cycle to 5 which should be -90 degrees.")
pwm.ChangeDutyCycle(5) # left -90 deg position
sleep(3)
print("Change Duty Cycle to 7.5 which should be \"neutral position\".")
pwm.ChangeDutyCycle(7.5) # neutral position
sleep(3)
print("Change Duty Cycle to 10 which should be +90 degrees.")
pwm.ChangeDutyCycle(10) # right +90 deg position
sleep(3)

pwm.stop()
GPIO.cleanup()
