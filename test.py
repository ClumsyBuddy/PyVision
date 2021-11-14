from enum import auto
from VisionManager import Handle_Images
from VisionManager import auto
from VisionManager import ShotType

import InputManager as input


from time import sleep

def PrintInfo():
    print(input.InputData["StoredMousePositions"])

handle = Handle_Images("anose.png")
handle.ScreenShot(ShotType.Single)

ScreenShotToggle = False  

while True:
    input.GetSingleMouseInteraction(PrintInfo, False)
    if ScreenShotToggle == True:
        if handle.Template() == False:
            handle.ScreenShot(ShotType.Single)
        if handle.Loc[0] > -1 and handle.Loc[1] > -1:
            auto.click(
                handle.Loc[0],
                handle.Loc[1]
            )
    sleep(0.25)
