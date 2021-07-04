import numpy as np
# This file contains what happens to the cube when every possible move is applied to it, meaning, it calculates
# where each piece is moved to after a move is applied such as 'front'.
def front(cube):
    tempWhite = np.copy(cube[0])
    tempRed = np.copy(cube[1])
    tempGreen = np.copy(cube[2])
    tempBlue = np.copy(cube[4])
    tempYellow = np.copy(cube[5])
    cube[0][2] = tempGreen[0]
    cube[0][3] = tempGreen[1]
    cube[0][4] = tempGreen[2]
    cube[4][4] = tempWhite[2]
    cube[4][5] = tempWhite[3]
    cube[4][6] = tempWhite[4]
    cube[5][0] = tempBlue[6]
    cube[5][7] = tempBlue[5]
    cube[5][6] = tempBlue[4]
    cube[2][0] = tempYellow[6]
    cube[2][1] = tempYellow[7]
    cube[2][2] = tempYellow[0]
    for elements in range(len(cube[1])):
        newval = elements+2
        if newval > 7:
            newval = newval-8
        cube[1][newval] = tempRed[elements]

    return cube
def right(cube):
    tempWhite = np.copy(cube[0])
    tempOrange = np.copy(cube[3])
    tempYellow = np.copy(cube[5])
    tempRed = np.copy(cube[1])
    tempGreen = np.copy(cube[2])
    cube[0][4] = tempOrange[0]
    cube[0][5] = tempOrange[1]
    cube[0][6] = tempOrange[2]
    cube[1][4] = tempWhite[4]
    cube[1][5] = tempWhite[5]
    cube[1][6] = tempWhite[6]
    cube[5][4] = tempRed[4]
    cube[5][5] = tempRed[5]
    cube[5][6] = tempRed[6]
    cube[3][0] = tempYellow[4]
    cube[3][1] = tempYellow[5]
    cube[3][2] = tempYellow[6]
    for elements in range(len(cube[2])):
        newval = elements+2
        if newval > 7:
            newval = newval-8
        cube[2][newval] = tempGreen[elements]

    return cube

def left(cube):
    tempWhite = np.copy(cube[0])
    tempOrange = np.copy(cube[3])
    tempYellow = np.copy(cube[5])
    tempRed = np.copy(cube[1])
    tempBlue = np.copy(cube[4])
    cube[0][0] = tempRed[0]
    cube[0][1] = tempRed[1]
    cube[0][2] = tempRed[2]
    cube[1][0] = tempYellow[0]
    cube[1][1] = tempYellow[1]
    cube[1][2] = tempYellow[2]
    cube[5][0] = tempOrange[4]
    cube[5][1] = tempOrange[5]
    cube[5][2] = tempOrange[6]
    cube[3][4] = tempWhite[0]
    cube[3][5] = tempWhite[1]
    cube[3][6] = tempWhite[2]
    for elements in range(len(cube[4])):
        newval = elements+2
        if newval > 7:
            newval = newval-8
        cube[4][newval] = tempBlue[elements]

    return cube

def up(cube):
    tempGreen = np.copy(cube[2])
    tempOrange = np.copy(cube[3])
    tempYellow = np.copy(cube[5])
    tempRed = np.copy(cube[1])
    tempBlue = np.copy(cube[4])
    cube[2][2] = tempOrange[2]
    cube[2][3] = tempOrange[3]
    cube[2][4] = tempOrange[4]
    cube[1][2] = tempGreen[2]
    cube[1][3] = tempGreen[3]
    cube[1][4] = tempGreen[4]
    cube[4][2] = tempRed[2]
    cube[4][3] = tempRed[3]
    cube[4][4] = tempRed[4]
    cube[3][2] = tempBlue[2]
    cube[3][3] = tempBlue[3]
    cube[3][4] = tempBlue[4]
    for elements in range(len(cube[5])):
        newval = elements+2
        if newval > 7:
            newval = newval-8
        cube[5][newval] = tempYellow[elements]

    return cube

