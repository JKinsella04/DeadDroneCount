import os
from pynput import keyboard
drone = 0

def on_press(key):
    global drone
    try:
        #print('special key {0} pressed'.format(key))
        if key == keyboard.Key.caps_lock:
            drone = drone + 1
            os.system("cls")
            print(drone)
        if key == keyboard.Key.f1:
            drone = 0
            os.system("cls")
            print(drone)
    except AttributeError:
         print(drone)


def on_release(key):
    if key == keyboard.Key.esc:
    # Stop listener
        return False


# Collect events until released
with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
#listener = mouse.Listener(
#    on_press=on_press,
#    on_release=on_release)
listener.start()
