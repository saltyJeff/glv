from GlvCommon import *
from math import *
from time import sleep, time
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