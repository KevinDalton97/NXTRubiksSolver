from moves import *
from rotationFunctions import *
from applyAlgorithm import *
# The functions in this file are used to solve step 4 of the Rubik's Cube

# The 2 algorithms used for each case
def secondLayerCases(cube, case):
    algorithm = []
    if case == 1:  # Right case
        algorithm.append('U R U` R` U` F` U F')
        return cube, algorithm
    else:  # Left case
        algorithm.append('U` L` U L U F U` F`')
        return cube, algorithm

# This functions finds the location of the pieces needed to solve step 4 on the cube
def checkSecondLayerPieces(cube):
    correctSecondLayer = 0

    possiblePiecePositions = [(cube[1][1], cube[4][5]), (cube[1][5], cube[2][1]), (cube[2][5], cube[3][1]),
                              (cube[3][5], cube[4][1]), (cube[5][7], cube[1][3]), (cube[5][1], cube[4][3]),
                              (cube[5][3], cube[3][3]), (cube[5][5], cube[2][3])]

    for i in range(len(possiblePiecePositions)):
        if correctSecondLayer == 4:
            return i, 4
        if possiblePiecePositions[i][0] != 'y' and possiblePiecePositions[i][1] != 'y':
            if i == 0 and possiblePiecePositions[i] == ('r', 'b'):
                correctSecondLayer += 1
                continue
            elif i == 1 and possiblePiecePositions[i] == ('r', 'g'):
                correctSecondLayer += 1
                continue
            elif i == 2 and possiblePiecePositions[i] == ('g', 'o'):
                correctSecondLayer += 1
                continue
            elif i == 3 and possiblePiecePositions[i] == ('o', 'b'):
                correctSecondLayer += 1
                continue
            if correctSecondLayer == 4:
                return i, 4

            else:
                return possiblePiecePositions[i], i
# pieces ('r', 'g'), ('g', 'r'), ('b', 'r'), ('r', 'b'), ('g', 'o'), ('o', 'g'), ('o', 'b'), ('b', 'o')

