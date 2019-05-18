from tkinter import Tk, Label, Button
from GlvCommon import *
from typing import List

class GlvGui(object):
    thisRow: int
    def __init__(self, master: Tk):
        self.master = master
        self.thisRow = 0
        master.title('Glv Gui')
    def nextRow(self):
        self.thisRow = self.thisRow + 1
        return self.thisRow
    def currentRow(self):
        return self.thisRow
font = ("Comic Sans MS", 24)
root = Tk()
root.geometry('500x500')
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

def startGui():
    while True:
        for guiFunc in guiFuncs:
            guiFunc.guiUpdate()
        if not dying:
            root.update()
        else:
            break
