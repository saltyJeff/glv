from GlvCommon.Func import Func
from GlvCommon.FuncVars import Input, Output
from typing import TypeVar
T = TypeVar('T')

class Const(Func[T]):
    def __init__(self, val: T):
        super().__init__()
        self.output.assign(val)
    def shouldUpdate(self):
        return False