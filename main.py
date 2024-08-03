# Python module to control the GPIO on a Raspberry Pi
import RPi.GPIO as GPIO
# Function to delay the execution of the program
from time import sleep

# GPIO stuffs
OUTPUT_PIN: int = 33
PWM_FREQUENCY: int = 50

# Modify as necessary
DUTY_CYCLE_0: float = 7.2
DUTY_CYCLE_45: float = 8.4
# simple math here can create shifts for other duty cycle differences if needed
SHIFT_DUTY_CYCLE_5: float = (DUTY_CYCLE_45 - DUTY_CYCLE_0) / 9

# User options
QUIT: str = "q"
NEUTRAL: str = "n"
MAX: str = "m"
UP: str = "u"
DOWN: str = "d"


def main() -> None:
    # Setup the GPIO and PWM
    setup_GPIO()
    pwm = setup_PWM()
    # Allow for the attachment to be correctly put in neutral position
    setup_attachment(pwm)

    # Print out user options
    print_options()

    # Track the "current duty cycle" to better increment
    current_cycle: float = DUTY_CYCLE_0  # Starts at neutral position
    # Use a negative number as "invalid"
    while current_cycle > 0.0:
        current_cycle = move_pwm(pwm, current_cycle)

    # Close the PWM and clean up PGIO
    cleanup(pwm)


def setup_GPIO() -> None:
    # Refer to the pins by their number
    GPIO.setmode(GPIO.BOARD)
    # Set GPIO33 as the output
    GPIO.setup(OUTPUT_PIN, GPIO.OUT)


def setup_PWM():
    print("Starting PWM on GPIO " + OUTPUT_PIN)
    # Setup a Pulse Width Modulated on the output pin with frequency 50Hz
    pwm = GPIO.PWM(OUTPUT_PIN, PWM_FREQUENCY)
    # Initialize the PWM at duty cycle 0.0
    pwm.start(0.0)

    return pwm


def setup_attachment(pwm) -> None:
    # Initialize the pwm to "neutral" position
    pwm.ChangeDutyCycle(DUTY_CYCLE_0)

    MESSAGE: str = "Put the attachment in a neutral (0 degrees) angle.\n"
    + "Please input 'yes' once you're done: "

    # Ensure the user is certain the attachment is put correctly
    valid: bool = input(MESSAGE) == 'yes'
    while not valid:
        valid = input(MESSAGE) == 'yes'


def print_options() -> None:
    print()
    print("Move the attachment 5 degrees downwards: " + DOWN)
    print("Move the attachment 5 degrees upwards: " + UP)
    print("Move the attachment to neutral position (0 degrees): " + NEUTRAL)
    print("Move the attachment to most downward position (45 degrees): " + MAX)
    print("Quit the program: " + QUIT)
    print()


def move_pwm(pwm, current_cycle: float) -> float:
    user_input: str = input("Input: ")

    if user_input == DOWN:
        current_cycle = move_down(pwm, current_cycle)
    elif user_input == UP:
        current_cycle = move_up(pwm, current_cycle)
    elif user_input == NEUTRAL:
        current_cycle = move_neutral(pwm, current_cycle)
    elif user_input == MAX:
        current_cycle = move_max(pwm, current_cycle)
    elif user_input == QUIT:
        current_cycle = -1.0
    else:
        print("Unknown option chosen!")
        print_options()

    # Safe buffer time to wait for the component to move
    sleep(1)

    return current_cycle


def move_down(pwm, current_cycle: float) -> float:
    # Bounds checking, ensure attachment doesn't turn above 45 degrees
    current_cycle = max(current_cycle + SHIFT_DUTY_CYCLE_5, DUTY_CYCLE_45)

    pwm.ChangeDutyCycle(current_cycle)

    if (current_cycle == DUTY_CYCLE_45):
        print("Maximum position reached!")

    return current_cycle


def move_up(pwm, current_cycle: float) -> float:
    # Bounds checking, ensure attachment doesn't turn below 0 degrees
    current_cycle = min(current_cycle - SHIFT_DUTY_CYCLE_5, DUTY_CYCLE_0)

    pwm.ChangeDutyCycle(current_cycle)

    if (current_cycle == DUTY_CYCLE_0):
        print("Minimum position reached!")

    return current_cycle


def move_neutral(pwm, current_cycle: float) -> float:
    current_cycle = DUTY_CYCLE_0

    pwm.ChangeDutyCycle(current_cycle)

    return current_cycle


def move_max(pwm, current_cycle: float) -> float:
    current_cycle = DUTY_CYCLE_45

    pwm.ChangeDutyCycle(current_cycle)

    return current_cycle


def cleanup(pwm) -> None:
    pwm.stop()
    GPIO.cleanup()


if __name__ == '__main__':
    main()
