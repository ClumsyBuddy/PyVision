import pyautogui as auto
import pydirectinput as dauto
import win32api, win32con


from time import sleep

global InputData
InputData = {"StoredMousePositions": [],
 "MouseHeldDown":False, "MouseClicked": False,
 "KeyClicked":False}


def MouseClick(MoveCursor=False, x=-1, y=-1, delay=0.01):
    if MoveCursor:
        sleep(delay)
        win32api.SetCursorPos((x,y))
        sleep(delay)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    sleep(delay)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)

def GetSingleMouseInteraction(Callback=(), SavePosition=False, *args):
    M = win32api.GetKeyState(0x01)
    if M <= 0:
        InputData["MouseHeldDown"] = True
        InputData["MouseClicked"] = True
    else:
        InputData["MouseHeldDown"] = False
    if InputData["MouseHeldDown"] == False and InputData["MouseClicked"] == True:
        InputData["MouseClicked"] = False
        GetMousePosition(SavePosition)
        Callback(*args)

def GetMousePosition(SavePosition=False):
    Pos = auto.position()
    if SavePosition:
        InputData["StoredMousePositions"].append(Pos)
    return Pos



def GetKeyPress(Callback=(), Key=None, *args):
    if Key == None:
        print("No key selected")
        return False
    K = win32api.GetAsyncKeyState(win32api.VkKeyScan(Key))
    if K >= 0:
        InputData["KeyClicked"] = True
    else:
        if InputData["KeyClicked"]:
            InputData["KeyClicked"] = False
            Callback()
            return True
        
    return False

def InputType(Key, DirectX=False):
    if DirectX:
        dauto.press(Key, 1, 0)
    else:
        auto.press(Key, 1 , 0)


