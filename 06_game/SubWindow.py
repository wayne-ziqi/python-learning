import pygame
from BackGround import BackGround
from MainWindow import MainWindow
from PushButton import PushButton

class BeginWindow(MainWindow):
    def __init__(self,width=0, height=0):
        super(BeginWindow, self).__init__(width, height)
        self._btnBegin = PushButton(self,
                                    (self.width()/2 - 30,self.height()/2),
                                    "images/resume_nor.png",
                                    "images/resume_pressed.png")
    def windowUpdate(self):
        super(BeginWindow, self).windowUpdate()
        self._btnBegin.update()


