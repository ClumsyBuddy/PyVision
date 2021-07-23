#imports
import cv2 as cv
from mss import mss
import mss.tools
import pyautogui as auto
import enum

class ShotType(enum.Enum):
    Single = 1
    Multiple = 2
    Section = 3


class Handle_Images:
    def __init__(self, img_path, x = 0, y = 0, w = auto.size().width, h = auto.size().height):
        self.img_path = img_path
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        tp = cv.imread(self.img_path)
        self.img_grey = cv.cvtColor(tp, cv.COLOR_RGB2GRAY)
        self.img_shape = self.img_grey.shape[::-1]
        self.Curr_img_grey = None
        self.Loc = (-1, -1)
        self.screen_shot = ScreenShot
        self._Type = ShotType


    def ScreenShot(self, Type, x=0, y=0, w=auto.size().width, h=auto.size().height):
        file_Name = None
        if Type == self._Type.Single:
           file_Name = self.screen_shot.SingleScreenShot(x=x,y=y,w=w,h=h)
        elif Type == self._Type.Multiple:
            print("Multiple is not working Currently")
            file_Name = self.screen_shot.SingleScreenShot(x=x,y=y,w=w,h=h)
        elif Type == self._Type.Section:
            file_Name = self.screen_shot.ScreenSection(x=x,y=y,w=w,h=h)
        Curr_Img = cv.imread(file_Name)
        self.Curr_img_grey = cv.cvtColor(Curr_Img, cv.COLOR_RGB2GRAY)

    def Template(self):
        result = cv.matchTemplate(
            image = self.Curr_img_grey, 
            templ = self.img_grey, 
            method = cv.TM_CCOEFF_NORMED
            )
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)
        if max_val >= 0.9:
            self.Loc = max_loc
            self.Curr_img_grey = cv.rectangle(
            img = self.Curr_img_grey,
            pt1 = max_loc,
            pt2 = (
                max_loc[0] + self.img_shape[0], # = pt2 x
                max_loc[1] + self.img_shape[1] # = pt2 y
                ),
                color = (0,0,255),
                thickness = -1 #fill the rectangle
            )
            return True
        self.Loc = (-1, -1)
        return False

class ScreenShot:
    _Directory = "image.png"
    _x = 0
    _y = 0
    _w = 0
    _h = 0

    def SingleScreenShot(Directory=_Directory, x=_x, y=_y, w=_w, h=_h):
        with mss.mss() as sct:
            filename = sct.shot(mon=-1, output=Directory)
        return filename

    def MultipleScreenShots(Directory=_Directory, x=_x, y=_y, w=_w, h=_h):
        file_names = []
        for i in range(100):
            with mss() as sct:
                file_names.append(sct.shot(mon=-1, output=Directory+str(i)))
        return file_names

    def ScreenSection(Directory=_Directory, x=_x, y=_y, w=_w, h=_h):
        with mss.mss() as sct:
            # The screen part to capture
            monitor = {"top": y, "left": x, "width": w, "height": h}
            filename = Directory.format(**monitor)
            # Grab the data
            sct_img = sct.grab(monitor)
            # Save to the picture file
            mss.tools.to_png(sct_img.rgb, sct_img.size, output=filename)
        return filename
