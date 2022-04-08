#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code


# wait for rotation sensor to fully initialize
wait(30, MSEC)


#endregion VEXcode Generated Robot Configuration

def when_started1():
    parking_map = [
        [0 for i in range(10)],
        [0, 2, 1, 1, 2, 2, 1, 1, 2, 0],
        [0, 1, 1, 2, 1, 1, 1, 1, 1, 0],
        [0 for i in range(10)],
        [0, 1, 2, 2, 1, 1, 2, 1, 1, 0]
    ]
    coords = []
    currentLoopPos = [0, 1]
    for row in parking_map:
        if not any(row):
            currentLoopPos[1] += 1
            continue
        for col in row:
            currentLoopPos[0] += 1
            if col == 2:
                coords.append([currentLoopPos[0], currentLoopPos[1]])
        currentLoopPos[0] = 0
        currentLoopPos[1] += 1
    brain.screen.print("There are " + str(len(coords)) + " open parking spaces:")
    for coord in coords:
        brain.screen.next_row()
        brain.screen.print("(" + str(coord[0]) + ", " + str(coord[1]) + ")")

when_started1()
