from rotationFunctions import *
from applyAlgorithm import *
import time

# # This function contains all the algorithms used to solve step 6
def solveLastLayer(cube):
    algorithm = []
    thirdLayer = [cube[1, 2], cube[1, 3], cube[1, 4], cube[2, 2], cube[2, 3], cube[2, 4], cube[3, 2], cube[3, 3],
                  cube[3, 4], cube[4, 2], cube[4, 3], cube[4, 4]]
    if thirdLayer[0] == thirdLayer[8] and thirdLayer[2] == thirdLayer[6] and thirdLayer[3] == thirdLayer[11] and \
            thirdLayer[5] == thirdLayer[9]:
        algorithm.append('F R U` R` U` R U R` F` R U R` U` R` F R F`') # corner 1
        return algorithm
    elif thirdLayer[0] == thirdLayer[5] and thirdLayer[2] == thirdLayer[6] and thirdLayer[3] == thirdLayer[8] and \
            thirdLayer[9] == thirdLayer[11]:
        algorithm.append('L U` R` U L` U2 R U` R` U2 R') # corner 2
        return algorithm
    elif thirdLayer[0] == thirdLayer[2] and thirdLayer[2] == thirdLayer[7] and thirdLayer[1] == thirdLayer[6] and \
            thirdLayer[1] == thirdLayer[8] and thirdLayer[3] == thirdLayer[5] and thirdLayer[3] == thirdLayer[10] and \
            thirdLayer[9] == thirdLayer[11] and thirdLayer[9] == thirdLayer[4]:
        algorithm.append('R2 L2 D R2 L2 U2 R2 L2 D R2 L2') # edge 1
        return algorithm
    elif thirdLayer[0] == thirdLayer[2] and thirdLayer[3] == thirdLayer[5] and thirdLayer[6] == thirdLayer[8] and \
            thirdLayer[9] == thirdLayer[11] and thirdLayer[1] == thirdLayer[3] and thirdLayer[4] == thirdLayer[9] and \
            thirdLayer[7] == thirdLayer[8] and thirdLayer[10] == thirdLayer[0]:
        algorithm.append('R U` R U R U R U` R` U` R2') # edge 1
        return algorithm
    elif thirdLayer[0] == thirdLayer[2] and thirdLayer[3] == thirdLayer[5] and thirdLayer[6] == thirdLayer[8] and\
            thirdLayer[9] == thirdLayer[11] and thirdLayer[1] == thirdLayer[11] and thirdLayer[4] == thirdLayer[0] and\
            thirdLayer[7] == thirdLayer[8] and thirdLayer[10] == thirdLayer[3]:
        algorithm.append('R2 U R U R` U` R` U` R` U R`') # edge 2
        return algorithm
    elif thirdLayer[0] == thirdLayer[2] and thirdLayer[3] == thirdLayer[5] and thirdLayer[6] == thirdLayer[8] and \
            thirdLayer[9] == thirdLayer[11] and thirdLayer[1] == thirdLayer[11] and thirdLayer[4] == thirdLayer[0] and \
            thirdLayer[7] == thirdLayer[8] and thirdLayer[10] == thirdLayer[3]:
        algorithm.append('R2 U R U R` U` R` U` R` U R`') # edge 3
        return algorithm
    elif thirdLayer[0] == thirdLayer[2] and thirdLayer[3] == thirdLayer[5] and thirdLayer[6] == thirdLayer[8] and \
            thirdLayer[9] == thirdLayer[11] and thirdLayer[1] == thirdLayer[11] and thirdLayer[4] == thirdLayer[6] and \
            thirdLayer[7] == thirdLayer[3] and thirdLayer[10] == thirdLayer[0]:
        algorithm.append('R L` B R2 L2 F R2 L2 B R L` D2 R2 L2') # edge 4
        return algorithm
    else:
        algorithm.append('Y')
        return algorithm

# Repeats the above function until step 6 is solved
def solvePLL(cube):
    algorithm = []
    solved = np.array(
        [['w', 'w', 'w', 'w', 'w', 'w', 'w',' w'], ['r', 'r', 'r', 'r', 'r', 'r', 'r', 'r'], ['g', 'g', 'g', 'g', 'g', 'g', 'g', 'g'], ['o', 'o', 'o', 'o', 'o', 'o', 'o', 'o'],
         ['b', 'b', 'b', 'b', 'b', 'b', 'b', 'b'], ['y', 'y', 'y', 'y', 'y', 'y', 'y', 'y']])
    while True:
        thirdLayer = [cube[1, 2], cube[1, 3], cube[1, 4], cube[2, 2], cube[2, 3], cube[2, 4], cube[3, 2], cube[3, 3],
                      cube[3, 4], cube[4, 2], cube[4, 3], cube[4, 4]]
        pllalgorithm = solveLastLayer(cube)
        pllalgorithm = [words for segments in pllalgorithm for words in segments.split()]
        cube = algorithmCubeMoves(cube, pllalgorithm)
        algorithm.append(pllalgorithm)
        while cube[1, 2] == cube[1, 3] and cube[1, 2] == cube[1, 4] and cube[2, 2] == cube[2, 3] and cube[2, 2] == cube[2, 4]:
            if cube[1, 2] == cube[1, 0] :
                return cube, algorithm
            else:
                cube = algorithmCubeMoves(cube, 'U')
                algorithm.append('U')

