from GlvCommon import Func, Input, Output
from typing import Generic, TypeVar, Type, Any
from tkinter import StringVar, Label, LEFT, RIGHT, X
from GlvGui.GlvGui import *
from GlvGui.GlvWidget import GlvWidget
from tk_tools import RotaryScale as RotScale

class Gauge(GlvWidget):
    def __init__(self, src, title='some gauge', maxValue=100, unit='', **kwargs):
        super().__init__()
        self.maxValue = maxValue
        row = gridder.shareRow()
        self.gaugeWidget = RotScale(root, max_value=maxValue, unit=unit)
        self.gaugeWidget.grid(row=row, column=gridder.takeCol())
        self.labelVal = 1
    def guiUpdate(self):
        self.gaugeWidget.set_value(self.labelVal)
    def update(self):
        self.labelVal = self.src()
