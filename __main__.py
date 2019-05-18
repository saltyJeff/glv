from GlvCommon import *
from GlvGui import *
from typing import List
from time import sleep, time
import traceback
from logging import getLogger, Logger, INFO, basicConfig
from math import sin, pi

basicConfig(
    format='%(asctime)s %(levelname)s %(name)s - %(message)s',
    datefmt='%m/%d/%Y %H:%M:%S')
logger: Logger = getLogger()
logger.setLevel(INFO)

class Sinusoidal(Func):
    def __init__(self, amp: float, period: float):
        super().__init__()
        self.amp = amp
        self.phase = 2 * pi / period
    def shouldUpdate(self):
        return True
    def update(self):
        self.out(sin(time() * self.phase) * self.amp)
    
class AddThree(Func):
    def __init__(self, opOne: Output[int]):
        super().__init__()
    def update(self):
        newVal = self.opOne() + 3
        self.out(newVal)

def main():
    sine = Sinusoidal(1, 1)
    sine >> TextLabel
    sine >> AddThree >> TextLabel
    startGui()

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
        traceback.print_exc()
        killThreads()
        exit(1)