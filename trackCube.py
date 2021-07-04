from motorSpins import *
import numpy as np
# These functions keep track of where each side is as the cube is moved

# This function keeps track of the cube as it is spun and flipped
def cubeFacePositions(facePositions, move):
    tempDown = np.copy(facePositions[0])
    tempFront = np.copy(facePositions[1])
    tempRight = np.copy(facePositions[2])
    tempBack = np.copy(facePositions[3])
    tempLeft = np.copy(facePositions[4])
    tempUp = np.copy(facePositions[5])
    if move == 'clockwiseSpin':
        facePositions[1] = tempRight
        facePositions[2] = tempBack
        facePositions[3] = tempLeft
        facePositions[4] = tempFront
    elif move == 'anticlockwiseSpin':
        facePositions[1] = tempLeft
        facePositions[2] = tempFront
        facePositions[3] = tempRight
        facePositions[4] = tempBack
    elif move == 'flip':
        facePositions[0] = tempBack
        facePositions[1] = tempDown
        facePositions[3] = tempUp
        facePositions[5] = tempFront

    return facePositions

# This fucntion returns the moves needed to position of the side of the cube to be spun on the spinning platform
def facePositionCases(brick, nextMove, facePositions):
    if nextMove == 'D' or nextMove == 'D`' or nextMove == 'D2' or nextMove == 'Y' or nextMove == 'Y`' or nextMove == 'Y2':
        nextMoveIndex = np.where(facePositions == 'D')
    elif nextMove == 'F' or nextMove == 'F`' or nextMove == 'F2':
        nextMoveIndex = np.where(facePositions == 'F')
    elif nextMove == 'R' or nextMove == 'R`' or nextMove == 'R2':
        nextMoveIndex = np.where(facePositions == 'R')
    elif nextMove == 'B' or nextMove == 'B`' or nextMove == 'B2':
        nextMoveIndex = np.where(facePositions == 'B')
    elif nextMove == 'L' or nextMove == 'L`' or nextMove == 'L2':
        nextMoveIndex = np.where(facePositions == 'L')
    elif nextMove == 'U' or nextMove == 'U`' or nextMove == 'U2':
        nextMoveIndex = np.where(facePositions == 'U')
    nextMoveIndex = nextMoveIndex[0]
    if nextMoveIndex == 0:
        pass
    elif nextMoveIndex == 1:
        spinCube(brick,'clockwise')
        cubeFacePositions(facePositions, 'clockwiseSpin')
        spinCube(brick,'clockwise')
        cubeFacePositions(facePositions, 'clockwiseSpin')
        flipCube(brick)
        cubeFacePositions(facePositions, 'flip')
    elif nextMoveIndex == 2:

        spinCube(brick,'clockwise')
        cubeFacePositions(facePositions, 'anticlockwiseSpin')
        flipCube(brick)
        cubeFacePositions(facePositions, 'flip')
    elif nextMoveIndex == 3:
        flipCube(brick)
        cubeFacePositions(facePositions, 'flip')
    elif nextMoveIndex == 4:
        spinCube(brick,'anticlockwise')
        cubeFacePositions(facePositions, 'clockwiseSpin')
        flipCube(brick)
        cubeFacePositions(facePositions, 'flip')
    elif nextMoveIndex == 5:
        flipCube(brick)
        time.sleep(0.3)
        cubeFacePositions(facePositions, 'flip')
        flipCube(brick)
        cubeFacePositions(facePositions, 'flip')
    return facePositions

