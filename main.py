import pynput.keyboard
import re
import FileMngr
import DateTimeClass as date
import pygetwindow as gw
from datetime import datetime
import pyautogui, sys
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
import database as db


def on_press(key):
    print("Key pressed: {0}".format(key))
    app = gw.getActiveWindow().title.replace("-","_")
    app = re.sub('\W+', '', app)
    db.insertKeyboard(db.conectar(),app,date.getAgora(),key)
    date.getAgora()
    screenShot = pyautogui.screenshot()
    fileName = str(date.getAgora()+' - '+app)
    screenShot.save(print_path+'\\'+fileName+".png")

def on_release(key):
    print("Key released: {0}".format(key))

def on_move(x, y):
    #print("Mouse moved to ({0}, {1})".format(x, y))
    pass

def on_click(x, y, button, pressed):
    if pressed:
        print('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))
        app = gw.getActiveWindow().title.replace("-", "_")
        app = re.sub('\W+','', app )
        db.insertMouse(db.conectar(), x, y,date.getAgora(),app, button)
        fileName = str(date.getAgora() + ' - ' + app)
        screenShot = pyautogui.screenshot()
        screenShot.save(print_path + '\\' + fileName + ".png")
    else:
        print('Mouse released at ({0}, {1}) with {2}'.format(x, y, button))

def on_scroll(x, y, dx, dy):
    print('Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))

fmng = FileMngr.FileMngr()
print_path = fmng.createFolder(date.getAgora(), r'C:\Users\douglas.favaro\Documents\Python Scripts\Process Mapping')
# Setup the listener threads
keyboard_listener = KeyboardListener(on_press=on_press, on_release=on_release)
mouse_listener = MouseListener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)

# Start the threads and join them so the script doesn't end early
keyboard_listener.start()
mouse_listener.start()
keyboard_listener.join()
mouse_listener.join()

