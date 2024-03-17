import keyboard
import time

def readGpsInput(coords):
    try:
        while True:
            if(keyboard.is_pressed("up")):
                return [coords[0] + 0.3, coords[1]]
            
            if(keyboard.is_pressed("down")):
                return [coords[0] - 0.3, coords[1]]
            
            if(keyboard.is_pressed("right")):
                return [coords[0], coords[1] + 0.3]
            
            if(keyboard.is_pressed("left")):
                return [coords[0], coords[1] - 0.3]

    except KeyboardInterrupt:
        exit()