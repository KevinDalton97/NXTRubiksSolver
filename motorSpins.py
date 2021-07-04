import nxt
from nxt.motor import *
import time
# Motor A is the one that spins the cube
# Motor B is the one that moves the light sensor
# Port C is the one that flips the cube

# This function flips the cube
def flipCube(brick):
    time.sleep(0.3)
    flipMotor = Motor(brick, PORT_C)
    flipMotor.turn(-30,270)
    time.sleep(0.1)
    flipMotor.turn(30,270)
    time.sleep(0.1)
    flipMotor.turn(30,17)
    time.sleep(0.1)


# This function spins the cube 90 degrees
def spinCube(brick, orientation):
    spinMotor = Motor(brick,PORT_A)
    if orientation == 'clockwise':
        # spinMotor.turn(30, 262, brake=True)
        # time.sleep(1)
        spinMotor.turn(65, 270)
        time.sleep(1)
    if orientation == 'anticlockwise':
        spinMotor.turn(-65, 270)
        time.sleep(1)

# The following 3 functions remained unused but were intended
# to control the colour sensor motor and reset the spin and flip motors
def spinColourMotor(brick, orientation):
    spinMotor = Motor(brick, PORT_B)
    if orientation == 'reset':
        spinMotor.turn(-20, 340)
        time.sleep(0.1)
    if orientation == 'start':
        spinMotor.turn(20, 100)
        time.sleep(0.1)
    if orientation == 'in':
        spinMotor.turn(-20, 100)
        time.sleep(0.1)
    if orientation == 'out':
        spinMotor.turn(20, 100)
        time.sleep(0.1)

def resetFlip(brick):
    flipMotor = Motor(brick, PORT_C)
    flipMotor.turn(30, 20)
    time.sleep(0.1)

def resetSpin(brick):
    spinMotor = Motor(brick,PORT_A)
    spinMotor.turn(-20,35)
    time.sleep(0.1)

