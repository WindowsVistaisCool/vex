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

# -- Enums --
import enum
class pathDirection(enum.Enum):
    UP = 0
    DOWN = 180
    RIGHT = 90
    LEFT = 270

    def getDegree(self, direction: pathDirection) -> int:
        degrees = {UP: 0, DOWN: 180, RIGHT: 90, LEFT: 270}
        return degrees[direction]

class pathMapType(enum.Enum):
    LIST = 0
    COORD = 1

# -- Objects --
class Path:
    def __init__(self, pathMap: PathMap):
        self.pathMap = pathMap.data()

    def getRawPathMap(self) -> dict:
        return self.pathMap

    def getDirections(self) -> tuple:
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

class PathMap:
    def __init__(self, type = pathMapType.LIST: pathMapType, pathMap):
        self.type = type
        self.pathMap = {}
        if self.type == pathMapType.COORDS:
            self.pathMap = pathMap
        elif self.type == pathMapType.LIST:
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

    def move_for_tile(self): # TODO: test tile with front color sensor
        self.stopped = False
        self.left.spin(FORWARD, tile_size_degrees, DEGREES)
        self.right.spin(FORWARD, tile_size_degrees, DEGREES)
        self.stopped = True

    def rotate(self, degree): # TODO: fix rotation algorithm
        self.stopped = False
        self.left.spin_for(FORWARD, degree*2, DEGREES)
        self.right.spin_for(FORWARD, -degree*2 , DEGREES)

    def run_path(self, path: Path):
        pathData = path.getDirections()
        print(f"Running path {path}. Robot start position is at ({pathData[0][0]}, {pathData[0][1]}). Amount of positions: {len(pathData[1].keys())}")
        directions = pathData[1]
        currentHeading = 0 # TODO: find accurate measurement
        for direction in directions:
            self.rotate(directions.value - currentHeading)
            currentHeading = direction.value
            self.move_for_tile()

# -- Execution --
def main():
    global Drivetrain, Path, PathMap, pathMapType # "import" everything
    drivetrain = Drivetrain(mLeft, mRight)

    simple_circle = Path(PathMap(pathMapType.LIST, [
                [9,   8,  7,  6,  5],
                [10,  0,  0,  0,  4],
                [11,  0,  0,  0,  3],
                [12,  0,  0,  0,  2],
                [13, 14, 15, 16,  1]
            ])) # Path to rotate around in a circle pattern
    zig_zag = Path(PathMap(pathMapType.LIST, [[9, 8, 0, 0, 0], [0, 7, 6, 0, 0], [0, 0, 5, 4, 0], [0, 0, 0, 3, 2], [0, 0, 0, 0, 1]])) # Path to zig zag diagonally from bottom right to top left
    drivetrain.run_path(simple_circle)

main()
