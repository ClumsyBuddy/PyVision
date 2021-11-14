#imports
from VisionManager import Handle_Images, ScreenShot, auto, ShotType
import InputManager as PlayerInput
from time import sleep

#Gloabl Variables
handle = Handle_Images("Dot.png", Acc=0.90)
handle.ScreenShot(ShotType.Single)

#MainLoop
while True:
    PlayerInput.GetKeyPress(handle.ToggleScreenShot, "o")
    #PlayerInput.GetSingleMouseInteraction(PrintInfo, False)
    if handle.ToggleScreenShot == True:
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
