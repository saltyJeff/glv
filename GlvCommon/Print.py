from GlvCommon import Func, Input, Output
from typing import Generic, TypeVar, Type, Any

class Print(Func):
    def __init__(self, src):
        super().__init__()
    def update(self):
        for inputVar in self.inputs:
            print(inputVar.sourceName()+': '+str(inputVar.value()), end='\t')
        print()