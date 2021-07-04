from trackCube import *
from colourDetection import *

# Used to stop all the motors and allow them to move freely
brick = nxt.locator.find_one_brick()

spinMotor = Motor(brick, PORT_A)
flipMotor = Motor(brick, PORT_C)
spinColourMotor = Motor(brick, PORT_B)
turnOffColourSensor(brick)

flipMotor.turn(1, 1, False)
spinMotor.turn(1, 1, False)
spinColourMotor.turn(-20, 400, False)
#spinColourMotor.turn(-20, 300, False)

