# #!/usr/bin/env python
# #
# # Raspberry Pi Rotary Encoder Class
# # $Id: rotary_class.py,v 1.3 2021/04/20 12:23:04 bob Exp $
# #
# # Author : Bob Rathbone
# # Site : http://www.bobrathbone.com
# #
# # This class uses standard rotary encoder with push switch
# #
# #
# import RPi.GPIO as GPIO
#
#
# class RotaryEncoder:
#     CLOCKWISE = 1
#     ANTICLOCKWISE = 2
#     BUTTONDOWN = 3
#     BUTTONUP = 4
#     rotary_a = 0
#     rotary_b = 0
#     rotary_c = 0
#     last_state = 0
#     direction = 0
#
#     # Initialise rotary encoder object
#     def __init__(self, pinA, pinB, button, callback):
#
#         self.pinA = pinA
#     self.pinB = pinB
#     self.button = button
#     self.callback = callback
#     GPIO.setmode(GPIO.BCM)
#     # The following lines enable the internal pull-up resistors
#     # on version 2 (latest) boards
#     GPIO.setwarnings(False)
#     GPIO.setup(self.pinA, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#     GPIO.setup(self.pinB, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#     GPIO.setup(self.button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#     # For version 1 (old) boards comment out the above four
#
#
# lines
# # and un-comment the following 3 lines
# # GPIO.setup(self.pinA, GPIO.IN)
# # GPIO.setup(self.pinB, GPIO.IN)
# # GPIO.setup(self.button, GPIO.IN)
# # Add event detection to the GPIO inputs
# GPIO.add_event_detect(self.pinA, GPIO.BOTH,
#                       callback=self.switch_event)
# GPIO.add_event_detect(self.pinB, GPIO.BOTH,
#                       callback=self.switch_event)
# GPIO.add_event_detect(self.button, GPIO.BOTH,
#                       callback=self.button_event, bouncetime=200)
# return
#
#
# # Call back routine called by switch events
# def switch_event(self, switch):
#
#
#     if GPIO.input(self.pinA):
#     self.rotary_a = 1
# else:
