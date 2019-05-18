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
    def __init__(self, opOne: Output[int], n):
        super().__init__()
        self.n = n
    def update(self):
        newVal = self.opOne() + self.n
        self.out(newVal)

def main():
    sine = Sinusoidal(1, 1)
    sine >> then(AddN, 4) >> TextLabel
    sine >> then(AddN, 4) >> TextLabel
    sine >> then(AddN, 4) >> TextLabel
    sine >> then(AddN, 4) >> TextLabel
    sine >> then(AddN, 4) >> TextLabel
    sine >> then(AddN, 4) >> TextLabel
    sine >> then(AddN, 4) >> TextLabel
    sine >> then(AddN, 4) >> TextLabel
    sine >> then(AddN, 4) >> TextLabel
    sine >> then(AddN, 4) >> TextLabel
    sine >> then(AddN, 4) >> TextLabel
    sine >> then(AddN, 4) >> TextLabel
    sine >> then(AddN, 4) >> TextLabel
    sine >> then(AddN, 4) >> TextLabel
    sine >> then(AddN, 4) >> TextLabel
    sine >> then(AddN, 4) >> TextLabel
    gridder.nextRow()
    # sine >> then(AddN, 1) >> then(Gauge, thread=1, maxValue=2)
    startGui()

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
        traceback.print_exc()
        killThreads()
        exit(1)