from moves import *
from rotationFunctions import *
from motorSpins import *
from applyAlgorithm import *
# The functions in this file are used to solve step 3 of the Rubik's Cube

# The 3 algorithms used for each case
def whiteCornerCases(cube, case):
    algorithm = []
    if case == 1:
        algorithm.append('F` U` F')
    elif case == 2:
        algorithm.append('R U R`')
    elif case == 3:
        algorithm.append('R U2 R` U` R U R`')
    return cube, algorithm

# This functions finds the location of the pieces needed to solve step 3 on the cube
def findWhiteCorners(cube):
    # need to only check for unsolved pieces
    whiteCornerArray = []
    correctCornerCount = 0
    for i in range(cube.shape[0]):
        if cube[i][0] == 'w':
            if i == 0 and cube[3][6] == 'o' and cube[4][0] == 'b':
                correctCornerCount = correctCornerCount + 1
            else:
                whiteCornerArray.append([i, 0])
                break
        if cube[i][2] == 'w':
            if i == 0 and cube[1][0] == 'r' and cube[4][6] == 'b':
                correctCornerCount = correctCornerCount + 1
            else:
                whiteCornerArray.append([i, 2])
                break
        if cube[i][4] == 'w':
            if i == 0 and cube[1][6] == 'r' and cube[2][0] == 'g':
                correctCornerCount = correctCornerCount + 1
            else:
                whiteCornerArray.append([i, 4])
                break
        if cube[i][6] == 'w':
            if i == 0 and cube[2][6] == 'g' and cube[3][0] == 'o':
                correctCornerCount = correctCornerCount + 1
            else:
                whiteCornerArray.append([i, 6])
                break

    return whiteCornerArray, correctCornerCount

