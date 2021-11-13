from enum import auto
import types
from VisionManager import Handle_Images
from VisionManager import auto
from VisionManager import ShotType

from time import sleep

handle = Handle_Images("nose.png")
handle.ScreenShot(ShotType.Single)

ScreenShotToggle = False  

while True:
    if ScreenShotToggle == True:
        if handle.Template() == False:
            handle.ScreenShot(ShotType.Single)
        if handle.Loc[0] > -1 and handle.Loc[1] > -1:
            auto.click(
                handle.Loc[0],
                handle.Loc[1]
            )
    sleep(0.01)