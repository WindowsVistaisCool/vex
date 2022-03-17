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

def prscreen(text: str) -> None:
    brain.screen.print(str(text))
    brain.screen.next_row()

# -- Enums --
class pathDirection:
    UP = 0
    DOWN = 134 # Should never be used
    RIGHT = 67
    LEFT = -67

# -- Objects --
class Path:
    def __init__(self, pathData):
        # check if pathData is a PathMap instance or coordinate list
        self.coords = pathData.data() if isinstance(pathData, PathMap) else pathData

    def getRawCoords(self) -> dict:
        return self.coords

    def getDirections(self) -> tuple:
        sequentialCommands = []
        firstCoord = lastCoord = self.coords[1]
        first = True
        for k, coord in sorted(self.coords.items()):
            if first:
                first = False
                continue
            if coord[1] < lastCoord[1]: # next tile is above
                sequentialCommands.append(pathDirection.UP)
            elif coord[1] > lastCoord[1]: # next tile is below
                sequentialCommands.append(pathDirection.DOWN)
            if coord[0] > lastCoord[0]: # next tile is right
                sequentialCommands.append(pathDirection.RIGHT)
            elif coord[0] < lastCoord[0]: # next tile is left
                sequentialCommands.append(pathDirection.LEFT)
            lastCoord = coord
        return (firstCoord, sequentialCommands)

class PathMap:
    def __init__(self, pathMap):
        self.pathMap = {}
        unsortedCoords = {}
        for row in pathMap:
            if not any(row): continue
            for order in row:
                if order != 0:
                    unsortedCoords[order] = (row.index(order), pathMap.index(row))
        for key in sorted(unsortedCoords.keys()):
            self.pathMap[key] = unsortedCoords[key]

    def data(self):
        return self.pathMap

class Drivetrain:
    tile_square_size = 12
    tile_center_size = 2.5

    def __init__(self, drivetrain):
        self.drive = drivetrain

    def move_for_tile(self): # TODO: test tile with front color sensor
        self.stopped = False
        self.drive.drive_for(FORWARD, self.tile_square_size, INCHES)
        self.stopped = True

    def rotate(self, degree):
        self.stopped = False
        self.drive.turn_for(RIGHT, degree, DEGREES)
        self.stopped = True

    def run_path(self, path: Path):
        pathData = path.getDirections()
        brain.screen.next_row()
        brain.screen.print("Starting path at " + str(pathData[0]))
        directions = pathData[1]
        currentHeading = 0 # TODO: find accurate measurement
        for degree in directions:
            if degree - currentHeading != 0:
                self.rotate(degree - currentHeading)
            currentHeading = degree
            self.move_for_tile()

# -- Execution --
def main():
    global Drivetrain, Path, PathMap # "import" everything
    dt = Drivetrain(drivetrain)

    # Paths to run on robot
    simple_circle = Path(PathMap([
                [9,   8,  7,  6,  5],
                [10,  0,  0,  0,  4],
                [11,  0,  0,  0,  3],
                [12,  0,  0,  0,  2],
                [13, 14, 15, 16,  1]
            ]))
    spiral = Path(PathMap([
                [9,   8,  7,  6,  5],
                [10, 21, 20, 19,  4],
                [11, 22, 25, 18,  3],
                [12, 23, 24, 17,  2],
                [13, 14, 15, 16,  1]
            ]))

    dt.run_path(spiral) # Run path

main()
