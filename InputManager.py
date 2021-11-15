import win32api, win32con
from time import sleep
from Utility import Counter
import keyboard
import mouse
#Data used for Input interactions
global InputData
InputData = {"StoredMousePositions": [],
 "MouseHeldDown":False, "MouseClicked": False,
 "KeyClicked":False, "KeyHeldDown":False}



#Clicks mouse with set delay and moves cursor if chosen
def MouseClick(MoveCursor=False, x=-1, y=-1, delay=0.01):
    print("MouseClick")
    if MoveCursor:
        sleep(delay)
        win32api.SetCursorPos((x,y))
        sleep(delay)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    sleep(delay)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

#Gets a single mouse click, returns true on mouse release
#Calls callbackk function with arguemensts on release
def GetSingleMouseInteraction(Callback=lambda:None, SavePosition=False, *args):
    M = win32api.GetKeyState(0x01)
    if M >= 0:
        InputData["MouseHeldDown"] = True
        InputData["MouseClicked"] = True
    else:
        InputData["MouseHeldDown"] = False
    if InputData["MouseHeldDown"] == False and InputData["MouseClicked"] == True:
        InputData["MouseClicked"] = False
        GetMousePosition(SavePosition)
        Callback(*args)

#Work in progress
def IsMouseBeingHeld(Counter: Counter, Callback, *args):
    M = win32api.GetKeyState(0x01)
    if M < 0 and Counter.GetValue() < 0:
        print("Clicked")
        Callback(*args)
        Counter.UpdateCounter()
    if Counter.GetValue() == 2:
        Counter.Reset()
    #print(Counter.GetValue())
    #print(M)



#Return cursor position and can save Cursor position in list
def GetMousePosition(SavePosition=False):
    Pos = win32api.GetCursorPos()
    if SavePosition:
        InputData["StoredMousePositions"].append(Pos)
    return Pos


#Gets a single keypress, returns true on key release and calls the 
#callback function
def GetKeyPress(Callback=lambda:None, Key=None, *args):
    if keyboard.is_pressed(Key):
        InputData["KeyClicked"] = True
        return False
    elif not keyboard.is_pressed(Key) and InputData["KeyClicked"]:
        InputData["KeyClicked"] = False
        Callback(*args)
        return True
    return False