def back(cube):
    tempWhite = np.copy(cube[0])
    tempBlue = np.copy(cube[4])
    tempYellow = np.copy(cube[5])
    tempOrange = np.copy(cube[3])
    tempGreen = np.copy(cube[2])
    cube[0][0] = tempBlue[2]
    cube[0][7] = tempBlue[1]
    cube[0][6] = tempBlue[0]
    cube[4][0] = tempYellow[2]
    cube[4][1] = tempYellow[3]
    cube[4][2] = tempYellow[4]
    cube[5][2] = tempGreen[4]
    cube[5][3] = tempGreen[5]
    cube[5][4] = tempGreen[6]
    cube[2][6] = tempWhite[0]
    cube[2][5] = tempWhite[7]
    cube[2][4] = tempWhite[6]
    for elements in range(len(cube[3])):
        newval = elements+2
        if newval > 7:
            newval = newval-8
        cube[3][newval] = tempOrange[elements]

    return cube

def down(cube):
    tempGreen = np.copy(cube[2])
    tempOrange = np.copy(cube[3])
    tempWhite = np.copy(cube[0])
    tempRed = np.copy(cube[1])
    tempBlue = np.copy(cube[4])
    cube[2][0] = tempRed[0]
    cube[2][7] = tempRed[7]
    cube[2][6] = tempRed[6]
    cube[1][0] = tempBlue[0]
    cube[1][7] = tempBlue[7]
    cube[1][6] = tempBlue[6]
    cube[4][0] = tempOrange[0]
    cube[4][7] = tempOrange[7]
    cube[4][6] = tempOrange[6]
    cube[3][0] = tempGreen[0]
    cube[3][7] = tempGreen[7]
    cube[3][6] = tempGreen[6]
    for elements in range(len(cube[0])):
        newval = elements+2
        if newval > 7:
            newval = newval-8
        cube[0][newval] = tempWhite[elements]
    return cube

def frontPrime(cube):
    tempWhite = np.copy(cube[0])
    tempBlue = np.copy(cube[4])
    tempYellow = np.copy(cube[5])
    tempRed = np.copy(cube[1])
    tempGreen = np.copy(cube[2])
    cube[0][2] = tempBlue[4]
    cube[0][3] = tempBlue[5]
    cube[0][4] = tempBlue[6]
    cube[4][4] = tempYellow[6]
    cube[4][5] = tempYellow[7]
    cube[4][6] = tempYellow[0]
    cube[5][0] = tempGreen[2]
    cube[5][7] = tempGreen[1]
    cube[5][6] = tempGreen[0]
    cube[2][0] = tempWhite[2]
    cube[2][1] = tempWhite[3]
    cube[2][2] = tempWhite[4]
    for elements in range(len(cube[1])):
        newval = elements - 2
        if newval < 0:
            newval = newval + 8
        cube[1][newval] = tempRed[elements]
    return cube

def rightPrime(cube):
    tempWhite = np.copy(cube[0])
    tempOrange = np.copy(cube[3])
    tempYellow = np.copy(cube[5])
    tempRed = np.copy(cube[1])
    tempGreen = np.copy(cube[2])
    cube[0][4] = tempRed[4]
    cube[0][5] = tempRed[5]
    cube[0][6] = tempRed[6]
    cube[1][4] = tempYellow[4]
    cube[1][5] = tempYellow[5]
    cube[1][6] = tempYellow[6]
    cube[5][4] = tempOrange[0]
    cube[5][5] = tempOrange[1]
    cube[5][6] = tempOrange[2]
    cube[3][0] = tempWhite[4]
    cube[3][1] = tempWhite[5]
    cube[3][2] = tempWhite[6]
    for elements in range(len(cube[2])):
        newval = elements-2
        if newval < 0:
            newval = newval+8
        cube[2][newval] = tempGreen[elements]
    return cube

