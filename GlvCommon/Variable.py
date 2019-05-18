from GlvCommon import Func, Input, Output
from typing import Generic, TypeVar, Type
T = TypeVar('T')
class Variable(Func[T]):
    name: str
    def __init__(self, setter: Output[T], name: str = 'unknown var'):
        super().__init__()
        self.name = name
        self.setter = setter
    
    def update(self, literal=None):
        if literal is not None:
            self.output.assign(literal)
        else:
            self.output.assign(self.inputs[0].value())