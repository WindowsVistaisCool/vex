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

# ------ Adam and Kyle's code ------
import enum
class pathDirection(enum.Enum):
    UP = 0
    DOWN = 180
    RIGHT = 90
    LEFT = 270

class Drivetrain:
    tile_square_size = 8
    tile_center_size = 2.5
    inch_per_rotation = 7.85
    tile_size_degrees = (360 / inch_per_rotation) * 8

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

    def move_for_tile(self):
        self.stopped = False
        self.left.spin(FORWARD, tile_size_degrees, DEGREES)
        self.right.spin(FORWARD, tile_size_degrees, DEGREES)
        self.stopped = True

    def rotate(self, degree): # TODO: fix rotation algorithm
        self.stopped = False
        self.left.spin_for(FORWARD, degree*2, DEGREES)
        self.right.spin_for(FORWARD, -degree*2 , DEGREES)

    def do_path(self, path):
        directions = path.getDirections()[1]
        currentHeading = 0 # TODO: find accurate measurement
        for direction in directions:
            self.rotate(directions.value - currentHeading)
            currentHeading = direction.value
            self.move_for_tile()

class Path:
    def __init__(self, pathMap):
        self.rawPathMap = pathMap
        self.unsortedCoords = {}
        self.coords = {}
        for row in pathMap:
            if not any(row): continue
            for order in row:
                if order != 0:
                    self.unsortedCoords[order] = (row.index(order), pathMap.index(row))
        for key in sorted(self.unsortedCoords.keys()): self.coords[key] = self.unsortedCoords[key]

    def getRawPathMap(self):
        return self.pathMap

    def getRawCoords(self):
        return self.coords

    def getDirections(self):
        sequentialCommands = []
        firstCoord = lastCoord = self.coords[1]
        for coord in self.coords[:1]: # skip first coord
            if coord[1] > lastCoord[1]:
                sequentialCommands.append(pathDirection.UP)
            elif coord[1] < lastCoord[1]:
                sequentialCommands.append(pathDirection.DOWN)
            if coord[0] > lastCoord[0]:
                sequentialCommands.append(pathDirection.RIGHT)
            elif coord[0] < lastCoord[0]:
                sequentialCommands.append(pathDirection.LEFT)
            lastCoord = coord
        return (firstCoord, sequentialCommands)

def main():
    # Define drivtrain to control both motors at once
    global Drivetrain, Path, pathDirection
    drivetrain = Drivetrain(mLeft, mRight)

    simple_circle = Path([
                [9,   8,  7,  6,  5],
                [10,  0,  0,  0,  4],
                [11,  0,  0,  0,  3],
                [12,  0,  0,  0,  2],
                [13, 14, 15, 16,  1]
            ])
    drivetrain.run_path(simple_circle)

main()
