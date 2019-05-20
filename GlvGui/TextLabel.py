from GlvCommon import Func, Input, Output
from typing import Generic, TypeVar, Type, Any
import pygame
from GlvGui.GlvGui import *
from GlvGui.GlvWidget import GlvWidget
from GlvGui.Gridder import TEXT_HEIGHT, LEFT_PAD

class TextLabel(GlvWidget):
    labelVal: str
    sourceName: str
    row: int
    col: int
    def __init__(self, src, inline=False):
        super().__init__()
        if not inline:
            gridder.nextRow(rowHeight=2*TEXT_HEIGHT)
        self.row = gridder.thisRow()
        self.col = gridder.takeCol()
        self.labelVal = ''
        self.sourceName = self.in_src.sourceName()
    def guiUpdate(self):
        sourceSurface = sansFont.render(self.sourceName, False, colors.text())
        root.blit(sourceSurface, (self.col, self.row))

        valSurface = serifFont.render(self.labelVal, False, colors.text())
        root.blit(valSurface, (self.col, self.row + TEXT_HEIGHT))
    def update(self):
        self.labelVal = str(self.in_src.value())[:14]
