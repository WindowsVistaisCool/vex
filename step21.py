#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
left_drive_smart = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
right_drive_smart = Motor(Ports.PORT2, GearSetting.RATIO_18_1, True)
drivetrain = DriveTrain(left_drive_smart, right_drive_smart, 319.19, 295, 40, MM, 1)


# wait for rotation sensor to fully initialize
wait(30, MSEC)


#endregion VEXcode Generated Robot Configuration
def main():
    math_list = [5, 1, 3]
    def sum_list(l):
        lastI = 0
        for i in l: lastI += i
        return lastI
    brain.screen.print(sum_list(math_list))
    brain.screen.next_row()
    brain.screen.print(sum_list([math_list[0], math_list[-1]]))
    brain.screen.next_row()
    brain.screen.print((math_list[0] - math_list[2]) * math_list[1])
    

main()
