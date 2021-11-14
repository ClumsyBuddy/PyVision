import pyautogui as auto
import pydirectinput as dauto
import win32api


from time import sleep

global InputData
InputData = {"StoredMousePositions": [], "MouseHeldDown":False, "MouseClicked": False}

Accounts = {"Name1": ("Email", "Password"), "Name2": ("Email", "Password")}

def MouseClick(DirectX=False, x=-1, y=-1):
    if x and y > 0:
        if DirectX:
            dauto.click(x,y)
        else:
            auto.click(x,y)
    else:
        if DirectX:
            dauto.click()
        else:
            auto.click()

def GetSingleMouseInteraction(Callback=(), SavePosition=False):
    M = win32api.GetKeyState(0x01)
    if M < 0:
        InputData["MouseHeldDown"] = True
        InputData["MouseClicked"] = True
    else:
        InputData["MouseHeldDown"] = False
    if InputData["MouseHeldDown"] == False and InputData["MouseClicked"] == True:
        InputData["MouseClicked"] = False
        GetMousePosition(SavePosition)
        Callback()

def GetMousePosition(SavePosition=False):
    Pos = auto.position()
    if SavePosition:
        InputData["StoredMousePositions"].append(Pos)
    return Pos

def InputType(Key, DirectX=False):
    if DirectX:
        dauto.press(Key, 1, 0)
    else:
        auto.press(Key, 1 , 0)


