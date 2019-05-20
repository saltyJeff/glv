from GlvCommon import Func, Input, Output
from typing import Generic, TypeVar, Type, Any

class Print(Func):
    def __init__(self, src):
        super().__init__()
    def update(self):
        print(self.in_src.sourceName()+': '+str(self.in_src.value()))
