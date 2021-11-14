from enum import auto
from VisionManager import Handle_Images
from VisionManager import auto
from VisionManager import ShotType

import InputManager as _input


from time import sleep

def SayHi():
    print("Hello World")
def GoodBye():
    print("GoodBye")

Obj = {"Hello":SayHi, "GoodBye":GoodBye, "Email":"Winnboys1105"}

Obj["GoodBye"]()
print(Obj["Email"])



