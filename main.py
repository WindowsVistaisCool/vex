#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain = Brain()

# Robot configuration code
mLeft = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
mRight = Motor(Ports.PORT2, GearSetting.RATIO_18_1, True)

# wait for rotation sensor to fully initialize
wait(30, MSEC)

#endregion VEXcode Generated Robot Configuration

class drivetrain:
    def __init__(self, leftM, rightM):
        self.left = leftM
        self.right = rightM
        self.stopped = True
    
    def stop(self):
        self.left.stop()
        self.right.stop()
        self.stopped = True
    
    def run(self):
        self.left.spin(FORWARD)
        self.right.spin(FORWARD)
        self.stopped = False

    def rotate(self, degree):
        self.stopped = False
        self.left.spin_for(FORWARD, degree*2, DEGREES)
        self.right.spin_for(FORWARD, -degree*2 , DEGREES)

def main():
    # Define drivtrain to control both motors at once
    global drivetrain
    drivetrain = drivetrain(mLeft, mRight)
    
    drivetrain.rotate(90)

    
main()
