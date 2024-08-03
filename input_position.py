#run add_attachment before to set the attachment to the correct initial neutral position

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(33, GPIO.OUT)

print("Starting PWM on GPIO 13...")
pwm=GPIO.PWM(33, 50)
pwm.start(0)

def set_45():
    print("Changing Duty Cycle to set 45 degrees.")
    pwm.ChangeDutyCycle(8.6) # duty cycle 8.6 => 45 degree angle

def set_22():
    print("Changing Duty Cycle to set 22.5 degrees.")
    pwm.ChangeDutyCycle(7.9) # duty cycle 7.9 => 22.5 degree angle

def set_neutral():
    print("Changing Duty Cycle to set neutral (0 degrees).")
    pwm.ChangeDutyCycle(7.2) # duty cycle 7.2 => 0 degree angle/neutral position


exit = False

set_neutral()
curr_dc = 7.2

print("Enter a \'45\', \'22\' for positions 45 or 22 degree, \'n\' for neutral position, or w to move the angle up s to move the angle down (:x to quit): \n")

while not exit:

    position = input("Set position: \n")

    if position == ":x":
        exit = True
    elif position == "45":
        set_45()
        curr_dc = 8.6
    elif position == "22":
        set_22()
        curr_dc = 7.9
    elif position == "n":
        set_neutral()
        curr_dc = 7.2
    elif position == "w":
        print("Moving angle up.")
        pwm.ChangeDutyCycle(curr_dc - 0.2) # duty cycle 7.2 => 0 degree angle/neutral position
        curr_dc = curr_dc - 0.2
    elif position == "s":
        print("Moving angle up.")
        pwm.ChangeDutyCycle(curr_dc + 0.2) # duty cycle 7.2 => 0 degree angle/neutral position
        curr_dc = curr_dc + 0.2
    elif position == "q":
        print("Duty cycle is: " + str(curr_dc))

pwm.stop()
GPIO.cleanup()