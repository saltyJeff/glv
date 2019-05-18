from tkinter import Tk, Label, Button
root = Tk()
from GlvCommon import *
from typing import List
from GlvGui.Gridder import Gridder

class GlvGui(object):
    def __init__(self, master: Tk):
        self.master = master
        self.master.title('Glv Gui')

sansFont = ("Calibri", 18)
serifFont = ("Courier", 18)

glvGui = GlvGui(root)
dying = False
def onExit():
    global dying
    dying = True
    killThreads()
    root.destroy()

root.wm_protocol("WM_DELETE_WINDOW", onExit)

guiFuncs: List[Func] = list()
def registerSelf(func: Func):
    guiFuncs.append(func)

gridder = Gridder()

def startGui():
    while True:
        for guiFunc in guiFuncs:
            guiFunc.guiUpdate()
        if not dying:
            root.update()
        else:
            break
