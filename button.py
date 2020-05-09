import RPi.GPIO as GPIO

BUTTON_PIN = 26
OFFLED_PIN = 16


GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(OFFLED_PIN, GPIO.OUT)


def button():
    return GPIO.input(BUTTON_PIN)

def led(index):
    if index == 0:
        GPIO.output(OFFLED_PIN, 1)
    else:
        GPIO.output(OFFLED_PIN, 0)

