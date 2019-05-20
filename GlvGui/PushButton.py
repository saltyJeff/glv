from GlvCommon import Func, Input, Output
from typing import Generic, TypeVar, Type, Any
import pygame
from GlvGui.GlvGui import *
from GlvGui.GlvWidget import GlvWidget
from GlvGui.Gridder import ROW_HEIGHT, COL_WIDTH, TEXT_HEIGHT

# no need to debounce :P
IDLE = 0
SET = 1
RESET = 2
class PushButton(GlvWidget):
    label: str
    row: int
    col: int
    def __init__(self, label='Ur Butt'):
        super().__init__()
        self.row = gridder.thisRow()
        self.col = gridder.takeCol()
        self.label = label
        self.primed = False
        self.state = IDLE
    def guiUpdate(self):
        borderColor = colors.text()
        textColor = colors.text()
        # handle clicks
        buttonRect = pygame.Rect(self.col, self.row, COL_WIDTH, TEXT_HEIGHT + 8)
        mouseOver = buttonRect.collidepoint(mousePos())
        if self.primed:
            if mouseReleased():
                if mouseOver:
                    self.state = SET
                self.primed = False
        else:
            if mousePressed() and mouseOver:
                self.primed = True
        
        if self.primed:
            borderColor = colors.accent()
            textColor = colors.back()
            pygame.draw.rect(root, colors.text(), buttonRect)
        elif buttonRect.collidepoint(mousePos()):
            borderColor = colors.accent()
        
        midX = self.col + COL_WIDTH / 2
        midY = self.row + (TEXT_HEIGHT + 8) / 2
        pygame.draw.rect(root, borderColor, buttonRect, 4)
        
        surface = sansFont.render(self.label, False, textColor)
        textX = midX - surface.get_width() / 2
        textY = midY - surface.get_height() / 2
        root.blit(surface, (textX, textY))
    def shouldUpdate(self):
        return self.state != IDLE
    def update(self):
        if self.state is SET:
            self.out(1)
            self.state = RESET
        elif self.state is RESET:
            self.out(0)
            self.state = IDLE