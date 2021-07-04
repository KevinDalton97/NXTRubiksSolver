from rotationFunctions import *
from applyAlgorithm import *
# The functions in this file are used to solve step 5 of the Rubik's Cube

# This function contains all the algorithms used to solve step 5
def orientateLastLayer(cube):
    algorithm = []
    yellowSide = np.where(cube[5] == 'y')

    singleCaseArray = [[0, 2, 4, 6], [0, 2, 4, 5, 6, 7], [0, 1, 2, 4, 5, 6]]

    notSingleCaseArray = [[1, 3, 4, 5, 7], [1, 3, 5, 7], [1, 2, 3, 5, 6, 7], [1, 2, 3, 4, 5, 7], [], [2, 6], [4], [0, 6], [0, 2, 3, 7], [3, 7], [1, 3], [4, 5, 6, 7],
                          [0, 1, 2, 7], [1, 4, 5, 6], [0, 1, 3, 4], [2, 4, 5, 7], [1, 2, 4, 7], [1, 2, 3, 6], [1, 4, 7],
                          [0, 1, 5], [1, 5, 6], [3, 5, 6], [0,1,3], [3, 4, 5], [0, 1, 4, 5], [1, 2, 5, 6]]

    singleCaseAlgorithms = ['R L` B R B R` B` R2 L2 F R F` L`','R` L F R L` U2 R` L F R L`','R U R` U` R` L F R F` L`']

    yellowSide = list(yellowSide[0])
    thirdLayer = [cube[1, 2], cube[1, 3], cube[1, 4], cube[2, 2], cube[2, 3], cube[2, 4], cube[3, 2], cube[3, 3],
                  cube[3, 4], cube[4, 2], cube[4, 3], cube[4, 4]]
    if yellowSide in singleCaseArray:
        result = singleCaseArray.index(yellowSide)
        algorithm.append(singleCaseAlgorithms[result])
        return algorithm
    elif yellowSide in notSingleCaseArray:
        result = notSingleCaseArray.index(yellowSide)
        if result == 0: # sunes
            if thirdLayer[2] == 'y':
                algorithm.append('L U L` U L U2 L`')
                #sune
            else:
                algorithm.append('U` R` U` R U` R` U2 R')
                #antisune
        elif result == 1: # cross
            if thirdLayer[0] == 'y' and thirdLayer[2] == 'y' and thirdLayer[6] == 'y' and thirdLayer[8] == 'y':
                algorithm.append('R U2 R` U` R U R` U` R U` R`')
                # first cross
            elif thirdLayer[2] == 'y' and thirdLayer[6] == 'y' and thirdLayer[9] == 'y' and thirdLayer[11] == 'y':
                algorithm.append('R U2 R2 U` R2 U` R2 U2 R')
                # second cross
            else:
                algorithm.append('Y')
                return algorithm
        elif result == 2: # sandtimer_shape
            if thirdLayer[0] == 'y':
                algorithm.append('R` F R B` R` F` R B')
                # correct orientation
            else:
                algorithm.append('U2 R` F R B` R` F` R B')
                # wrong orientation
        elif result == 3: # fat point
            if thirdLayer[0] == 'y':
                algorithm.append('R2 D R` U2 R D` R` U2 R`')
                # first
            else:
                algorithm.append('U` R` F` L F R F` L` F')
                # second
        elif result == 4: # dot
            if thirdLayer[1] == 'y' and thirdLayer[3] == 'y' and thirdLayer[4] == 'y' and thirdLayer[5] == 'y' and thirdLayer[7] == 'y' and thirdLayer[9] == 'y' and thirdLayer[10] == 'y' and thirdLayer[11] == 'y':
                algorithm.append('R U2 R2 F R F` U2 R` F R F`')
                #first
            elif thirdLayer[1] == 'y' and thirdLayer[2] == 'y' and thirdLayer[4] == 'y' and thirdLayer[6] == 'y' and thirdLayer[7] == 'y' and thirdLayer[9] == 'y' and thirdLayer[10] == 'y' and thirdLayer[11] == 'y':
                algorithm.append('F R U R` U` F` B U L U` L` B`')
                #second
            else:
                algorithm.append('Y')
                return algorithm
        elif result == 5: # diag line
            if thirdLayer[6] == 'y':
                algorithm.append('R U R` U R` F R F` U2 R` F R F`')
                #correct orien
            else:
                algorithm.append('U2 R U R` U R` F R F` U2 R` F R F`')
                #wrong orien
        elif result == 6: # dotDiag_shape
            if thirdLayer[0] == 'y':
                algorithm.append('B U L U` L` B` U F R U R` U` F`')
                # second right
            else:
                algorithm.append('U B U L U` L` B` U` F R U R` U` F`')
                # first kinda wrong
        elif result == 7: # v shape
            if thirdLayer[8] == 'y':
                algorithm.append('F R U R` U Y` R` U2 R` F R F` Y')
                # first
            else:
                algorithm.append('U2 L` R B R B R` B` L R2 F R F`')
                #NO 19
                # second
        elif result == 8: # c shape
            if thirdLayer[3] == 'y':
                algorithm.append('R` U` R` F R F` U R')
                # first
            else:
                algorithm.append('U` R U R2 U` R` F R U R U` F`')
                # second
        elif result == 9: # line
            if thirdLayer[3] == 'y' and thirdLayer[4] == 'y' and thirdLayer[5] == 'y' and thirdLayer[9] == 'y' and thirdLayer[11] == 'y':
                algorithm.append('R U2 R2 U` R U` R` U2 F R F`')
                # first
            elif thirdLayer[2] == 'y' and thirdLayer[4] == 'y' and thirdLayer[6] == 'y' and thirdLayer[9] == 'y' and thirdLayer[10] == 'y'and thirdLayer[11] == 'y':
                algorithm.append('U2 R U R` U R U` B U` B` R`')
                #52
                # second
            elif thirdLayer[3] == 'y' and thirdLayer[4] == 'y' and thirdLayer[6] == 'y' and thirdLayer[8] == 'y' and thirdLayer[10] == 'y' and thirdLayer[11] == 'y':
                algorithm.append('U` B U L U` L` U L U` L` B`')
                #51
                # third
            elif thirdLayer[0] == 'y' and thirdLayer[2] == 'y' and thirdLayer[4] == 'y' and thirdLayer[6] == 'y' and thirdLayer[8] == 'y' and thirdLayer[10] == 'y':
                algorithm.append('U F R U R` U` R F` L F R` F` L`')
                #56
                # fourth
            else:
                algorithm.append('Y2')
                return algorithm
                #spin twice
        elif result == 10: # l shape
            if thirdLayer[1] == 'y' and thirdLayer[2] == 'y' and thirdLayer[4] == 'y' and thirdLayer[6] == 'y' and thirdLayer[9] == 'y' and thirdLayer[11] == 'y':
                algorithm.append('F R U R` U` R U R` U` F`')
                # first
            elif thirdLayer[1] == 'y' and thirdLayer[3] == 'y' and thirdLayer[4] == 'y' and thirdLayer[6] == 'y' and thirdLayer[8] == 'y' and thirdLayer[11] == 'y':
                algorithm.append('U R` U` R` F R F` R` F R F` U R')
                # second
            elif thirdLayer[0] == 'y' and thirdLayer[1] == 'y' and thirdLayer[2] == 'y' and thirdLayer[4] == 'y' and thirdLayer[6] == 'y' and thirdLayer[8] == 'y':
                algorithm.append('U L F R` F R F` R` F R F2 L`')
                # 54
                # third
            elif thirdLayer[1] == 'y' and thirdLayer[3] == 'y' and thirdLayer[4] == 'y' and thirdLayer[5] == 'y' and thirdLayer[9] == 'y' and thirdLayer[11] == 'y':
                algorithm.append('R` F` L F` L` F L F` L` F2 R')
                #53
                # fourth
            elif thirdLayer[0] == 'y' and thirdLayer[1] == 'y' and thirdLayer[2] == 'y' and thirdLayer[4] == 'y' and thirdLayer[5] == 'y' and thirdLayer[9] == 'y':
                algorithm.append('U R` F R` F` R2 U2 Y R` F R F` Y`')
                # fifth
            elif thirdLayer[0] == 'y' and thirdLayer[1] == 'y' and thirdLayer[3] == 'y' and thirdLayer[4] == 'y' and thirdLayer[5] == 'y' and thirdLayer[8] == 'y':
                algorithm.append('R` F R2 B` R2 F` R2 B R`')
                # sixth
        elif result == 11: # p shape1
            if thirdLayer[9] == 'y':
                algorithm.append('B U L U` L` B`')
                # first
            else:
                algorithm.append('R U B` U` R` U R B R`')
                # second
        elif result == 12: # p shape2
            if thirdLayer[3] == 'y':
                algorithm.append('B` U` R` U R B')
                # first
            else:
                algorithm.append('U2 R` U` F U R U` R` F` R')
                # second
        elif result == 13: # t shape
            if thirdLayer[0] == 'y':
                algorithm.append('R U R` U` R` F R F`')
                # first
            else:
                algorithm.append('F R U R` U` F`')
                # second
        elif result == 14: # w_shape
            if thirdLayer[3] == 'y':
                algorithm.append('R U R` U R U` R` U` R` F R F`')
                # first
            else:
                algorithm.append('U L` U` L U` L` U L U L F` L` F')
                # second
        elif result == 15: # treeSun_shape1
            if thirdLayer[3] == 'y':
                algorithm.append('R2 U R` B` R U` R2 U R B R`')
                # first
            else:
                algorithm.append('R U` R` U2 R U Y R U` R` U` F` Y`')
                # second
        elif result == 16: # treeSun_shape2
            if thirdLayer[3] == 'y':
                algorithm.append('Y R U R` U` R U` R` F` U` F R U R` Y`')
                # first
            else:
                algorithm.append('U R` U2 R U R` U R Y F R U R` U` F` Y`')
                # second
        elif result == 17: # fish_shape1
            if thirdLayer[0] == 'y':
                # first
                algorithm.append('F R U` R` U` R U R` F`')
            else:
                algorithm.append('U2 R U2 R2 F R F` R U2 R`')
                # second
        elif result == 18: # fish_shape2
            if thirdLayer[2] == 'y':
                # first
                algorithm.append('R U R` U R` F R F` R U2 R`')
            else:
                algorithm.append('U R U R` U` R` F R2 U R` U` F`')
                # second
        elif result == 19: # knightMove_shape1
            if thirdLayer[2] == 'y':
                # first
                algorithm.append('L F` L` U` L F L` Y` R` U R')
            else:
                algorithm.append('U2 L F L` R U R` U` L F` L`')
                # second
        elif result == 20: # knightMove_shape2
            if thirdLayer[0] == 'y':
                # first
                algorithm.append('R` F R U R` F` R Y` R U` R`')
            else:
                algorithm.append('U2 R` F` R L` U` L U R` F R')
                # second
        elif result == 21: # smallBolt_shape1
            if thirdLayer[0] == 'y':
                # first
                algorithm.append('R U2 R` U2 R` F R F`')
            else:
                algorithm.append('U2 F` L` U` L U F Y F R U R` U` F`')
                # second
        elif result == 22: # smallBolt_shape2
            if thirdLayer[2] == 'y':
                # first
                algorithm.append('L F R` F R F2 L`')
            else:
                algorithm.append('U2 F R U R` U` F` U F R U R` U` F`')
                # second
        elif result == 23: # square_shape1
            if thirdLayer[0] == 'y':
                # first
                algorithm.append('L F2 R` F` R F` L`')
            else:
                algorithm.append('U` R` F2 L F L` F R')
                # second
        elif result == 24: # bigbolt2
            if thirdLayer[3] == 'y':
                # first
                algorithm.append('L F` L` U` L U F U` L`')
            else:
                algorithm.append('U2 L F` L` U` L U F U` L`')
                # second
        elif result == 25: # bigbolt1
            if thirdLayer[11] == 'y':
                # first
                algorithm.append('R` F R U R` U` F` U R')
            else:
                algorithm.append('U2 R` F R U R` U` F` U R')
                # second
    else:
        algorithm.append('Y')
        return algorithm

    return algorithm

# Repeats the above function until step 5 is solved
def solveOLL(cube):
    algorithm = []
    expectedYelllowside = ['y', 'y', 'y', 'y', 'y', 'y', 'y', 'y']
    currentYellowSide = cube[5]
    count = 0
    while np.array_equal(currentYellowSide,expectedYelllowside) == False:
        OLLalgorithm = orientateLastLayer(cube)
        OLLalgorithm = [words for segments in OLLalgorithm for words in segments.split()]
        cube = algorithmCubeMoves(cube, OLLalgorithm)
        algorithm.append(OLLalgorithm)
        currentYellowSide = cube[5]
    return cube, algorithm
