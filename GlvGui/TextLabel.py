from GlvCommon import Func, Input, Output
from typing import Generic, TypeVar, Type, Any
import pygame
from GlvGui.GlvGui import *
from GlvGui.GlvWidget import GlvWidget
from GlvGui.Gridder import TEXT_HEIGHT, LEFT_PAD

class TextLabel(GlvWidget):
    labelVal: str
    sourceName: str
    def __init__(self, src, inline=True):
        super().__init__()
        if not inline:
            gridder.nextRow(rowHeight=2*TEXT_HEIGHT)
        self.y = gridder.shareRow(rowHeight=2*TEXT_HEIGHT)
        self.x = gridder.takeCol()
        self.labelVal = ''
        self.sourceName = self.in_src.sourceName()
    def guiUpdate(self):
        sourceSurface = sansFont.render(self.sourceName, False, colors.text())
        root.blit(sourceSurface, (self.x, self.y))

        valSurface = serifFont.render(self.labelVal, False, colors.text())
        root.blit(valSurface, (self.x, self.y + TEXT_HEIGHT))
    def update(self):
        self.labelVal = str(self.in_src.value())[:14]
