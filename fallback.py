# PLEASE MAKE SURE TO CHECK THESE VARS/METHODS WITH THE THING ON THE LEFT SIDE WITH ALL THE FUNCS

# stuff to run inside whenstarted1()
def whenstarted1():
    hasFoundObjects = True
    lastObjCount = 0
    while True:
        # take vision snapshot
        vision_5.takeSnapshot(color_code_shitass_you_name_it_adam_please_thx_ily)
        if vision_5.object_count > 0:
            if not hasFoundObjects:
                hasFoundObjects = True
            if lastObjCount != vision_5.object_count:
                lastObjCount = vision_5.object_count
                brain.screen.clear_screen()
                brain.screen.print("There are currently " + vision_5.object_count + " objects detected"
        else:
            if hasFoundObjects:
                brain.screen.clear_screen()
                brain.screen.print("No object found :(")
                hasFoundObjects = False
