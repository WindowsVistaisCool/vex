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

DEBUG = True

def prscreen(text) -> None:
    if not DEBUG: return
    brain.screen.print(str(text))
    brain.screen.next_row()

# -- Enums --
class pathDirection:
    UP = 0
    DOWN = -134
    RIGHT = 67
    LEFT = -67

# -- Objects --
class Path:
    def __init__(self, pathData):
        # check if pathData is a PathMap instance or coordinate list
        prscreen("Starting path with " + str(type(pathData)))
        self.coords = pathData.data() if isinstance(pathData, PathMap) else pathData

    def getRawCoords(self) -> dict:
        return self.coords

    def getDirections(self) -> tuple:
        sequentialCommands = []
        firstCoord = lastCoord = self.coords[1]
        first = True
        currentHead = 0
        for k, coord in sorted(self.coords.items()):
            if first:
                first = False
                continue
            if coord[1] < lastCoord[1]: # next tile is above
                pD = pathDirection.UP
                sequentialCommands.append(pD)
            elif coord[1] > lastCoord[1]: # next tile is below
                pD = pathDirection.DOWN
                sequentialCommands.append(pD)
            if coord[0] > lastCoord[0] : # next tile is right
                pD = pathDirection.RIGHT
                sequentialCommands.append(pD)
            elif coord[0] < lastCoord[0]: # next tile is left
                pD = pathDirection.LEFT
                sequentialCommands.append(pD)
            lastCoord = coord
            currentHead = pD
        return (firstCoord, sequentialCommands)

class PathMap:
    def __init__(self, pathMap):
        prscreen("PathMap init...")
        self.pathMap = {}
        unsortedCoords = {}
        for row in pathMap:
            if not any(row): continue
            for order in row:
                if order != 0:
                    unsortedCoords[order] = (row.index(order), pathMap.index(row))
        for key in sorted(unsortedCoords.keys()):
            self.pathMap[key] = unsortedCoords[key]
        prscreen("Coords: " + str(self.pathMap[15]))

    def data(self):
        return self.pathMap

class Drivetrain:
    tile_square_size = 12.5

    def __init__(self, drivetrain):
        self.drive = drivetrain

    def move_for_tile(self):
        self.drive.drive_for(FORWARD, self.tile_square_size, INCHES)

    def rotate(self, degree):
        if degree > 0:
            self.drive.turn_for(RIGHT, degree, DEGREES)
        else:
            self.drive.turn_for(LEFT, -degree, DEGREES)

    def run_path(self, path: Path):
        prscreen("Driving path...")
        pathData = path.getDirections()
        directions = pathData[1]
        currentHeading = 0 # TODO: find accurate measurement
        for degree in directions:
            if degree - currentHeading != 0:
                prscreen("> ROTATE " + str(degree - currentHeading))
                self.rotate(degree - currentHeading)
            currentHeading = degree
            prscreen("> MOVE TILE")
            self.move_for_tile()

# -- Execution --
def main():
    global Drivetrain, Path, PathMap, prscreen, DEBUG # "import" everything
    dt = Drivetrain(drivetrain)

    # Paths to run on robot
    simple_circle = Path(PathMap([
        [9,   8,  7,  6,  5],
        [10,  0,  0,  0,  4],
        [11,  0,  0,  0,  3],
        [12,  0,  0,  0,  2],
        [13, 14, 15, 16,  1]
    ]))
    # spiral = Path(PathMap([
    #     [9,   8,  7,  6,  5],
    #     [10, 21, 20, 19,  4],
    #     [11, 22, 25, 18,  3],
    #     [12, 23, 24, 17,  2],
    #     [13, 14, 15, 16,  1]
    # ]))
    spiral = Path({
        1: (4, 4),
        2: (4, 3),
        3: (4, 2),
        4: (4, 1),
        5: (4, 0),
        6: (3, 0),
        7: (2, 0),
        8: (1, 0),
        9: (0, 0),
        10: (0, 1),
        11: (0, 2),
        12: (0, 3),
        13: (0, 4),
        14: (1, 4),
        15: (2, 4),
        16: (3, 4),
        17: (3, 3),
        18: (3, 2),
        19: (3, 1),
        20: (2, 1),
        21: (1, 1),
        22: (1, 2),
        23: (1, 3),
        24: (2, 3),
        25: (2, 2)
    })

    r_t = Path({
        1: (1, 0),
        2: (0, 0),
        3: (0, 1)
    })

    dt.run_path(spiral) # Run path

main()
