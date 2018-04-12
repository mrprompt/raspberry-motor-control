#!/usr/bin/env python
import argparse
import os
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

IN1 = 6  # IN1
IN2 = 13 # IN2
IN3 = 19 # IN3
IN4 = 26 # IN4
TIME = 0.001

GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

GPIO.output(IN1, False)
GPIO.output(IN2, False)
GPIO.output(IN3, False)
GPIO.output(IN4, False)

def step1():
    """
    move function
    """
    GPIO.output(IN4, True)
    sleep(TIME)
    GPIO.output(IN4, False)

def step2():
    """
    move function
    """
    GPIO.output(IN4, True)
    GPIO.output(IN3, True)
    sleep(TIME)
    GPIO.output(IN4, False)
    GPIO.output(IN3, False)

def step3():
    """
    move function
    """
    GPIO.output(IN3, True)
    sleep(TIME)
    GPIO.output(IN3, False)

def step4():
    """
    move function
    """
    GPIO.output(IN2, True)
    GPIO.output(IN3, True)
    sleep(TIME)
    GPIO.output(IN2, False)
    GPIO.output(IN3, False)

def step5():
    """
    move function
    """
    GPIO.output(IN2, True)
    sleep(TIME)
    GPIO.output(IN2, False)

def step6():
    """
    move function
    """
    GPIO.output(IN1, True)
    GPIO.output(IN2, True)
    sleep(TIME)
    GPIO.output(IN1, False)
    GPIO.output(IN2, False)

def step7():
    """
    move function
    """
    GPIO.output(IN1, True)
    sleep(TIME)
    GPIO.output(IN1, False)

def step8():
    """
    move function
    """
    GPIO.output(IN4, True)
    GPIO.output(IN1, True)
    sleep(TIME)
    GPIO.output(IN4, False)
    GPIO.output(IN1, False)

def right(step):
    """
    Move to the right side
    """
    for i in range(step):
        step1()
        step2()
        step3()
        step4()
        step5()
        step6()
        step7()
        step8()

        print "Step left: ", i

def left(step):
    """
    Move to the left side
    """
    for i in range(step):
        step8()
        step7()
        step6()
        step5()
        step4()
        step3()
        step2()
        step1()

        print "Step right: ", i

def looping():
    """
    console function
    """
    while True:
        command = raw_input("Direction <left | right> <steps>: ").split(" ")
        direction = command[0]
        counter = int(command[1])

        if direction == "left":
            left(counter)

        if direction == "right":
            right(counter)

if __name__ == '__main__':
    PARSER = argparse.ArgumentParser("simple_example")
    PARSER.add_argument("direction", help="Direction: ", choices=('left', 'right', 'console'))
    PARSER.add_argument("counter", help="Steps: 1 ~ 1024", type=int, default=1)

    ARGS = PARSER.parse_args()

    if ARGS.direction == "left":
        left(ARGS.counter)

    if ARGS.direction == "right":
        right(ARGS.counter)

    if ARGS.direction == "console":
        os.system('clear')

        looping()

    GPIO.cleanup()
