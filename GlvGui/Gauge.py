from GlvCommon import Func, Input, Output
from typing import Generic, TypeVar, Type, Any
import pygame
from GlvGui.GlvGui import *
from GlvGui.GlvWidget import GlvWidget
from GlvGui.Gridder import TEXT_HEIGHT, ROW_HEIGHT, COL_WIDTH
from GlvGui.mathUtils import *
from math import pi, sin, cos

class Gauge(GlvWidget):
    minVal: float
    maxVal: float
    value: float
    sourceName: str
    textY: int
    radius: float
    origin: float
    color: int
    def __init__(self, src, minVal=0, maxVal=100, color=None):
        super().__init__()
        self.y = grid().shareRow()
        self.x = grid().takeCol()
        self.minVal = minVal
        self.maxVal = maxVal
        self.value = minVal
        self.sourceName = self.in_src.sourceName()
        self.color = color
        self.clamped = False

        # perform offset calculations
        self.textY = self.y + ROW_HEIGHT - 2 * TEXT_HEIGHT
        self.radius = COL_WIDTH / 2
        self.origin = self.x + self.radius
    def guiUpdate(self):
        # draw gauge
        lineColor = self.color
        if lineColor is None:
            lineColor = colors.accent()
        theta = rescale(self.value, (self.minVal, self.maxVal), (0, pi))
        theta = pi - theta
        endX = self.origin + self.radius * cos(theta)
        endY = self.textY - self.radius * sin(theta)
        pygame.draw.line(root(), lineColor, (self.origin, self.textY), (endX, endY))
        
        # draw labels
        titleSurface = sansFont.render(self.sourceName, False, colors.text())
        valText = str(self.value)
        if self.clamped:
            valText = '! ' + valText + ' !'
        valSurface = detailFont.render(valText, False, colors.text())
        root().blit(titleSurface, (self.centerOffset(titleSurface), self.textY))
        root().blit(valSurface, (self.centerOffset(valSurface), self.textY + TEXT_HEIGHT))
        
        # annotate the gauge's min and max
        minSurface = detailFont.render(str(self.minVal), False, colors.text())
        maxSurface = detailFont.render(str(self.maxVal), False, colors.text())
        midSurface = detailFont.render(f'{((self.minVal + self.maxVal) / 2):.2f}', False, colors.text())
        detailY = self.textY - TEXT_HEIGHT / 2
        maxSurfaceX = self.x + COL_WIDTH - maxSurface.get_width()
        root().blit(minSurface, (self.x, detailY))
        root().blit(maxSurface, (maxSurfaceX, detailY))
        root().blit(midSurface, (self.centerOffset(midSurface), self.y))
    
    def centerOffset(self, surface):
        return self.x + ((COL_WIDTH - surface.get_width()) / 2)

    def update(self):
        self.value = clamp(self.src(), self.minVal, self.maxVal)
        self.clamped = self.value != self.src()