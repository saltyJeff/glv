from GlvCommon import Func, Input, Output
from typing import Generic, TypeVar, Type, Any
import pygame
from GlvGui.GlvGui import *
from GlvGui.GlvWidget import GlvWidget
from GlvGui.Gridder import ROW_HEIGHT, COL_WIDTH, TEXT_HEIGHT

class ToggleButton(GlvWidget):
    label: str
    row: int
    col: int
    def __init__(self, label='Ur Butt'):
        super().__init__()
        self.row = gridder.shareRow(rowHeight=2 * TEXT_HEIGHT)
        self.col = gridder.takeCol()
        self.label = label
        self.set = False
    def guiUpdate(self):
        borderColor = colors.text()
        textColor = colors.text()
        # handle clicks
        buttonRect = pygame.Rect(self.col, self.row, COL_WIDTH, 2 * TEXT_HEIGHT)
        if buttonRect.collidepoint(mousePos()):
            if mousePressed():
                self.set = not self.set
                self.out(1 if self.set else 0)
            if not self.set:
                borderColor = colors.accent()
        if self.set:
            borderColor = colors.accent()
            textColor = colors.back()
            pygame.draw.rect(root, colors.text(), buttonRect)
        
        midX = self.col + COL_WIDTH / 2
        midY = self.row + (2 * TEXT_HEIGHT) / 2
        pygame.draw.rect(root, borderColor, buttonRect, 4)
        
        surface = sansFont.render(self.label, False, textColor)
        textX = midX - surface.get_width() / 2
        textY = midY - surface.get_height() / 2
        root.blit(surface, (textX, textY))