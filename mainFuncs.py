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
    a = 0
    b = 1
    if n < 0: 
        print("Incorrect input") 
    elif n == 0: 
        return a 
    elif n == 1: 
        return b 
    else: 
        for i in range(2,n): 
            c = a + b 
            a = b 
            b = c 
        return b

class Fibbonaci(Func):
    def __init__(self, **kwargs):
        super().__init__()
        pool()
        self.ready = True
    def shouldUpdate(self):
        return self.ready
    def update(self):
        self.ready = False
        result = pool().apply_async(fib, (90000,))
        start = time()
        try:
            # a high timeout may lead to slower shutdowns as the thread can't check for its exit condition
            val = result.get(timeout=3)
            #self.out(val) # remove comment if you want to dump the actual value of the fib
        except multiprocessing.TimeoutError:
            print("Process timed out")
        span = time() - start
        self.out(span) # comment out if you want the value of the fib. This just shows how long it takes to calculate the fib
        self.ready = True
