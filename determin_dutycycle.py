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

def findDutyCycle45():
    done = False

    while not done:
        userInput = input("Guess the duty cycle corresponding to 45 degrees: ")

        try:
            dutyCycle45 = float(userInput)
            pwm.ChangeDutyCycle(dutyCycle45)
            check = input("Is this correct? (yes/no)")
            done = check == "yes"
        except ValueError:
            print("Please input a float!")

    return dutyCycle45

pos_45 = findDutyCycle45()

#print("Change Duty Cycle to 7.5 which should be \"neutral position\".")
#pwm.ChangeDutyCycle(7.5) # neutral position
#sleep(3)
#print("Change Duty Cycle to 10 which should be +90 degrees.")
pwm.ChangeDutyCycle(10) # right +90 deg position
sleep(3)


exit = False
while not exit:
    position = input("Enter a position degree angle or n for neutral: \n")

    if position == "q":
        exit = True
    else:
        move_to_angle_45(pos_45)


pwm.stop()
GPIO.cleanup()
