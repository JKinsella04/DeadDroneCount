import os
import webbrowser
from pynput import keyboard, mouse
drone = 0
webbrowser.open("dronecount.html")

def on_press(key):
    global drone
    

    try:
        #print('special key {0} pressed'.format(key))
        if key == keyboard.Key.caps_lock:            
            drone = drone + 1
            os.system("cls")
            print(drone)
            f = open("dronecount.html", "w")
            f.write('<body style="background-color:powderblue;">')
            f.write('<h1 style="color:black;font-size:40px;">')
            f.write('<center>')
            f.write('Killed Drone Counter\n')
            f.write('</center>')
            f.write('</h1>')
            f.write('<center>')
            f.write('<h2 style="color:black;font-size:200px;">')
            f.write(str(drone))
            f.write('</center>')
            f.write('</h2>\n')
            f.write('<meta http-equiv="refresh" content="1">')
            f.write('</body>')
            f.close
            f.newline

        if key == keyboard.Key.esc:
            drone = 0
            os.system("cls")
            print(drone)
    except AttributeError:
        print(drone)


def on_release(key):
    if key == keyboard.Key.num_lock:
    # Stop listener
        return False


# Collect events until released
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

#...or, in a non-blocking fashion:
listener = mouse.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
