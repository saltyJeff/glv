from GlvCommon import Func, Input, Output
from typing import Generic, TypeVar, Type, Any
import pygame
from GlvGui.GlvGui import *
from GlvGui.GlvWidget import GlvWidget
from GlvGui.Gridder import TEXT_HEIGHT, ROW_HEIGHT, COL_WIDTH
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
        self.row = gridder.shareRow()
        self.col = gridder.takeCol()
        self.minVal = minVal
        self.maxVal = maxVal
        self.value = minVal
        self.sourceName = self.in_src.sourceName()
        self.color = color
        self.clamped = False

        # perform offset calculations
        self.textY = self.row + ROW_HEIGHT - 2 * TEXT_HEIGHT
        self.radius = COL_WIDTH / 2
        self.origin = self.col + self.radius
    def guiUpdate(self):
        # draw gauge
        lineColor = self.color
        if lineColor is None:
            lineColor = colors.accent()
        theta = rescale(self.value, (self.minVal, self.maxVal), (0, pi))
        theta = pi - theta
        endX = self.origin + self.radius * cos(theta)
        endY = self.textY - self.radius * sin(theta)
        pygame.draw.line(root, lineColor, (self.origin, self.textY), (endX, endY))
        
        # draw labels
        titleSurface = serifFont.render(self.sourceName, False, colors.text())
        valText = str(self.value)
        if self.clamped:
            valText = '! ' + valText + ' !'
        valSurface = detailFont.render(valText, False, colors.text())
        root.blit(titleSurface, (self.centerOffset(titleSurface), self.textY))
        root.blit(valSurface, (self.centerOffset(valSurface), self.textY + TEXT_HEIGHT))
        
        # annotate the gauge's min and max
        minSurface = detailFont.render(str(self.minVal), False, colors.text())
        maxSurface = detailFont.render(str(self.maxVal), False, colors.text())
        midSurface = detailFont.render(f'{((self.minVal + self.maxVal) / 2):.2f}', False, colors.text())
        detailY = self.textY - TEXT_HEIGHT / 2
        maxSurfaceX = self.col + COL_WIDTH - maxSurface.get_width()
        root.blit(minSurface, (self.col, detailY))
        root.blit(maxSurface, (maxSurfaceX, detailY))
        root.blit(midSurface, (self.centerOffset(midSurface), self.row))
    
    def centerOffset(self, surface):
        return self.col + ((COL_WIDTH - surface.get_width()) / 2)

    def update(self):
        self.value = clamp(self.src(), self.minVal, self.maxVal)
        self.clamped = self.value != self.src()

def clamp(val, minVal, maxVal) -> float:
    return max(minVal, min(val, maxVal))
def rescale(n, range1, range2):
    delta1 = range1[1] - range1[0]
    delta2 = range2[1] - range2[0]
    return (delta2 * (n - range1[0]) / delta1) + range2[0]