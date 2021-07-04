import numpy as np
from moves import *
from whiteCross import *
from solveWhiteCorners import *
from applyAlgorithm import *
from colourDetection import *
import nxt
import usb.core
import usb.util
from nxt.motor import *
from motorSpins import *
from nxt.sensor import Color20
from nxt.sensor import Type
import time
from nxt.sensor import BaseAnalogSensor
import random
from scrambleCubeTest import *
from solveSecondLayer import *
from trackCube import *
from OLL import *
from PLL import *
from optimiseAlgorithm import *
random.seed()
start_time = time.time()
brick = nxt.locator.find_one_brick()
facePositions = np.array(['D', 'F', 'R', 'B', 'L', 'U'])

w = 'w'
r = 'r'
g = 'g'
o = 'o'
b = 'b'
y = 'y'

cube = np.array([[w, w, w, w, w, w, w, w], [r, r, r, r, r, r, r, r], [g, g, g, g, g, g, g, g], [o, o, o, o, o, o, o, o],
                 [b, b, b, b, b, b, b, b], [y, y, y, y, y, y, y, y]])
#
# scrambleAlgorithm, scrambleCube = scrambleCubeTest(cube)
# print('---Scramble Algorithm---')
# print(scrambleAlgorithm)
# print('------------------------')

scrambleCube = scanCubeFace(brick) # Scanning the faces of the cube, Step 1
#
# whiteCrossAlgorithm, scrambleCube = solveWhiteCross(scrambleCube) # Solving Step 2
# print('---White Cross Algorithm---')
# print(whiteCrossAlgorithm)
# print('------------------------')
#
# whiteSideAlgorithm, scrambleCube = solveWhiteSide(scrambleCube) # Solving Step 3
# solveAlgorithm = whiteCrossAlgorithm+whiteSideAlgorithm # Adding to full algorithm
# print('---White Side Algorithm---')
# print(whiteSideAlgorithm)
# print('------------------------')
#
# scrambleCube, secondLayerAlgorithm = solveSecondLayerPieces(scrambleCube) # Solving Step 4
# solveAlgorithm = solveAlgorithm+secondLayerAlgorithm # Adding to full algorithm
# print('---Second Layer Algorithm---')
# print(secondLayerAlgorithm)
# print('------------------------')
#
# scrambleCube, ollAlgorithm = solveOLL(scrambleCube) # Solving Step 5
# solveAlgorithm = solveAlgorithm+ollAlgorithm # Adding to full algorithm
# print('---OLL Algorithm---')
# print(ollAlgorithm)
# print('------------------------')
#
# scrambleCube, pllAlgorithm = solvePLL(scrambleCube) # Solving Step 6
# solveAlgorithm = solveAlgorithm+pllAlgorithm # Adding to full algorithm
# print('---PLL Algorithm---')
# print(pllAlgorithm)
# print('------------------------')
#
# solveAlgorithm = algorithmToString(solveAlgorithm) # Converting algorithm to string
# solveAlgorithm = optimiseAlgorithm(solveAlgorithm) # Removing unnecessary moves
#
# print('---Solve Algorithm---')
# print(solveAlgorithm)

solveAlgorithm = ['F','D','L','F2','R2','F2','R2','U2','R','D`','F2','B2','U`','L2','F2','L2','U2','R2','U2']
algorithmOnRobot(solveAlgorithm, facePositions, brick)

print("%s seconds" % (time.time() - start_time))
#F` D B` R` B` L2 D` F2 L F2 U` L2 F` D2 L` B` F` L2 D U` F` D2 R D L2 R2 D` B` U F2

# U2 B2 L2 R D2 L2 B2 D2 L' D2 U' B2 F2 U2 F'