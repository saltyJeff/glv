from GlvCommon import *
from math import *
from time import sleep, time
import multiprocessing

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
        if self.opOne() is not None:
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
def fib(n): 
    if n==1: 
        return 0
    elif n==2: 
        return 1
    else: 
        return fib(n-1)+fib(n-2)

class Fibbonaci(Func):
    def __init__(self, **kwargs):
        super().__init__()
        self.procs = multiprocessing.Pool(1)
        self.resolved = False
    def shouldUpdate(self):
        if self.resolved:
            self.resolved = False
            return True
        return False
    def update(self):
        fibVal = self.procs.apply(fib, (100,))
        self.out(fibVal)
        self.resolved = True