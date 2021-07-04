import numpy as np
from whiteCross import *
from solveWhiteCorners import *
from solveSecondLayer import *
from optimiseAlgorithm import *
from OLL import *
from PLL import *
w = 'w'
r = 'r'
g = 'g'
o = 'o'
b = 'b'
y = 'y'

# This was used to calculate the average moves in the algorithm with and without optimisation

average = 0
for i in range(5000):
    cube = np.array(
        [[w, w, w, w, w, w, w, w], [r, r, r, r, r, r, r, r], [g, g, g, g, g, g, g, g], [o, o, o, o, o, o, o, o],
         [b, b, b, b, b, b, b, b], [y, y, y, y, y, y, y, y]])
    scrambleAlgorithm, scrambleCube = scrambleCubeTest(cube)
    whiteCrossAlgorithm, scrambleCube = solveWhiteCross(scrambleCube)
    whiteSideAlgorithm, scrambleCube = solveWhiteSide(scrambleCube)
    solveAlgorithm = whiteCrossAlgorithm+whiteSideAlgorithm
    scrambleCube, secondLayerAlgorithm = solveSecondLayerPieces(scrambleCube)
    solveAlgorithm = solveAlgorithm+secondLayerAlgorithm
    scrambleCube, ollAlgorithm = solveOLL(scrambleCube)
    solveAlgorithm = solveAlgorithm+ollAlgorithm
    scrambleCube, pllAlgorithm = solvePLL(scrambleCube)
    solveAlgorithm = solveAlgorithm+pllAlgorithm
    solveAlgorithm = algorithmToString(solveAlgorithm)
    average = average+len(solveAlgorithm)

print(average)
print(average/5000)
