from threading import Thread
from typing import List, Dict
from time import time
from logging import getLogger, Logger
import traceback
class FuncThread(Thread):
    def __init__(self, num: int):
        super().__init__()
        self.funcs: List = []
        self.die = False
        self.num = num
        self.logger: Logger = getLogger(f'FuncThread{num}')
    def kill(self):
        self.die = True
    def attachFuncs(self, funcs: List):
        for arg in funcs:
            self.funcs.append(arg)
    def attachFunc(self, func):
        self.funcs.append(func)
    def run(self):
        self.logger.warn('Starting')
        while self.die is False:
            try:
                for func in self.funcs:
                    if func.shouldUpdate():
                        start = time()
                        func.update()
                        self.logger.debug(f'{type(func).__name__}: {(time() - start):.2f}s')
            except Exception as e:
                self.logger.error(e)
                traceback.print_exc()
        self.logger.warn('Dead')

logger = getLogger('ThreadPool')
pool: Dict[int, FuncThread] = {}
def getThread(num: int) -> FuncThread:
    if not (num in pool):
        newThread = FuncThread(num)
        newThread.start()
        pool[num] = newThread
        logger.warn(f'Spawning new thread {num}')
        return newThread
    return pool[num]

def killThreads():
    for num,thread in pool.items():
        thread.kill()