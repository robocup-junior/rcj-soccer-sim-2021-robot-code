import sys
from pathlib import Path
sys.path.append(str(Path('.').absolute().parent))
sys.path.append('/app/controllers')

# team = 'BLUE'
# rcj_soccer_player controller - ROBOT Y1

# Feel free to import built-in libraries
import math

# You can also import scripts that you put into the folder with controller
from team_037_libraries.robot1 import rcj_soccer_robot
from team_037_libraries.robot1 import utils


class MyRobot(rcj_soccer_robot.RCJSoccerRobot):
    def run(self):
        if self.name[0] == 'Y':
            t_m  = 1
        else:
            t_m = -1
        frameCounter = 0
        while self.robot.step(rcj_soccer_robot.TIME_STEP) != -1:
            if self.is_new_data():
                data = self.get_new_data()

                # Get the position of our robot
                robot_pos = data[self.name]
                # Get the position of the ball
                ball_pos = data['ball']

                # Get angle between the robot and the ball
                # and between the robot and the north
                ball_angle, robot_angle = self.get_angles(ball_pos, robot_pos)

                # Compute the speed for motors
                direction = utils.get_direction(ball_angle)

                # If the robot has the ball right in front of it, go forward,
                # rotate otherwise
                if direction == 0:
                    left_speed = -10
                    right_speed = -10
                elif direction == 2:
                    left_speed = 10
                    right_speed = 10
                else:
                    left_speed = direction * 4
                    right_speed = direction * -4

                # Set the speed to motors
                self.left_motor.setVelocity(left_speed)
                self.right_motor.setVelocity(right_speed)
                frameCounter += 1


my_robot = MyRobot()
my_robot.run()
