from CS2API import * #1.0.14
import keyboard

def events():
    if keyboard.is_pressed('space') and read('on_ground', int) == 65665:
        do('jump', 65537, 256, int)

listen(events)
