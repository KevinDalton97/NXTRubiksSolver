from scrambleCubeTest import *

# This function keeps track of the cube when full cube rotations are performed
# A full cube rotation does not contain a face spin
def cubeFullRotation(cube, rotationCharacter):
    tempWhite = np.copy(cube[0])
    tempRed = np.copy(cube[1])
    tempGreen = np.copy(cube[2])
    tempOrange = np.copy(cube[3])
    tempBlue = np.copy(cube[4])
    tempYellow = np.copy(cube[5])
    if rotationCharacter == 'Y':
        cube[1] = tempGreen
        cube[2] = tempOrange
        cube[3] = tempBlue
        cube[4] = tempRed
        for elements in range(len(cube[0])):
            newval = elements - 2
            if newval < 0:
                newval = newval + 8
            cube[0][newval] = tempWhite[elements]

        for elements in range(len(cube[5])):
            newval = elements + 2
            if newval > 7:
                newval = newval - 8
            cube[5][newval] = tempYellow[elements]

    if rotationCharacter == 'Y`':
        cube[1] = tempBlue
        cube[2] = tempRed
        cube[3] = tempGreen
        cube[4] = tempOrange
        for elements in range(len(cube[0])):
            newval = elements + 2
            if newval > 7:
                newval = newval - 8
            cube[0][newval] = tempWhite[elements]

        for elements in range(len(cube[5])):
            newval = elements - 2
            if newval < 0:
                newval = newval + 8
            cube[5][newval] = tempYellow[elements]
    return cube

