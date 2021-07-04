from rotationFunctions import *
import time
from trackCube import *

#This function takes in a set of moves and cube and applies
# the moves to the software representation of the cube.
def algorithmCubeMoves(cube, algorithm):
    for i in range(len(algorithm)):
        if algorithm[i] == 'U':
            cube = up(cube)
        elif algorithm[i] == 'U`':
            cube = upPrime(cube)
        elif algorithm[i] == 'R':
            cube = right(cube)
        elif algorithm[i] == 'R`':
            cube = rightPrime(cube)
        elif algorithm[i] == 'L':
            cube = left(cube)
        elif algorithm[i] == 'L`':
            cube = leftPrime(cube)
        elif algorithm[i] == 'F':
            cube = front(cube)
        elif algorithm[i] == 'F`':
            cube = frontPrime(cube)
        elif algorithm[i] == 'D':
            cube = down(cube)
        elif algorithm[i] == 'D`':
            cube = downPrime(cube)
        elif algorithm[i] == 'B':
            cube = back(cube)
        elif algorithm[i] == 'B`':
            cube = backPrime(cube)
        elif algorithm[i] == 'Y':
            cube = cubeFullRotation(cube, 'Y')
        elif algorithm[i] == 'Y`':
            cube = cubeFullRotation(cube, 'Y`')
        elif algorithm[i] == 'Y2':
            cube = cubeFullRotation(cube, 'Y')
            cube = cubeFullRotation(cube, 'Y')
        elif algorithm[i] == 'U2':
            cube = up(cube)
            cube = up(cube)
        elif algorithm[i] == 'R2':
            cube = right(cube)
            cube = right(cube)
        elif algorithm[i] == 'L2':
            cube = left(cube)
            cube = left(cube)
        elif algorithm[i] == 'F2':
            cube = front(cube)
            cube = front(cube)
        elif algorithm[i] == 'D2':
            cube = down(cube)
            cube = down(cube)
        elif algorithm[i] == 'B2':
            cube = back(cube)
            cube = back(cube)
    return cube

# Converts a set of moves to a string, removes all non move elements and
# converts back to array
def algorithmToString(algorithm):
    algorithm = list(map(' '.join, algorithm))
    algorithm = " ".join(algorithm)
    algorithm=algorithm.split()
    return algorithm

# Applies a facespin on the cube with the robot
def faceSpin(brick, orientation, facePositions):
    spinMotor = Motor(brick,PORT_A)
    flipMotor = Motor(brick, PORT_C)
    time.sleep(0.5)
    flipMotor.turn(-30, 120)
    time.sleep(0.1)
    if orientation == 'clockwise':
        # spinMotor.turn(30,279)
        # time.sleep(0.1)
        # flipMotor.turn(30,125)
        # time.sleep(0.1)
        # spinMotor.turn(-30,23)
        # flipMotor.turn(30,20)
        spinMotor.turn(60,277)
        time.sleep(0.1)
        flipMotor.turn(30,125)
        time.sleep(0.1)
        spinMotor.turn(-60,24)
        flipMotor.turn(30,20)
        facePositions = cubeFacePositions(facePositions,'clockwise')
    if orientation == 'anticlockwise':
        # spinMotor.turn(-30,279)
        # time.sleep(0.1)
        # flipMotor.turn(30,125)
        # time.sleep(0.1)
        # spinMotor.turn(30,25)
        # flipMotor.turn(30,20)
        spinMotor.turn(-60,277)
        time.sleep(0.1)
        flipMotor.turn(30,125)
        time.sleep(0.1)
        spinMotor.turn(60,26)
        flipMotor.turn(30,20)
        facePositions = cubeFacePositions(facePositions,'anticlockwise')

# This function contains all the possible moves that can be applied
# to the cube by the robot and calls the correct one based on the next move in the algorithm
def applyAlgorithmMove(i, facePositions, algorithm, brick, count):
    if algorithm[i] == 'U':
        faceSpin(brick, 'clockwise', facePositions)
        count = count + 1
    elif algorithm[i] == 'U`':
        faceSpin(brick, 'anticlockwise', facePositions)
        count = count - 1
    elif algorithm[i] == 'R':
        faceSpin(brick, 'clockwise', facePositions)
        count = count + 1
    elif algorithm[i] == 'R`':
        faceSpin(brick, 'anticlockwise', facePositions)
        count = count - 1
    elif algorithm[i] == 'L':
        faceSpin(brick, 'clockwise', facePositions)
        count = count + 1
    elif algorithm[i] == 'L`':
        faceSpin(brick, 'anticlockwise', facePositions)
        count = count - 1
    elif algorithm[i] == 'F':
        faceSpin(brick, 'clockwise', facePositions)
        count = count + 1
    elif algorithm[i] == 'F`':
        faceSpin(brick, 'anticlockwise', facePositions)
        count = count - 1
    elif algorithm[i] == 'D':
        faceSpin(brick, 'clockwise', facePositions)
        count = count + 1
    elif algorithm[i] == 'D`':
        faceSpin(brick, 'anticlockwise', facePositions)
        count = count - 1
    elif algorithm[i] == 'B':
        faceSpin(brick, 'clockwise', facePositions)
        count = count + 1
    elif algorithm[i] == 'B`':
        faceSpin(brick, 'anticlockwise', facePositions)
        count = count - 1
    elif algorithm[i] == 'Y':
        spinCube(brick, 'anticlockwise')
        facePositions = cubeFacePositions(facePositions,'clockwise')
        count = count - 1
    elif algorithm[i] == 'Y`':
        spinCube(brick, 'clockwise')
        facePositions = cubeFacePositions(facePositions,'anticlockwise')
        count = count + 1
    elif algorithm[i] == 'Y2':
        spinCube(brick, 'clockwise')
        spinCube(brick, 'clockwise')
        facePositions = cubeFacePositions(facePositions,'clockwise')
        facePositions = cubeFacePositions(facePositions,'clockwise')
        count = count + 2
    elif algorithm[i] == 'U2':
        faceSpin(brick, 'clockwise', facePositions)
        faceSpin(brick, 'clockwise', facePositions)
        count = count + 2
    elif algorithm[i] == 'R2':
        faceSpin(brick, 'clockwise', facePositions)
        faceSpin(brick, 'clockwise', facePositions)
        count = count + 2
    elif algorithm[i] == 'L2':
        faceSpin(brick, 'clockwise', facePositions)
        faceSpin(brick, 'clockwise', facePositions)
        count = count + 2
    elif algorithm[i] == 'F2':
        faceSpin(brick, 'clockwise', facePositions)
        faceSpin(brick, 'clockwise', facePositions)
        count = count + 2
    elif algorithm[i] == 'D2':
        faceSpin(brick, 'clockwise', facePositions)
        faceSpin(brick, 'clockwise', facePositions)
        count = count + 2
    elif algorithm[i] == 'B2':
        faceSpin(brick, 'clockwise', facePositions)
        faceSpin(brick, 'clockwise', facePositions)
        count = count + 2
    return facePositions, count

# This function takes in the algorithm and makes the robot perform the moves
def algorithmOnRobot(algorithm,facePositions, brick):
    moveCount = 0
    count = 0
    for i in range(len(algorithm)):
        time.sleep(0.5)
        facePositions = facePositionCases(brick, algorithm[i], facePositions)
        facePositions, count = applyAlgorithmMove(i, facePositions, algorithm, brick, count)
        time.sleep(0.1)
        moveCount = moveCount+1
        print(moveCount)
        print('---------------------------------')
