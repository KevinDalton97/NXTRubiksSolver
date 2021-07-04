from nxt.sensor import Color20
from nxt.sensor import Type
from motorSpins import *
from nxt.motor import *
import numpy as np


# This function returns the colour that the colour sensor is facing
def getColour(b):
    colour = Color20(b, 0x00)
    type_ = Type.COLORFULL
    colour.set_light_color(type_)
    rawColour = colour.get_color().scaled_value
    if rawColour == 1:
        return 'o'
    elif rawColour == 2:
        return 'b'
    elif rawColour == 3:
        return 'g'
    elif rawColour == 4:
        return 'y'
    elif rawColour == 5:
        return 'r'
    elif rawColour == 6:
        return 'w'


# Turns off the colour sensor
def turnOffColourSensor(b):
    colour = Color20(b, 0x00)
    type_ = Type.COLORNONE
    colour.set_light_color(type_)

# This function positions the colour sensor above each piece during the scan phase
def scanFaceSpinMotor(brick, integer):
    spinCubeMotor = Motor(brick, PORT_A)
    spinColourMotor = Motor(brick, PORT_B)

    if integer == 0:
        spinCubeMotor.turn(20, 120)
        spinColourMotor.turn(20, 22)
    elif integer == 1:
        spinCubeMotor.turn(20, 130)
        spinColourMotor.turn(-20, 30)
    elif integer == 2:
        spinCubeMotor.turn(20, 115)
        spinColourMotor.turn(20, 26)
    elif integer == 3:
        spinCubeMotor.turn(20, 155)
        spinColourMotor.turn(-20, 22)
    elif integer == 4:
        spinCubeMotor.turn(20, 130)
        spinColourMotor.turn(20, 35)
    elif integer == 5:
        spinCubeMotor.turn(20, 125)
        spinColourMotor.turn(-20, 25)
    elif integer == 6:
        spinCubeMotor.turn(20, 130)
        spinColourMotor.turn(20, 20)

# Scans each colour on the cube
def scanCubeFace(brick):
    flipMotor = Motor(brick, PORT_C)
    spinColourMotor = Motor(brick, PORT_B)
    spinMotor = Motor(brick, PORT_A)

    colour = Color20(brick, 0x00)
    type_ = Type.COLORFULL
    colour.set_light_color(type_)
    spinColourMotor.turn(20, 280)
    fullColour = []
    for i in range(6):
        #print(i)
        faceColours = []
        time.sleep(0.2)
        spinColourMotor.turn(-20, 80)
        time.sleep(0.2)
        for j in range(4):
            spinCube(brick, 'clockwise')
            a = getColour(brick)
            faceColours.append(a)

        spinColourMotor.turn(-20, 20)
        spinMotor.turn(30, 100)
        time.sleep(0.2)

        for j in range(4):
            a = getColour(brick)
            piecePos = j * 2
            faceColours.insert(piecePos, a)
            spinCube(brick, 'clockwise')
            #print(a)
        fullColour.append(faceColours)
        spinMotor.turn(-30, 105)
        spinColourMotor.turn(-20, 105)
        ##print(fullColour)
        flipCube(brick)

        if i == 2:
            spinCube(brick, 'clockwise')
            spinCube(brick, 'clockwise')

        if i == 3:
            spinCube(brick, 'anticlockwise')
            flipCube(brick)
            spinCube(brick, 'clockwise')
            spinCube(brick, 'clockwise')

        if i == 4:
            flipCube(brick)
            spinCube(brick, 'clockwise')
            spinCube(brick, 'clockwise')
        if i != 5:
            spinColourMotor.turn(20, 200)

    turnOffColourSensor(brick)
    flipCube(brick)
    flipCube(brick)
    spinCube(brick, 'clockwise')
    flipMotor.turn(1, 1, False)
    spinMotor.turn(1, 1, False)
    #print(fullColour)
    spinColourMotor.turn(-1, 1, False)

    time.sleep(5)
    fullColour = np.reshape(fullColour, (6, 8))
    #     unique, counts = np.unique(a, return_counts=True)
    #     result = np.all(counts == counts[0])
    #     print(a)
    #     print(result)
    # spinColourMotor.turn(20, 60)
    return faceColours
