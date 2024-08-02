#run add_attachment before to set the attachment to the correct initial neutral position

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(33, GPIO.OUT)

print("Starting PWM on GPIO 13...")
pwm=GPIO.PWM(33, 50)
pwm.start(0)

def set_45():
    print("Changing Duty Cycle to 45 degrees.")
    pwm.ChangeDutyCycle(8.6) # duty cycle 8.6 => 45 degree angle
    sleep(1)

def set_neutral():
    print("Changing Duty Cycle to neutral.")
    pwm.ChangeDutyCycle(7.2) # duty cycle 7.2 => 0 degree angle/neutral position
    sleep(1)


exit = False
while not exit:
    position = input("Enter a \'45\' for position 45 degrees or \'n\' for neutral position (q to quit): \n")

    if position == "q":
        exit = True
    elif position == "45":
        set_45()
    elif position == "n":
        set_neutral()


pwm.stop()
GPIO.cleanup()
