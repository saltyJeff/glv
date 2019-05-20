from GlvCommon import Func, Input, Output
from typing import Generic, TypeVar, Type, Any
import pygame
from GlvGui.GlvGui import *
from GlvGui.GlvWidget import GlvWidget
from GlvGui.Gridder import ROW_HEIGHT, COL_WIDTH, TEXT_HEIGHT
from GlvGui.TextInputModule import TextInput
class NumericInput(GlvWidget):
    label: str
    row: int
    col: int
    def __init__(self, label='Ur #'):
        super().__init__()
        self.row = gridder.shareRow(rowHeight=2*TEXT_HEIGHT)
        self.col = gridder.takeCol()
        self.label = label
        self.textInput = TextInput(
            font_family='Courier',
            antialias=False,
            text_color=colors.text(),
            font_size=16
        )
        self.focused = False
        self.lastText = ''
    def guiUpdate(self):
        boundingRect = pygame.Rect(self.col, self.row + 0.8 * TEXT_HEIGHT, COL_WIDTH, 1.1 * TEXT_HEIGHT)
        borderColor = colors.text()
        if mousePressed():
            self.focused = boundingRect.collidepoint(mousePos())
        if self.focused:
            borderColor = colors.accent()
            # process events
            self.textInput.update(getEvents())
            self.textInput.text_color = colors.text()
            self.textInput.set_cursor_color(colors.text())
            inputText = self.textInput.get_text()
            if len(inputText) >= 14:
                inputText = inputText[:14]
            self.textInput.set_text(inputText)
            if self.lastText != inputText:
                try:
                    val = parseNum(inputText)
                    self.out(val)
                except:
                    pass
                self.lastText = inputText
        root.blit(self.textInput.get_surface(), (self.col + 10, self.row + 1.1 * TEXT_HEIGHT))
        pygame.draw.rect(root, borderColor, boundingRect, 2)
        labelSurface = sansFont.render(self.label, False, colors.text())
        root.blit(labelSurface, (self.col, self.row))

def parseNum(numStr):
    # if decimal point, then get rid of it
    if '.' in numStr:
        return float(numStr)
    if numStr.startswith('0b'):
        return int(numStr[2:], 2)
    elif numStr.startswith('0x'):
        return int(numStr[2:], 16)
    return int(numStr)
    