import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(33, GPIO.OUT)

print("Starting PWM on GPIO 13...")
pwm=GPIO.PWM(33, 50)
pwm.start(0)

def move_to_angle_45(angle):
    print("Change Duty Cycle to 5 which should be -90 degrees.")
    pwm.ChangeDutyCycle(angle) # left -90 deg position
    sleep(3)


print("Change Duty Cycle to 7.5 which should be \"neutral position\".\n")
pwm.ChangeDutyCycle(7.2) # neutral position
print("You have 20 seconds to put the attachment straight.\n")
sleep(20)


print("Changing to a 45 degree angle.\n")
pwm.ChangeDutyCycle(8.6) # neutral position
sleep(1)

pwm.stop()
GPIO.cleanup()
