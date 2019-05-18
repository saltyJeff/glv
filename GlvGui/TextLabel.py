from GlvCommon import Func, Input, Output
from typing import Generic, TypeVar, Type, Any
from tkinter import *
from GlvGui.GlvGui import root, registerSelf, font

class TextLabel(Func):
    labelVal: str
    def __init__(self, src):
        super().__init__()
        self.labelVar = StringVar()
        self.nameLabel = Label(root, text=self.in_src.sourceName()+':', font=font)
        self.nameLabel.pack()
        self.varLabel = Label(root, textvariable=self.labelVar, font=font)
        self.varLabel.pack()
        self.labelVal = ''
        registerSelf(self)
        
    def guiUpdate(self):
        self.labelVar.set(self.labelVal)
    def update(self):
        self.labelVal = str(self.in_src.value())
