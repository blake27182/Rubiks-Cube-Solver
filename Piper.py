#
#  Piper.py
#  Rubik's Cube Solver
#
#  Created by Blake Williams on 1/10/19.
#  Copyright © 2019 Blake Williams. All rights reserved.
#


import RPi.GPIO as G
from time import sleep


def MotMov50(direction, pinSet):
    dirPin, stepPin, sleepPin = pinSet
    try:
        G.output(sleepPin, 1)   # wake up
        G.output(dirPin, direction)
        delay = .005
        for i in range(50):
            G.output(stepPin, 1)
            sleep(delay)
            G.output(stepPin, 0)
            sleep(delay)
        G.output(sleepPin, 0)   # put to sleep
    except KeyboardInterrupt:
        G.cleanup()


def MotMov180(pinSet):
    dirPin, stepPin, sleepPin = pinSet
    try:
        G.output(sleepPin, 1)   # wake up
        G.output(dirPin, 1)
        delay = .005
        for i in range(100):
            G.output(stepPin, 1)
            sleep(delay)
            G.output(stepPin, 0)
            sleep(delay)
        G.output(sleepPin, 0)   # put to sleep
    except KeyboardInterrupt:
        G.cleanup()


def PrintToBot(moves):
    # Broadcom Memory
    G.setmode(G.BCM)

    # (Dir, Step, Sleep)
    Uset = (2, 3, 4)
    Dset = (18, 15, 14)
    Lset = (17, 27, 22)
    Rset = (7, 8, 25)
    Fset = (5, 6, 13)
    Bset = (21, 20, 16)

    for i in Uset:              # setting pins as outputs
        G.setup(i, G.OUT)
        G.output(i, 0)
    for i in Dset:
        G.setup(i, G.OUT)
        G.output(i, 0)
    for i in Lset:
        G.setup(i, G.OUT)
        G.output(i, 0)
    for i in Rset:
        G.setup(i, G.OUT)
        G.output(i, 0)
    for i in Fset:
        G.setup(i, G.OUT)
        G.output(i, 0)
    for i in Bset:
        G.setup(i, G.OUT)
        G.output(i, 0)

    try:
        for code in moves:      # GPIO Broadcom pins
            if code[0] == 'U':
                pinSet = Uset
            elif code[0] == 'D':
                pinSet = Dset
            elif code[0] == 'L':
                pinSet = Lset
            elif code[0] == 'R':
                pinSet = Rset
            elif code[0] == 'F':
                pinSet = Fset
            elif code[0] == 'B':
                pinSet = Bset

            if len(code) < 4:
                direction = len(code)-2     # clockwise is 0 counterclockwise is 1
                MotMov50(direction, pinSet)
            else:
                MotMov180(pinSet)

    except KeyboardInterrupt:
        G.cleanup()

    G.cleanup()
