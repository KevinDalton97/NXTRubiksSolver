from nxt.sensor import Color20
from nxt.sensor import Type
from motorSpins import *
from nxt.motor import *
import numpy as np
from colourDetection import *
w = 'w'
r = 'r'
g = 'g'
o = 'o'
b = 'b'
y = 'y'

brick = nxt.locator.find_one_brick()
flipMotor = Motor(brick, PORT_C)
spinColourMotor = Motor(brick, PORT_B)
spinMotor = Motor(brick, PORT_A)


colour = Color20(brick, 0x00)
type_ = Type.COLORFULL
colour.set_light_color(type_)
spinColourMotor.turn(20, 280)
fullColour = []
for i in range(6):
    print(i)
    faceColours = []
    time.sleep(0.2)
    spinColourMotor.turn(-20, 80)
    time.sleep(0.2)
    for j in range(4):

        spinCube(brick,'clockwise')
        a = getColour(brick)
        faceColours.append(a)

    spinColourMotor.turn(-20, 20)
    spinMotor.turn(60, 100)
    time.sleep(0.2)

    for j in range(4):
        a = getColour(brick)
        piecePos = j * 2
        faceColours.insert(piecePos, a)
        spinCube(brick,'clockwise')
        print(a)
    fullColour.append(faceColours)
    spinMotor.turn(-60, 110)
    spinColourMotor.turn(-20,100)
    print(fullColour)
    flipCube(brick)

    if i == 2:
        spinCube(brick,'clockwise')
        spinCube(brick,'clockwise')

    if i == 3:
        spinCube(brick,'anticlockwise')
        flipCube(brick)
        spinCube(brick,'clockwise')
        spinCube(brick,'clockwise')

    if i == 4:
        flipCube(brick)
        spinCube(brick, 'clockwise')
        spinCube(brick,'clockwise')
    if i !=5:
        spinColourMotor.turn(20,200)

turnOffColourSensor(brick)
flipCube(brick)
flipCube(brick)
spinCube(brick,'clockwise')
flipMotor.turn(1, 1, False)
spinMotor.turn(1, 1, False)
print(fullColour)
spinColourMotor.turn(-1, 1, False)

time.sleep(5)
#F` D B` R` B` L2 D` F2 L F2 U` L2 F` D2 L` B` F` L2 D U` F` D2 R D L2 R2 D` B` U F2
