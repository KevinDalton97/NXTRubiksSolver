from moves import *
from applyAlgorithm import *
# All functions required to solve step 2 of the cube

# This function checks the cube to find where all the white edge pieces are, it only returns unsolved pieces.
def findWhiteEdges(cube):
    # need to only check for unsolved pieces
    whitePieceArray = []
    correctEdgeCount = 0
    for i in range(cube.shape[0]):
        if cube[i][1] == 'w':
            if i == 0 and cube[4][7] == 'b':
                correctEdgeCount = correctEdgeCount + 1
            else:
                whitePieceArray.append([i, 1])
                break
        if cube[i][3] == 'w':
            if i == 0 and cube[1][7] == 'r':
                correctEdgeCount = correctEdgeCount + 1
            else:
                whitePieceArray.append([i, 3])
                break
        if cube[i][5] == 'w':
            if i == 0 and cube[2][7] == 'g':
                correctEdgeCount = correctEdgeCount + 1
            else:
                whitePieceArray.append([i, 5])
                break
        if cube[i][7] == 'w':
            if i == 0 and cube[3][7] == 'o':
                correctEdgeCount = correctEdgeCount + 1
            else:
                whitePieceArray.append([i, 7])
                break

    return whitePieceArray, correctEdgeCount


# This function solves the white cross step using the pieces found in the previous function. cube[i][j] represents the
# pieces, where i is the side and j is the piece on the side, i 0-5 for the sides white, red, green, orange,
# blue and yellow and 0-7 for the pieces on each side starting at the bottom left and moving clockwise around.
def solveWhiteEdge(whiteEdges, cube):
    algorithm = []
    for i in whiteEdges:
        if i[0] == 0:  # white side
            if i[1] == 1:
                colourPiece = cube[4][7]
                if colourPiece == 'o':
                    algorithm.append('L D L` D`')
                elif colourPiece == 'r':
                    algorithm.append('L` D` L D')
                elif colourPiece == 'g':
                    algorithm.append('L` D2 L D2')
            elif i[1] == 3:
                colourPiece = cube[1][7]
                if colourPiece == 'b':
                    algorithm.append('F D F` D`')
                elif colourPiece == 'g':
                    algorithm.append('F` D` F D')
                elif colourPiece == 'o':
                    algorithm.append('F D2 F` D2')
            elif i[1] == 5:
                colourPiece = cube[2][7]
                if colourPiece == 'b':
                    algorithm.append('R D2 R` D2')
                elif colourPiece == 'r':
                    algorithm.append('R D R` D`')
                elif colourPiece == 'o':
                    algorithm.append('R` D` R D')
            elif i[1] == 7:
                colourPiece = cube[3][7]
                if colourPiece == 'b':
                    algorithm.append('B D` B` D')
                elif colourPiece == 'r':
                    algorithm.append('B D2 B` D2')
                elif colourPiece == 'g':
                    algorithm.append('B D B` D`')
        elif i[0] == 1:  # red side
            if i[1] == 1:
                colourPiece = cube[4][5]
                if colourPiece == 'r':
                    algorithm.append('D` L D')
                elif colourPiece == 'b':
                    algorithm.append('L')
                elif colourPiece == 'g':
                    algorithm.append('D2 L D2')
                elif colourPiece == 'o':
                    algorithm.append('D L D`')
            elif i[1] == 3:
                colourPiece = cube[5][7]
                if colourPiece == 'r':
                    algorithm.append('D U` R` D` F')
                elif colourPiece == 'b':
                    algorithm.append('D F` D` L')
                elif colourPiece == 'g':
                    algorithm.append('D` F D R`')
                elif colourPiece == 'o':
                    algorithm.append('D2 F D R` D')
            elif i[1] == 5:
                colourPiece = cube[2][1]
                if colourPiece == 'b':
                    algorithm.append('D2 R` D2')
                elif colourPiece == 'r':
                    algorithm.append('D R` D`')
                elif colourPiece == 'o':
                    algorithm.append('D` R` D')
                elif colourPiece == 'g':
                    algorithm.append('R`')
            elif i[1] == 7:
                colourPiece = cube[0][3]
                if colourPiece == 'b':
                    algorithm.append('F L')
                elif colourPiece == 'o':
                    algorithm.append('F D L D`')
                elif colourPiece == 'g':
                    algorithm.append('F` R`')
                elif colourPiece == 'r':
                    algorithm.append('F` D R` D`')
        elif i[0] == 2:  # green side
            if i[1] == 1:
                colourPiece = cube[1][5]
                if colourPiece == 'r':
                    algorithm.append('F')
                elif colourPiece == 'b':
                    algorithm.append('D F D`')
                elif colourPiece == 'g':
                    algorithm.append('D` F D')
                elif colourPiece == 'o':
                    algorithm.append('D2 F D2')
            elif i[1] == 3:
                colourPiece = cube[5][5]
                if colourPiece == 'r':
                    algorithm.append('D R` D` F')
                elif colourPiece == 'b':
                    algorithm.append('U D F` D` L')
                elif colourPiece == 'g':
                    algorithm.append('R` D` F D')
                elif colourPiece == 'o':
                    algorithm.append('D` R D B`')
            elif i[1] == 5:
                colourPiece = cube[3][1]
                if colourPiece == 'b':
                    algorithm.append('D` B` D')
                elif colourPiece == 'r':
                    algorithm.append('D2 B` D2')
                elif colourPiece == 'o':
                    algorithm.append('B`')
                elif colourPiece == 'g':
                    algorithm.append('D B` D`')
            elif i[1] == 7:
                colourPiece = cube[0][5]
                if colourPiece == 'b':
                    algorithm.append('R D F D')
                elif colourPiece == 'o':
                    algorithm.append('R` B`')
                elif colourPiece == 'g':
                    algorithm.append('R D` F D')
                elif colourPiece == 'r':
                    algorithm.append('R F')
        elif i[0] == 3:  # orange side
            if i[1] == 1:
                colourPiece = cube[2][5]
                if colourPiece == 'b':
                    algorithm.append('D2 R D2')
                elif colourPiece == 'r':
                    algorithm.append('D R D`')
                elif colourPiece == 'g':
                    algorithm.append('R')
                elif colourPiece == 'o':
                    algorithm.append('D` R D')
            elif i[1] == 3:
                colourPiece = cube[5][3]
                if colourPiece == 'b':
                    algorithm.append('D` B D L`')
                elif colourPiece == 'r':
                    algorithm.append('U` D` L D F`')
                elif colourPiece == 'g':
                    algorithm.append('D B` D` R')
                elif colourPiece == 'o':
                    algorithm.append('B D L` D`')
            elif i[1] == 5:
                colourPiece = cube[4][1]
                if colourPiece == 'b':
                    algorithm.append('L`')
                elif colourPiece == 'r':
                    algorithm.append('D` L` D')
                elif colourPiece == 'g':
                    algorithm.append('D2 L` D2')
                elif colourPiece == 'o':
                    algorithm.append('D L` D`')
            elif i[1] == 7:
                colourPiece = cube[0][7]
                if colourPiece == 'b':
                    algorithm.append('B` L`')
                elif colourPiece == 'r':
                    algorithm.append('B D R D`')
                elif colourPiece == 'g':
                    algorithm.append('B R')
                elif colourPiece == 'o':
                    algorithm.append('B D` R D')
        elif i[0] == 4:  # blue side
            if i[1] == 1:
                colourPiece = cube[3][5]
                if colourPiece == 'b':
                    algorithm.append('D` B D')
                elif colourPiece == 'r':
                    algorithm.append('D2 B D2')
                elif colourPiece == 'g':
                    algorithm.append('D B D`')
                elif colourPiece == 'o':
                    algorithm.append('B')
            elif i[1] == 3:
                colourPiece = cube[5][1]
                if colourPiece == 'b':
                    algorithm.append('L D F` D`')
                elif colourPiece == 'r':
                    algorithm.append('D` L D F`')
                elif colourPiece == 'g':
                    algorithm.append('U2 R D B` D`')
                elif colourPiece == 'o':
                    algorithm.append('L` B L')
            elif i[1] == 5:
                colourPiece = cube[1][1]
                if colourPiece == 'b':
                    algorithm.append('D F` D`')
                elif colourPiece == 'r':
                    algorithm.append('F`')
                elif colourPiece == 'g':
                    algorithm.append('D` F` D')
                elif colourPiece == 'o':
                    algorithm.append('D2 F` D2')
            elif i[1] == 7:
                colourPiece = cube[0][1]
                if colourPiece == 'b':
                    algorithm.append('L D` B D')
                elif colourPiece == 'r':
                    algorithm.append('L` F`')
                elif colourPiece == 'g':
                    algorithm.append('L D` F` D')
                elif colourPiece == 'o':
                    algorithm.append('L B')
        elif i[0] == 5:  # yellow side
            if i[1] == 1:
                colourPiece = cube[4][3]
                if colourPiece == 'b':
                    algorithm.append('L2')
                elif colourPiece == 'r':
                    algorithm.append('U` F2')
                elif colourPiece == 'g':
                    algorithm.append('U2 R2')
                elif colourPiece == 'o':
                    algorithm.append('U B2')
            elif i[1] == 3:
                colourPiece = cube[3][3]
                if colourPiece == 'b':
                    algorithm.append('U` L2')
                elif colourPiece == 'r':
                    algorithm.append('U2 F2')
                elif colourPiece == 'g':
                    algorithm.append('U R2')
                elif colourPiece == 'o':
                    algorithm.append('B2')
            elif i[1] == 5:
                colourPiece = cube[2][3]
                if colourPiece == 'b':
                    algorithm.append('U2 L2')
                elif colourPiece == 'r':
                    algorithm.append('U F2')
                elif colourPiece == 'g':
                    algorithm.append('R2')
                elif colourPiece == 'o':
                    algorithm.append('U` B2')
            elif i[1] == 7:
                colourPiece = cube[1][3]
                if colourPiece == 'b':
                    algorithm.append('U L2')
                elif colourPiece == 'r':
                    algorithm.append('F2')
                elif colourPiece == 'g':
                    algorithm.append('U` R2')
                elif colourPiece == 'o':
                    algorithm.append('U2 B2')
    return algorithm, cube

# This function is repeated until step 2 is solved
def solveWhiteCross(cube):
    fullWhiteCrossAlgorithm = []
    correctEdgeCount = 0
    while correctEdgeCount != 4:
        singleEdgeAlgorithm, correctEdgeCount = findWhiteEdges(cube)
        solveAlgorithm, cube =solveWhiteEdge(singleEdgeAlgorithm, cube)
        solveAlgorithm = [words for segments in solveAlgorithm for words in segments.split()]
        cube = algorithmCubeMoves(cube, solveAlgorithm)
        if not solveAlgorithm:
            pass
        else:
            fullWhiteCrossAlgorithm.append(solveAlgorithm)
    return fullWhiteCrossAlgorithm, cube
