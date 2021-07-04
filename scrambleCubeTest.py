from moves import *
import random
import numpy as np

# This function was used during testing to randomly scramble a cube.
# It performs 25 random scrambles on a cube.
def scrambleCubeTest(cube):
    scrambleArr = []
    for i in range(25):
        randomSpin = random.randrange(0, 13)
        if randomSpin == 1:
            cube = front(cube)
            scrambleArr.append('F')
        if randomSpin == 2:
            cube = frontPrime(cube)
            scrambleArr.append('F`')
        if randomSpin == 3:
            cube = right(cube)
            scrambleArr.append('R')
        if randomSpin == 4:
            cube = rightPrime(cube)
            scrambleArr.append('R`')
        if randomSpin == 5:
            cube = left(cube)
            scrambleArr.append('L')
        if randomSpin == 6:
            cube = leftPrime(cube)
            scrambleArr.append('L`')
        if randomSpin == 7:
            cube = back(cube)
            scrambleArr.append('B')
        if randomSpin == 8:
            cube = backPrime(cube)
            scrambleArr.append('B`')
        if randomSpin == 9:
            cube = up(cube)
            scrambleArr.append('U')
        if randomSpin == 10:
            cube = upPrime(cube)
            scrambleArr.append('U`')
        if randomSpin == 11:
            cube = down(cube)
            scrambleArr.append('D')
        if randomSpin == 12:
            cube = downPrime(cube)
            scrambleArr.append('D`')
    return scrambleArr, cube
