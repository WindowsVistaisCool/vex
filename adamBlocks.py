vexcode_vision_5_objects = None
vexcode_brain_precision = 0
vexcode_console_precision = 0
Repititions = 0
message1 = Event()
REDD = Event()
BLUEE = Event()
GREENN = Event()
BlueForward = Event()
For = Event()
Lef = Event()

def when_started1():
    global Repititions, message1, REDD, BLUEE, GREENN, BlueForward, For, Lef, vexcode_vision_5_objects, vexcode_brain_precision, vexcode_console_precision
    while True:
        vexcode_vision_5_objects = vision_5.take_snapshot(vision_5__BLUEE)
        if vexcode_vision_5_objects and len(vexcode_vision_5_objects) > 0:
            brain.screen.clear_screen()
            brain.screen.print("Blue!")
            while (vexcode_vision_5_objects and len(vexcode_vision_5_objects) > 0):
                vexcode_vision_5_objects = vision_5.take_snapshot(vision_5__BLUEE)
                drivetrain.drive_for(FORWARD, 4, INCHES, wait=True)
                wait(5, MSEC)
        else:
            brain.screen.clear_screen()
            brain.screen.print("No blue!")
            drivetrain.turn_for(RIGHT, 72, DEGREES, wait=True)
            while not (vexcode_vision_5_objects and len(vexcode_vision_5_objects) > 0):
                vexcode_vision_5_objects = vision_5.take_snapshot(vision_5__BLUEE)
                drivetrain.turn_for(LEFT, 10, DEGREES, wait=True)
                wait(5, MSEC)
        wait(5, MSEC)

when_started1()