def leftPrime(cube):
    tempWhite = np.copy(cube[0])
    tempOrange = np.copy(cube[3])
    tempYellow = np.copy(cube[5])
    tempRed = np.copy(cube[1])
    tempBlue = np.copy(cube[4])
    cube[0][0] = tempOrange[4]
    cube[0][1] = tempOrange[5]
    cube[0][2] = tempOrange[6]
    cube[1][0] = tempWhite[0]
    cube[1][1] = tempWhite[1]
    cube[1][2] = tempWhite[2]
    cube[5][0] = tempRed[0]
    cube[5][1] = tempRed[1]
    cube[5][2] = tempRed[2]
    cube[3][4] = tempYellow[0]
    cube[3][5] = tempYellow[1]
    cube[3][6] = tempYellow[2]
    for elements in range(len(cube[4])):
        newval = elements-2
        if newval < 0:
            newval = newval+8
        cube[4][newval] = tempBlue[elements]
    return cube

def upPrime(cube):
    tempGreen = np.copy(cube[2])
    tempOrange = np.copy(cube[3])
    tempYellow = np.copy(cube[5])
    tempRed = np.copy(cube[1])
    tempBlue = np.copy(cube[4])
    cube[2][2] = tempRed[2]
    cube[2][3] = tempRed[3]
    cube[2][4] = tempRed[4]
    cube[1][2] = tempBlue[2]
    cube[1][3] = tempBlue[3]
    cube[1][4] = tempBlue[4]
    cube[4][2] = tempOrange[2]
    cube[4][3] = tempOrange[3]
    cube[4][4] = tempOrange[4]
    cube[3][2] = tempGreen[2]
    cube[3][3] = tempGreen[3]
    cube[3][4] = tempGreen[4]
    for elements in range(len(cube[5])):
        newval = elements-2
        if newval < 0:
            newval = newval+8
        cube[5][newval] = tempYellow[elements]
    return cube

def backPrime(cube):
    tempWhite = np.copy(cube[0])
    tempBlue = np.copy(cube[4])
    tempYellow = np.copy(cube[5])
    tempOrange = np.copy(cube[3])
    tempGreen = np.copy(cube[2])
    cube[0][0] = tempGreen[6]
    cube[0][7] = tempGreen[5]
    cube[0][6] = tempGreen[4]
    cube[4][0] = tempWhite[6]
    cube[4][1] = tempWhite[7]
    cube[4][2] = tempWhite[0]
    cube[5][2] = tempBlue[0]
    cube[5][3] = tempBlue[1]
    cube[5][4] = tempBlue[2]
    cube[2][6] = tempYellow[4]
    cube[2][5] = tempYellow[3]
    cube[2][4] = tempYellow[2]
    for elements in range(len(cube[3])):
        newval = elements-2
        if newval < 0:
            newval = newval+8
        cube[3][newval] = tempOrange[elements]
    return cube

def downPrime(cube):
    tempGreen = np.copy(cube[2])
    tempOrange = np.copy(cube[3])
    tempWhite = np.copy(cube[0])
    tempRed = np.copy(cube[1])
    tempBlue = np.copy(cube[4])
    cube[2][0] = tempOrange[0]
    cube[2][7] = tempOrange[7]
    cube[2][6] = tempOrange[6]
    cube[1][0] = tempGreen[0]
    cube[1][7] = tempGreen[7]
    cube[1][6] = tempGreen[6]
    cube[4][0] = tempRed[0]
    cube[4][7] = tempRed[7]
    cube[4][6] = tempRed[6]
    cube[3][0] = tempBlue[0]
    cube[3][7] = tempBlue[7]
    cube[3][6] = tempBlue[6]
    for elements in range(len(cube[0])):
        newval = elements-2
        if newval < 0:
            newval = newval+8
        cube[0][newval] = tempWhite[elements]
    return cube
