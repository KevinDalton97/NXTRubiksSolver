from motorSpins import *
from applyAlgorithm import *
from colourDetection import *
from motorSpins import *

brick = nxt.locator.find_one_brick()
facePositions = np.array(['D', 'F', 'R', 'B', 'L', 'U'])
flipMotor = Motor(brick, PORT_C)
spinColourMotor = Motor(brick, PORT_B)
spinMotor = Motor(brick, PORT_A)
# Used to test consistency of individual parts of robot
# Flip Test
# for i in range(50):
#     flipCube(brick)
#     time.sleep(0.2)
#     print(i)

for i in range(10):
    spinCube(brick, 'clockwise')

# for i in range(10):
#     spinCube(brick, 'anticlockwise')


# for i in range(10):
#     faceSpin(brick, 'anticlockwise', facePositions)
#     time.sleep(0.2)
#     print(i)
# # #
# colourArray = []
# for i in range(20):
#     spinCube(brick, 'clockwise')
#     time.sleep(0.2)
#     colourArray.append(getColour(brick))
#     print(colourArray)

time.sleep(5)
turnOffColourSensor(brick)
flipMotor.turn(1, 1, False)
spinMotor.turn(1, 1, False)
spinColourMotor.turn(1, 1, False)