# Based on the pieces found in the function above, this functions returns an algorithm needed to solve
def secondLayerAlgorithm(cube,piece,position):
    algorithm = []
    if position == 0: # (cube[1][1], cube[4][5])
        if piece == ('r', 'g'):
            cube, caseAlgorithm = secondLayerCases(cube, 2)
            algorithm = algorithm+caseAlgorithm
            algorithm.append('U Y')
            cube, caseAlgorithm = secondLayerCases(cube, 2)
            algorithm = algorithm+caseAlgorithm
            algorithm.append('Y`')
        elif piece == ('g', 'r'):
            cube, caseAlgorithm = secondLayerCases(cube, 2)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('U2')
            cube, caseAlgorithm = secondLayerCases(cube, 1)
            algorithm = algorithm + caseAlgorithm
        elif piece == ('b', 'r'):
            cube, caseAlgorithm = secondLayerCases(cube, 2)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('U2')
            cube, caseAlgorithm = secondLayerCases(cube, 2)
            algorithm = algorithm + caseAlgorithm
        elif piece == ('g', 'o'):
            cube, caseAlgorithm = secondLayerCases(cube, 2)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('Y2')
            cube, caseAlgorithm = secondLayerCases(cube, 2)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('Y2')
        elif piece == ('o', 'g'):
            cube, caseAlgorithm = secondLayerCases(cube, 2)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('U Y')
            cube, caseAlgorithm = secondLayerCases(cube, 1)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('Y`')
        elif piece == ('o', 'b'):
            cube, caseAlgorithm = secondLayerCases(cube, 2)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('U` Y`')
            cube, caseAlgorithm = secondLayerCases(cube, 2)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('Y')
        elif piece == ('b', 'o'):
            cube, caseAlgorithm = secondLayerCases(cube, 2)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('Y2')
            cube, caseAlgorithm = secondLayerCases(cube, 1)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('Y2')
    elif position == 1:  # (cube[1][5], cube[2][1])
        if piece == ('r', 'b'):
            cube, caseAlgorithm = secondLayerCases(cube, 1)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('U` Y`')
            cube, caseAlgorithm = secondLayerCases(cube, 1)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('Y')
        elif piece == ('g', 'r'):
            cube, caseAlgorithm = secondLayerCases(cube, 1)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('U2')
            cube, caseAlgorithm = secondLayerCases(cube, 1)
            algorithm = algorithm + caseAlgorithm
        elif piece == ('b', 'r'):
            cube, caseAlgorithm = secondLayerCases(cube, 1)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('U2')
            cube, caseAlgorithm = secondLayerCases(cube, 2)
            algorithm = algorithm + caseAlgorithm
        elif piece == ('g', 'o'):
            cube, caseAlgorithm = secondLayerCases(cube, 1)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('Y2')
            cube, caseAlgorithm = secondLayerCases(cube, 2)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('Y2')
        elif piece == ('o', 'g'):
            cube, caseAlgorithm = secondLayerCases(cube, 1)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('U Y')
            cube, caseAlgorithm = secondLayerCases(cube, 1)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('Y`')
        elif piece == ('o', 'b'):
            cube, caseAlgorithm = secondLayerCases(cube, 1)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('U` Y`')
            cube, caseAlgorithm = secondLayerCases(cube, 2)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('Y')
        elif piece == ('b', 'o'):
            cube, caseAlgorithm = secondLayerCases(cube, 1)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('Y2')
            cube, caseAlgorithm = secondLayerCases(cube, 1)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('Y2')
    elif position == 2:  # (cube[2][5], cube[3][1])
        if piece == ('r', 'b'):
            algorithm.append('Y')
            cube, caseAlgorithm = secondLayerCases(cube, 1)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('Y2')
            cube, caseAlgorithm = secondLayerCases(cube, 1)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('Y')
        elif piece == ('g', 'r'):
            algorithm.append('Y')
            cube, caseAlgorithm = secondLayerCases(cube, 1)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('U` Y`')
            cube, caseAlgorithm = secondLayerCases(cube, 1)
            algorithm = algorithm + caseAlgorithm
        elif piece == ('b', 'r'):
            algorithm.append('Y')
            cube, caseAlgorithm = secondLayerCases(cube, 1)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('U` Y`')
            cube, caseAlgorithm = secondLayerCases(cube, 2)
            algorithm = algorithm + caseAlgorithm
        elif piece == ('r', 'g'):
            algorithm.append('Y')
            cube, caseAlgorithm = secondLayerCases(cube, 1)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('U2')
            cube, caseAlgorithm = secondLayerCases(cube, 2)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('Y`')
        elif piece == ('o', 'g'):
            algorithm.append('Y')
            cube, caseAlgorithm = secondLayerCases(cube, 1)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('U2')
            cube, caseAlgorithm = secondLayerCases(cube, 1)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('Y`')
        elif piece == ('o', 'b'):
            algorithm.append('Y')
            cube, caseAlgorithm = secondLayerCases(cube, 1)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('Y2')
            cube, caseAlgorithm = secondLayerCases(cube, 2)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('Y')
        elif piece == ('b', 'o'):
            algorithm.append('Y')
            cube, caseAlgorithm = secondLayerCases(cube, 1)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('U Y')
            cube, caseAlgorithm = secondLayerCases(cube, 1)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('Y2')
    elif position == 3:  # (cube[3][5], cube[4][1])
        if piece == ('r', 'b'):
            algorithm.append('Y2')
            cube, caseAlgorithm = secondLayerCases(cube, 1)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('U Y')
            cube, caseAlgorithm = secondLayerCases(cube, 1)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('Y')
        elif piece == ('g', 'r'):
            algorithm.append('Y2')
            cube, caseAlgorithm = secondLayerCases(cube, 1)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('Y2')
            cube, caseAlgorithm = secondLayerCases(cube, 1)
            algorithm = algorithm + caseAlgorithm
        elif piece == ('b', 'r'):
            algorithm.append('Y2')
            cube, caseAlgorithm = secondLayerCases(cube, 1)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('Y2')
            cube, caseAlgorithm = secondLayerCases(cube, 2)
            algorithm = algorithm + caseAlgorithm
        elif piece == ('r', 'g'):
            algorithm.append('Y2')
            cube, caseAlgorithm = secondLayerCases(cube, 1)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('U Y`')
            cube, caseAlgorithm = secondLayerCases(cube, 2)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('Y`')
        elif piece == ('o', 'g'):
            algorithm.append('Y2')
            cube, caseAlgorithm = secondLayerCases(cube, 1)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('U Y`')
            cube, caseAlgorithm = secondLayerCases(cube, 1)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('Y`')
        elif piece == ('g', 'o'):
            algorithm.append('Y2')
            cube, caseAlgorithm = secondLayerCases(cube, 1)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('U2')
            cube, caseAlgorithm = secondLayerCases(cube, 2)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('Y2')
        elif piece == ('b', 'o'):
            algorithm.append('Y2')
            cube, caseAlgorithm = secondLayerCases(cube, 1)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('U2')
            cube, caseAlgorithm = secondLayerCases(cube, 1)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('Y2')
    elif position == 4:  # (cube[5][7], cube[1][3])
        if piece == ('r', 'g'):
            algorithm.append('U` Y')
            cube, caseAlgorithm = secondLayerCases(cube, 2)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('Y`')
        elif piece == ('g', 'r'):
            cube, caseAlgorithm = secondLayerCases(cube, 1)
            algorithm = algorithm + caseAlgorithm
        elif piece == ('b', 'r'):
            cube, caseAlgorithm = secondLayerCases(cube, 2)
            algorithm = algorithm + caseAlgorithm
        elif piece == ('r', 'b'):
            algorithm.append('U Y`')
            cube, caseAlgorithm = secondLayerCases(cube, 1)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('Y')
        elif piece == ('g', 'o'):
            algorithm.append('Y2')
            cube, caseAlgorithm = secondLayerCases(cube, 1)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('Y2')
        elif piece == ('o', 'g'):
            algorithm.append('U` Y')
            cube, caseAlgorithm = secondLayerCases(cube, 1)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('Y`')
        elif piece == ('o', 'b'):
            algorithm.append('U Y`')
            cube, caseAlgorithm = secondLayerCases(cube, 2)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('Y')
        elif piece == ('b', 'o'):
            algorithm.append('Y2')
            cube, caseAlgorithm = secondLayerCases(cube, 2)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('Y2')
    elif position == 5:  # (cube[5][1], cube[4][3])
        if piece == ('r', 'g'):
            algorithm.append('U2 Y')
            cube, caseAlgorithm = secondLayerCases(cube, 2)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('Y`')
        elif piece == ('g', 'r'):
            algorithm.append('U`')
            cube, caseAlgorithm = secondLayerCases(cube, 1)
            algorithm = algorithm + caseAlgorithm
        elif piece == ('b', 'r'):
            algorithm.append('U`')
            cube, caseAlgorithm = secondLayerCases(cube, 2)
            algorithm = algorithm + caseAlgorithm
        elif piece == ('r', 'b'):
            algorithm.append('Y`')
            cube, caseAlgorithm = secondLayerCases(cube, 1)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('Y')
        elif piece == ('g', 'o'):
            algorithm.append('U Y2')
            cube, caseAlgorithm = secondLayerCases(cube, 2)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('U Y2')
        elif piece == ('o', 'g'):
            algorithm.append('U2 Y')
            cube, caseAlgorithm = secondLayerCases(cube, 1)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('Y`')
        elif piece == ('o', 'b'):
            algorithm.append('Y`')
            cube, caseAlgorithm = secondLayerCases(cube, 2)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('Y')
        elif piece == ('b', 'o'):
            algorithm.append('U Y2')
            cube, caseAlgorithm = secondLayerCases(cube, 1)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('Y2')
    elif position == 6:  # (cube[5][3], cube[3][3])
        if piece == ('r', 'g'):
            algorithm.append('U Y')
            cube, caseAlgorithm = secondLayerCases(cube, 2)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('Y`')
        elif piece == ('g', 'r'):
            algorithm.append('U2')
            cube, caseAlgorithm = secondLayerCases(cube, 1)
            algorithm = algorithm + caseAlgorithm
        elif piece == ('b', 'r'):
            algorithm.append('U2')
            cube, caseAlgorithm = secondLayerCases(cube, 2)
            algorithm = algorithm + caseAlgorithm
        elif piece == ('r', 'b'):
            algorithm.append('U` Y`')
            cube, caseAlgorithm = secondLayerCases(cube, 1)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('Y')
        elif piece == ('g', 'o'):
            algorithm.append('Y2')
            cube, caseAlgorithm = secondLayerCases(cube, 2)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('Y2')
        elif piece == ('o', 'g'):
            algorithm.append('U Y')
            cube, caseAlgorithm = secondLayerCases(cube, 1)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('Y`')
        elif piece == ('o', 'b'):
            algorithm.append('U` Y`')
            cube, caseAlgorithm = secondLayerCases(cube, 2)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('Y')
        elif piece == ('b', 'o'):
            algorithm.append('Y2')
            cube, caseAlgorithm = secondLayerCases(cube, 1)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('Y2')
    elif position == 7:  # (cube[5][5], cube[2][3])
        if piece == ('r', 'g'):
            algorithm.append('Y')
            cube, caseAlgorithm = secondLayerCases(cube, 2)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('Y`')
        elif piece == ('g', 'r'):
            algorithm.append('U')
            cube, caseAlgorithm = secondLayerCases(cube, 1)
            algorithm = algorithm + caseAlgorithm
        elif piece == ('b', 'r'):
            algorithm.append('U')
            cube, caseAlgorithm = secondLayerCases(cube, 2)
            algorithm = algorithm + caseAlgorithm
        elif piece == ('r', 'b'):
            algorithm.append('U2 Y`')
            cube, caseAlgorithm = secondLayerCases(cube, 1)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('Y')
        elif piece == ('g', 'o'):
            algorithm.append('U` Y2')
            cube, caseAlgorithm = secondLayerCases(cube, 2)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('Y2')
        elif piece == ('o', 'g'):
            algorithm.append('Y')
            cube, caseAlgorithm = secondLayerCases(cube, 1)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('Y`')
        elif piece == ('o', 'b'):
            algorithm.append('U2 Y`')
            cube, caseAlgorithm = secondLayerCases(cube, 2)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('Y')
        elif piece == ('b', 'o'):
            algorithm.append('U` Y2')
            cube, caseAlgorithm = secondLayerCases(cube, 1)
            algorithm = algorithm + caseAlgorithm
            algorithm.append('Y2')
    return cube, algorithm

# Repeats the above functions until step 4 is solved
def solveSecondLayerPieces(cube):
    algorithm = []
    while True:
        piece, position = checkSecondLayerPieces(cube)
        cube, returnedAlgorithm = secondLayerAlgorithm(cube,piece,position)
        returnedAlgorithm = [words for segments in returnedAlgorithm for words in segments.split()]
        cube = algorithmCubeMoves(cube, returnedAlgorithm)
        algorithm.append(returnedAlgorithm)
        if cube[1,0] =='r' and cube[1,1] =='r' and cube[1,5] =='r' and cube[1,6] =='r' and cube[2,0] =='g' and cube[2,1] =='g' and cube[2,5] =='g' and cube[2,6] =='g' and cube[3,0] =='o' and cube[3,1] =='o' and cube[3,5] =='o' and cube[3,6] =='o' and cube[4,0] =='b' and cube[4,1] =='b' and cube[4,5] =='b' and cube[4,6] =='b':
            break
    algorithm = list(filter(None, algorithm))

    return cube, algorithm




