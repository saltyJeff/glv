from inspect import getmembers
from typing import List, Tuple, Generic, TypeVar
from GlvCommon.FuncVars import Input, Output
from GlvCommon.FuncThread import getThread
from inspect import FrameInfo, currentframe
from shortuuid import uuid

T = TypeVar('T')
class Func(Generic[T]):
    inputs: List[Input]
    output: Output[T]
    uuid: str
    name: str
    def __init__(self):
        lastFrame = currentframe().f_back
        locals = lastFrame.f_locals
        argNames: list[str] = list(lastFrame.f_code.co_varnames)

        def cleanArgs(varName: str):
            if varName == 'self' or varName.startswith('_'):
                return False
            if isinstance(locals[varName], Output):
                return True
            return False

        cleanedArgs = list(filter(cleanArgs, argNames))
        
        def registerInputs(varName: str) -> Input:
            outputVar = locals[varName]
            inputVar = Input(self, outputVar)
            inputVar.name = varName
            setattr(self, varName, lambda: inputVar.value()) # makes life easier
            setattr(self, 'in_'+varName, inputVar) # makes life easier
            return inputVar

        self.inputs = list(map(registerInputs, cleanedArgs))
        self.name = locals['__class__'].__name__
        self.output = Output[T](self)
        self.out = self.output.assign
        self.uuid = uuid()

        getThread(0).attachFunc(self)

    def shouldUpdate(self) -> bool:
        for inputVar in self.inputs:
            if inputVar.dirty:
                return True
        return False
    def update(self):
        print('Unimplemented update', self)
    def __rshift__(self, ctor):
        return ctor(self.output)
    def cleanAll(self):
        for inputVar in self.inputs:
            inputVar.dirty = False

def isGlvIn(memberTuple) -> bool:
    obj = memberTuple[1].__class__
    return obj is not None and issubclass(obj, Input)