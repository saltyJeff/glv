from GlvCommon import Func, Input, Output
from typing import Generic, TypeVar, Type, Any
from tkinter import StringVar, Label, LEFT, RIGHT, X
from GlvGui.GlvGui import *
from GlvGui.GlvWidget import GlvWidget

class TextLabel(GlvWidget):
    labelVal: str
    def __init__(self, src):
        super().__init__()
        row = gridder.takeRow()
        self.labelVar = StringVar()
        self.nameLabel = Label(text=self.in_src.sourceName()+':', font=sansFont, padx=20)
        self.nameLabel.grid(row=row, column=gridder.takeCol())
        self.varLabel = Label(textvariable=self.labelVar, font=serifFont)
        self.varLabel.grid(row=row, column=gridder.takeCol(), padx=20)
        self.labelVal = ''
    def guiUpdate(self):
        self.labelVar.set(self.labelVal)
    def update(self):
        self.labelVal = str(self.in_src.value())[:12]
