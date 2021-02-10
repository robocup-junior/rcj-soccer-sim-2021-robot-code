# rcj_soccer_player controller - ROBOT Y1

###### REQUIRED in order to import files from B1 controller
import sys
from pathlib import Path
from time import time

sys.path.append(str(Path(".").absolute().parent))
# You can now import scripts that you put into the folder with your
# robot B1 controller
from robot1.europa.striker import Striker
from robot1.europa.vector import Vector, angle, distance, is_angle_between

######

# Feel free to import built-in libraries
import math

millis = lambda: int(round(time() * 1000))


class MyRobot(Striker):
    def __init__(self):
        super(MyRobot, self).__init__(blue=self.team.startswith("B"))


my_robot = MyRobot()
my_robot.run()