# Based on the pieces found in the function above, this functions returns an algorithm needed to solve
def solveWhiteCorners(whiteCorners, cube):
    algorithm = []
    for i in whiteCorners:
        if i[0] == 0:  # white side
            if i[1] == 0:
                colourPiece = cube[3][6]
                if colourPiece == 'b':
                    algorithm.append('B` U` F U F` B')
                elif colourPiece == 'r':
                    algorithm.append('B` U2 R U R` B')
                elif colourPiece == 'g':
                    algorithm.append('L U2 L` B U` B`')
            elif i[1] == 2:
                colourPiece = cube[4][6]
                if colourPiece == 'o':
                    algorithm.append('F U F` B` U` B')
                elif colourPiece == 'r':
                    algorithm.append('F U` F` U` R U R`')
                elif colourPiece == 'g':
                    algorithm.append('F U2 F` R` U` R')
            elif i[1] == 4:
                colourPiece = cube[1][6]
                if colourPiece == 'b':
                    algorithm.append('R U R` L` U` L')
                elif colourPiece == 'o':
                    algorithm.append('R U2 R` B` U` B')
                elif colourPiece == 'g':
                    algorithm.append('F` U` F B U B`')
            elif i[1] == 6:
                colourPiece = cube[2][6]
                if colourPiece == 'o':
                    algorithm.append('B U B` L U2 L`')
                elif colourPiece == 'r':
                    algorithm.append('B U2 B` R U` R`')
                elif colourPiece == 'b':
                    algorithm.append('B U2 B` L` U` L')
        elif i[0] == 1:  # red side
            if i[1] == 0:
                colourPiece = cube[0][2]
                if colourPiece == 'b':
                    cube, caseAlgorithm = whiteCornerCases(cube, 2)
                    algorithm.append('L` U L Y`')
                    algorithm = algorithm + caseAlgorithm
                    algorithm.append('Y')
                elif colourPiece == 'r':
                    cube, caseAlgorithm = whiteCornerCases(cube, 2)
                    algorithm.append('F U2 F` U')
                    algorithm = algorithm + caseAlgorithm
                elif colourPiece == 'g':
                    cube, caseAlgorithm = whiteCornerCases(cube, 2)
                    algorithm.append('L` U L U2 Y')
                    algorithm = algorithm + caseAlgorithm
                    algorithm.append('Y`')
                elif colourPiece == 'o':
                    cube, caseAlgorithm = whiteCornerCases(cube, 2)
                    algorithm.append('L` U L U Y2')
                    algorithm = algorithm + caseAlgorithm
                    algorithm.append('Y2')
            elif i[1] == 2:
                colourPiece = cube[4][4]
                if colourPiece == 'b':
                    cube, caseAlgorithm = whiteCornerCases(cube, 2)
                    algorithm.append('Y`')
                    algorithm = algorithm + caseAlgorithm
                    algorithm.append('Y')
                elif colourPiece == 'r':
                    cube, caseAlgorithm = whiteCornerCases(cube, 2)
                    algorithm.append('U`')
                    algorithm = algorithm + caseAlgorithm
                elif colourPiece == 'g':
                    cube, caseAlgorithm = whiteCornerCases(cube, 2)
                    algorithm.append('U2 Y')
                    algorithm = algorithm + caseAlgorithm
                    algorithm.append('Y`')
                elif colourPiece == 'o':
                    cube, caseAlgorithm = whiteCornerCases(cube, 2)
                    algorithm.append('U Y2')
                    algorithm = algorithm + caseAlgorithm
                    algorithm.append('Y2')
            elif i[1] == 4:
                colourPiece = cube[5][6]
                if colourPiece == 'b':
                    cube, caseAlgorithm = whiteCornerCases(cube, 1)
                    algorithm.append('U Y`')
                    algorithm = algorithm + caseAlgorithm
                    algorithm.append('Y')
                elif colourPiece == 'r':
                    cube, caseAlgorithm = whiteCornerCases(cube, 1)
                    algorithm = algorithm + caseAlgorithm
                elif colourPiece == 'g':
                    algorithm.append('B U` B`')
                elif colourPiece == 'o':
                    cube, caseAlgorithm = whiteCornerCases(cube, 1)
                    algorithm.append('U2 Y2')
                    algorithm = algorithm + caseAlgorithm
                    algorithm.append('Y2')
            elif i[1] == 6:
                colourPiece = cube[0][4]
                if colourPiece == 'b':
                    cube, caseAlgorithm = whiteCornerCases(cube, 3)
                    algorithm.append('R U2 R` Y2')
                    algorithm = algorithm + caseAlgorithm
                    algorithm.append('Y2')
                elif colourPiece == 'r':
                    cube, caseAlgorithm = whiteCornerCases(cube, 3)
                    algorithm.append('R U R` Y`')
                    algorithm = algorithm + caseAlgorithm
                    algorithm.append('Y')
                elif colourPiece == 'g':
                    cube, caseAlgorithm = whiteCornerCases(cube, 3)
                    algorithm.append('R U R` U`')
                    algorithm = algorithm + caseAlgorithm
                elif colourPiece == 'o':
                    cube, caseAlgorithm = whiteCornerCases(cube, 1)
                    algorithm.append('R U` R` U` Y')
                    algorithm = algorithm + caseAlgorithm
                    algorithm.append('Y`')
        elif i[0] == 2:  # green side
            if i[1] == 0:
                colourPiece = cube[0][4]
                if colourPiece == 'b':
                    cube, caseAlgorithm = whiteCornerCases(cube, 2)
                    algorithm.append('R U R` Y`')
                    algorithm = algorithm + caseAlgorithm
                    algorithm.append('Y')
                elif colourPiece == 'r':
                    cube, caseAlgorithm = whiteCornerCases(cube, 2)
                    algorithm.append('R U2 R` U2')
                    algorithm = algorithm + caseAlgorithm
                elif colourPiece == 'g':
                    cube, caseAlgorithm = whiteCornerCases(cube, 2)
                    algorithm.append('R U R` U2 Y')
                    algorithm = algorithm + caseAlgorithm
                    algorithm.append('Y`')
                elif colourPiece == 'o':
                    cube, caseAlgorithm = whiteCornerCases(cube, 2)
                    algorithm.append('R U2 R` Y2')
                    algorithm = algorithm + caseAlgorithm
                    algorithm.append('Y2')
            elif i[1] == 2:
                colourPiece = cube[1][4]
                if colourPiece == 'b':
                    cube, caseAlgorithm = whiteCornerCases(cube, 2)
                    algorithm.append('U Y`')
                    algorithm = algorithm + caseAlgorithm
                    algorithm.append('Y')
                elif colourPiece == 'r':
                    cube, caseAlgorithm = whiteCornerCases(cube, 2)
                    algorithm = algorithm + caseAlgorithm
                elif colourPiece == 'g':
                    cube, caseAlgorithm = whiteCornerCases(cube, 2)
                    algorithm.append('U` Y')
                    algorithm = algorithm + caseAlgorithm
                    algorithm.append('Y`')
                elif colourPiece == 'o':
                    cube, caseAlgorithm = whiteCornerCases(cube, 2)
                    algorithm.append('U2 Y2')
                    algorithm = algorithm + caseAlgorithm
                    algorithm.append('Y2')
            elif i[1] == 4:
                colourPiece = cube[5][4]
                if colourPiece == 'b':
                    cube, caseAlgorithm = whiteCornerCases(cube, 1)
                    algorithm.append('U2 Y`')
                    algorithm = algorithm + caseAlgorithm
                    algorithm.append('Y')
                elif colourPiece == 'r':
                    cube, caseAlgorithm = whiteCornerCases(cube, 1)
                    algorithm.append('U')
                    algorithm = algorithm + caseAlgorithm
                elif colourPiece == 'g':
                    cube, caseAlgorithm = whiteCornerCases(cube, 1)
                    algorithm.append('Y')
                    algorithm = algorithm + caseAlgorithm
                    algorithm.append('Y`')
                elif colourPiece == 'o':
                    cube, caseAlgorithm = whiteCornerCases(cube, 1)
                    algorithm.append('U` Y2')
                    algorithm = algorithm + caseAlgorithm
                    algorithm.append('Y2')
            elif i[1] == 6:
                colourPiece = cube[0][6]
                if colourPiece == 'b':
                    cube, caseAlgorithm = whiteCornerCases(cube, 1)
                    algorithm.append('R` U` R Y2')
                    algorithm = algorithm + caseAlgorithm
                    algorithm.append('Y2')
                elif colourPiece == 'r':
                    cube, caseAlgorithm = whiteCornerCases(cube, 1)
                    algorithm.append('R` U2 R Y`')
                    algorithm = algorithm + caseAlgorithm
                    algorithm.append('Y')
                elif colourPiece == 'g':
                    cube, caseAlgorithm = whiteCornerCases(cube, 1)
                    algorithm.append('R` U2 R U`')
                    algorithm = algorithm + caseAlgorithm
                elif colourPiece == 'o':
                    cube, caseAlgorithm = whiteCornerCases(cube, 1)
                    algorithm.append('R` U` R U Y')
                    algorithm = algorithm + caseAlgorithm
                    algorithm.append('Y`')
        elif i[0] == 3:  # orange side
            if i[1] == 0:
                colourPiece = cube[0][6]
                if colourPiece == 'b':
                    cube, caseAlgorithm = whiteCornerCases(cube, 2)
                    algorithm.append('B U2 B` Y`')
                    algorithm = algorithm + caseAlgorithm
                    algorithm.append('Y')
                elif colourPiece == 'r':
                    cube, caseAlgorithm = whiteCornerCases(cube, 2)
                    algorithm.append('B U B`')
                    algorithm = algorithm + caseAlgorithm
                elif colourPiece == 'g':
                    cube, caseAlgorithm = whiteCornerCases(cube, 2)
                    algorithm.append('B U B` U` Y')
                    algorithm = algorithm + caseAlgorithm
                    algorithm.append('Y`')
                elif colourPiece == 'o':
                    cube, caseAlgorithm = whiteCornerCases(cube, 2)
                    algorithm.append('B U B` U2 Y2')
                    algorithm = algorithm + caseAlgorithm
                    algorithm.append('Y2')
            elif i[1] == 2:
                colourPiece = cube[2][4]
                if colourPiece == 'b':
                    cube, caseAlgorithm = whiteCornerCases(cube, 2)
                    algorithm.append('U2 Y`')
                    algorithm = algorithm + caseAlgorithm
                    algorithm.append('Y')
                elif colourPiece == 'r':
                    cube, caseAlgorithm = whiteCornerCases(cube, 2)
                    algorithm.append('U')
                    algorithm = algorithm + caseAlgorithm
                elif colourPiece == 'g':
                    cube, caseAlgorithm = whiteCornerCases(cube, 2)
                    algorithm.append('Y')
                    algorithm = algorithm + caseAlgorithm
                    algorithm.append('Y`')
                elif colourPiece == 'o':
                    cube, caseAlgorithm = whiteCornerCases(cube, 2)
                    algorithm.append('U` Y2')
                    algorithm = algorithm + caseAlgorithm
                    algorithm.append('Y2')
            elif i[1] == 4:
                colourPiece = cube[5][2]
                if colourPiece == 'b':
                    cube, caseAlgorithm = whiteCornerCases(cube, 1)
                    algorithm.append('U` Y`')
                    algorithm = algorithm + caseAlgorithm
                    algorithm.append('Y')
                elif colourPiece == 'r':
                    cube, caseAlgorithm = whiteCornerCases(cube, 1)
                    algorithm.append('U2')
                    algorithm = algorithm + caseAlgorithm
                elif colourPiece == 'g':
                    cube, caseAlgorithm = whiteCornerCases(cube, 1)
                    algorithm.append('U Y')
                    algorithm = algorithm + caseAlgorithm
                    algorithm.append('Y`')
                elif colourPiece == 'o':
                    cube, caseAlgorithm = whiteCornerCases(cube, 1)
                    algorithm.append('Y2')
                    algorithm = algorithm + caseAlgorithm
                    algorithm.append('Y2')
            elif i[1] == 6:
                colourPiece = cube[0][0]
                if colourPiece == 'b':
                    cube, caseAlgorithm = whiteCornerCases(cube, 1)
                    algorithm.append('L U` L` Y2')
                    algorithm = algorithm + caseAlgorithm
                    algorithm.append('Y2')
                elif colourPiece == 'r':
                    cube, caseAlgorithm = whiteCornerCases(cube, 1)
                    algorithm.append('L U` L` U` Y`')
                    algorithm = algorithm + caseAlgorithm
                    algorithm.append('Y')
                elif colourPiece == 'g':
                    cube, caseAlgorithm = whiteCornerCases(cube, 1)
                    algorithm.append('L U` L` U2 ')
                    algorithm = algorithm + caseAlgorithm
                elif colourPiece == 'o':
                    cube, caseAlgorithm = whiteCornerCases(cube, 1)
                    algorithm.append('L U` L` U Y')
                    algorithm = algorithm + caseAlgorithm
                    algorithm.append('Y`')
        elif i[0] == 4:  # blue side
            if i[1] == 0:
                colourPiece = cube[0][0]
                if colourPiece == 'b':
                    cube, caseAlgorithm = whiteCornerCases(cube, 2)
                    algorithm.append('L U L` U2 Y`')
                    algorithm = algorithm + caseAlgorithm
                    algorithm.append('Y')
                elif colourPiece == 'r':
                    cube, caseAlgorithm = whiteCornerCases(cube, 2)
                    algorithm.append('L U2 L`')
                    algorithm = algorithm + caseAlgorithm
                elif colourPiece == 'g':
                    cube, caseAlgorithm = whiteCornerCases(cube, 2)
                    algorithm.append('L U L` Y')
                    algorithm = algorithm + caseAlgorithm
                    algorithm.append('Y`')
                elif colourPiece == 'o':
                    cube, caseAlgorithm = whiteCornerCases(cube, 2)
                    algorithm.append('L U L` U` Y2')
                    algorithm = algorithm + caseAlgorithm
                    algorithm.append('Y2')
            elif i[1] == 2:
                colourPiece = cube[5][2]
                if colourPiece == 'b':
                    cube, caseAlgorithm = whiteCornerCases(cube, 2)
                    algorithm.append('Y2')
                    algorithm = algorithm + caseAlgorithm
                    algorithm.append('Y2')
                elif colourPiece == 'r':
                    cube, caseAlgorithm = whiteCornerCases(cube, 2)
                    algorithm.append('U` Y`')
                    algorithm = algorithm + caseAlgorithm
                    algorithm.append('Y')
                elif colourPiece == 'g':
                    cube, caseAlgorithm = whiteCornerCases(cube, 2)
                    algorithm.append('U2')
                    algorithm = algorithm + caseAlgorithm
                elif colourPiece == 'o':
                    cube, caseAlgorithm = whiteCornerCases(cube, 2)
                    algorithm.append('U Y')
                    algorithm = algorithm + caseAlgorithm
                    algorithm.append('Y`')
            elif i[1] == 4:
                colourPiece = cube[5][0]
                if colourPiece == 'b':
                    cube, caseAlgorithm = whiteCornerCases(cube, 1)
                    algorithm.append('Y`')
                    algorithm = algorithm + caseAlgorithm
                    algorithm.append('Y')
                elif colourPiece == 'r':
                    cube, caseAlgorithm = whiteCornerCases(cube, 1)
                    algorithm.append('U`')
                    algorithm = algorithm + caseAlgorithm
                elif colourPiece == 'g':
                    cube, caseAlgorithm = whiteCornerCases(cube, 1)
                    algorithm.append('U2 Y')
                    algorithm = algorithm + caseAlgorithm
                    algorithm.append('Y`')
                elif colourPiece == 'o':
                    cube, caseAlgorithm = whiteCornerCases(cube, 1)
                    algorithm.append('U Y2')
                    algorithm = algorithm + caseAlgorithm
                    algorithm.append('Y2')
            elif i[1] == 6:
                colourPiece = cube[0][2]
                if colourPiece == 'b':
                    cube, caseAlgorithm = whiteCornerCases(cube, 1)
                    algorithm.append('L` U2 L U` Y2')
                    algorithm = algorithm + caseAlgorithm
                    algorithm.append('Y2')
                elif colourPiece == 'r':
                    cube, caseAlgorithm = whiteCornerCases(cube, 1)
                    algorithm.append('F U` F` Y`')
                    algorithm = algorithm + caseAlgorithm
                    algorithm.append('Y')
                elif colourPiece == 'g':
                    cube, caseAlgorithm = whiteCornerCases(cube, 1)
                    algorithm.append('L` U` L')
                    algorithm = algorithm + caseAlgorithm
                elif colourPiece == 'o':
                    cube, caseAlgorithm = whiteCornerCases(cube, 1)
                    algorithm.append('L` U2 L Y')
                    algorithm = algorithm + caseAlgorithm
                    algorithm.append('Y`')
        elif i[0] == 5:  # yellow side
            if i[1] == 0:
                colourPiece = cube[1][2]
                if colourPiece == 'b':
                    cube, caseAlgorithm = whiteCornerCases(cube, 3)
                    algorithm.append('Y`')
                    algorithm = algorithm + caseAlgorithm
                    algorithm.append('Y')
                elif colourPiece == 'r':
                    cube, caseAlgorithm = whiteCornerCases(cube, 3)
                    algorithm.append('U`')
                    algorithm = algorithm + caseAlgorithm
                elif colourPiece == 'g':
                    cube, caseAlgorithm = whiteCornerCases(cube, 3)
                    algorithm.append('U2 Y')
                    algorithm = algorithm + caseAlgorithm
                    algorithm.append('Y`')
                elif colourPiece == 'o':
                    cube, caseAlgorithm = whiteCornerCases(cube, 3)
                    algorithm.append('U Y2')
                    algorithm = algorithm + caseAlgorithm
                    algorithm.append('Y2')
            elif i[1] == 2:
                colourPiece = cube[4][2]
                if colourPiece == 'b':
                    cube, caseAlgorithm = whiteCornerCases(cube, 3)
                    algorithm.append('U` Y`')
                    algorithm = algorithm + caseAlgorithm
                    algorithm.append('Y')
                elif colourPiece == 'r':
                    cube, caseAlgorithm = whiteCornerCases(cube, 3)
                    algorithm.append('U2')
                    algorithm = algorithm + caseAlgorithm
                elif colourPiece == 'g':
                    cube, caseAlgorithm = whiteCornerCases(cube, 3)
                    algorithm.append('U Y')
                    algorithm = algorithm + caseAlgorithm
                    algorithm.append('Y`')
                elif colourPiece == 'o':
                    cube, caseAlgorithm = whiteCornerCases(cube, 3)
                    algorithm.append('Y2')
                    algorithm = algorithm + caseAlgorithm
                    algorithm.append('Y2')
            elif i[1] == 4:
                colourPiece = cube[3][2]
                if colourPiece == 'b':
                    cube, caseAlgorithm = whiteCornerCases(cube, 3)
                    algorithm.append('U2 Y`')
                    algorithm = algorithm + caseAlgorithm
                    algorithm.append('Y')
                elif colourPiece == 'r':
                    cube, caseAlgorithm = whiteCornerCases(cube, 3)
                    algorithm.append('U')
                    algorithm = algorithm + caseAlgorithm
                elif colourPiece == 'g':
                    cube, caseAlgorithm = whiteCornerCases(cube, 3)
                    algorithm.append('Y')
                    algorithm = algorithm + caseAlgorithm
                    algorithm.append('Y`')
                elif colourPiece == 'o':
                    cube, caseAlgorithm = whiteCornerCases(cube, 3)
                    algorithm.append('U` Y2')
                    algorithm = algorithm + caseAlgorithm
                    algorithm.append('Y2')
            elif i[1] == 6:
                colourPiece = cube[1][4]
                if colourPiece == 'b':
                    cube, caseAlgorithm = whiteCornerCases(cube, 3)
                    algorithm.append('U2 Y2')
                    algorithm = algorithm + caseAlgorithm
                    algorithm.append('Y2')
                elif colourPiece == 'r':
                    cube, caseAlgorithm = whiteCornerCases(cube, 3)
                    algorithm.append('U Y`')
                    algorithm = algorithm + caseAlgorithm
                    algorithm.append('Y')
                elif colourPiece == 'g':
                    cube, caseAlgorithm = whiteCornerCases(cube, 3)
                    algorithm = algorithm + caseAlgorithm
                elif colourPiece == 'o':
                    cube, caseAlgorithm = whiteCornerCases(cube, 3)
                    algorithm.append('U` Y')
                    algorithm = algorithm + caseAlgorithm
                    algorithm.append('Y`')
    return algorithm, cube

# Repeats the above functions until step 3 is solved
def solveWhiteSide(cube):
    fullWhiteCornerAlgorithm = []
    correctCornerCount = 0
    while correctCornerCount != 4:
        singleCornerAlgorithm, correctCornerCount = findWhiteCorners(cube)
        solveAlgorithm, cube = solveWhiteCorners(singleCornerAlgorithm, cube)
        solveAlgorithm = [words for segments in solveAlgorithm for words in segments.split()]
        cube = algorithmCubeMoves(cube, solveAlgorithm)
        if not solveAlgorithm:
            pass
        else:
            fullWhiteCornerAlgorithm.append(solveAlgorithm)
    return fullWhiteCornerAlgorithm, cube
