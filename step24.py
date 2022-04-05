def check4():
    index = 9
    while index > 0:
        brain.screen.print(str(index))
        index -= 1
        wait(1, SECONDS)
        brain.screen.clear_screen()
    brain.screen.print("BOOM")
