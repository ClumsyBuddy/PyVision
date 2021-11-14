#imports
from pyautogui import printInfo
from VisionManager import Handle_Images, ShotType
import InputManager as PlayerInput
from time import sleep
from Utility import PTimer, Counter


#Gloabl Variables
handle = Handle_Images("Dot.png", Acc=0.90)
handle.ScreenShot(ShotType.Single)
MainTimer = PTimer({"MouseTimer":PTimer(), "SkillTimer":PTimer()})
MainCounter = {"MC":Counter()}


tempToggle = False
def PrintInfo():
    print("Hello World")


#MainLoop
while True:
    #PlayerInput.GetKeyPress(handle.ToggleScreenShot, Key="o")
    PlayerInput.GetKeyPress(PrintInfo, Key="i")

  
        #PlayerInput.IsMouseBeingHeld(Callback=PlayerInput.MouseClick, Counter=MainCounter["MC"])
    #PlayerInput.GetSingleMouseInteraction(SavePosition=True, Callback=PrintInfo)
    if handle._ToggleScreenShot == True:
        if handle.Template() == False:
            handle.ScreenShot(ShotType.Single)
        if handle.Loc[0] > -1 and handle.Loc[1] > -1:
            PlayerInput.MouseClick(
                True,
                handle.CenterPoint[0],
                handle.CenterPoint[1],
                0.001
            )
    sleep(0.0001)
