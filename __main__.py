from GlvCommon import *
from GlvGui import *
from typing import List
from time import sleep, time
import traceback
from logging import getLogger, Logger, INFO, basicConfig
from math import sin, pi

class Sinusoidal(Func):
    def __init__(self, amp: float, period: float, **kwargs):
        super().__init__()
        self.amp = amp
        self.phase = 2 * pi / period
    def shouldUpdate(self):
        return True
    def update(self):
        self.out(sin(time() * self.phase) * self.amp)
    
class AddN(Func):
    def __init__(self, opOne: Output[int], n, **kwargs):
        super().__init__()
        self.n = n
    def update(self):
        newVal = self.opOne() + self.n
        self.out(newVal)
        sleep(1)
class Counter(Func):
    def __init__(self, src: Output[int], **kwargs):
        super().__init__()
        self.counter = 0
    def update(self):
        if self.src():
            self.counter = self.counter + 1
            self.out(self.counter)

def main():
    sine = Sinusoidal(1, 1)
    sine >> then(Gauge, minVal=-1, maxVal=1)
    sine >> then(Gauge, minVal=-1, maxVal=1)
    sine >> then(Gauge, minVal=-1, maxVal=1)
    gridder.nextRow()
    bigSine = Sinusoidal(4, 2)
    # AddN blocks for a second so we dump it on its own thread
    bigSine >> then(AddN, 1, thread=3) >> TextLabel
    bigSine >> then(TextLabel, inline=True)
    bigSine >> then(TextLabel)
    ToggleButton(label='toggly boi') >> Counter >> then(TextLabel, inline=True)
    PushButton(label='pushy boi') >> Counter >> then(TextLabel, inline=True)
    gridder.nextRow(rowHeight=2*TEXT_HEIGHT)
    NumericInput(label='hi') >> then(TextLabel, inline=True)
    startGui()

if __name__ == '__main__':
    main()