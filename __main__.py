from GlvCommon import *
from typing import List
from time import sleep, time
import traceback
from logging import getLogger, Logger, INFO, basicConfig

basicConfig(
    format='%(asctime)s %(levelname)s %(name)s - %(message)s',
    datefmt='%m/%d/%Y %H:%M:%S')
logger: Logger = getLogger()
logger.setLevel(INFO)

class AddThree(Func):
    def __init__(self, opOne: Output[int]):
        super().__init__()
    def update(self):
        newVal = self.opOne() + 3
        self.output.assign(newVal)

def main():
    varFunc = Const(8) |then('potato')| Variable
    varFunc >> AddThree >> AddThree >> AddThree \
            >> Print

    while True:
        newVal = int(input("Enter a number: "))
        if newVal == -1:
            killThreads()
            exit()
        print('Expect to see it plus 3')
        varFunc.update(newVal)

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
        traceback.print_exc()
        killThreads()
        exit(1)