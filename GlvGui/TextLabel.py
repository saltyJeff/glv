from GlvCommon import Func, Input, Output
from typing import Generic, TypeVar, Type, Any
import pygame
from GlvGui.GlvGui import *
from GlvGui.GlvWidget import GlvWidget
from GlvGui.Gridder import TEXT_HEIGHT

class TextLabel(GlvWidget):
    labelVal: str
    sourceName: str
    row: int
    def __init__(self, src):
        super().__init__()
        self.row = gridder.takeRow(rowHeight=TEXT_HEIGHT)
        self.labelVal = ''
        self.sourceName = self.in_src.sourceName()
    def guiUpdate(self):
        drawStr = f'{self.sourceName}: {self.labelVal}'
        surface = serifFont.render(drawStr, False, accent)
        root.blit(surface, (20, self.row))
    def update(self):
        self.labelVal = str(self.in_src.value())[:12]
