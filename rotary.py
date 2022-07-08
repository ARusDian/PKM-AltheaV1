#!/usr/bin/env python2.7
# script by Alex Eames https://raspi.tv/
# https://raspi.tv/2013/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
counter = 0
temp = 0


def pin_handler(pin):
    global pin5_counter, pin5_time, pin5_prevState
    global pin12_counter, pin12_time, pin12_prevState

    pin5_state = GPIO.input(5)
    pin12_state = GPIO.input(12)

    if (pin5_state != pin5_prevState):
        pin5_prevState = pin5_state

        pin5_time = time.time()
        pin5_counter += 1
        print("Pin5 - State:", pin5_state, " Counter: ", pin5_counter)

    if (pin12_state != pin12_prevState):
        pin12_prevState = pin12_state

        pin12_time = time.time()
        pin12_counter += 1
        print("Pin12 - State:", pin12_state, " Counter: ", pin12_counter)

def interrupt_handler(channel):
    global counter
    if channel == 17:
        if GPIO.input(17) == 0:
            counter =+ 1
        else:
            counter =- 1
    elif channel == 27:
        if GPIO.input(27) == 0:
            counter =+ 1
        else:
            counter =- 1


GPIO.add_event_detect(17, GPIO.RISING, callback=interrupt_handler, bouncetime=200)  # add rising edge detection on a channel
GPIO.add_event_detect(27, GPIO.RISING, callback=interrupt_handler, bouncetime=200)
# GPIO 23 set up as input. It is pulled up to stop false signals

while True:
    if counter != temp:
        print(counter)
        temp = counter




