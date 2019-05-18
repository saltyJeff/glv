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
    constArgStr: str
    inputArgStr: str
    def __init__(self, lastFrame=None, *args, **kwargs):
        if lastFrame is None:
            lastFrame = currentframe().f_back
        locals = lastFrame.f_locals
        argNames: list[str] = list(lastFrame.f_code.co_varnames)

        self.constArgs: list = list()
        def cleanArgs(varName: str):
            if varName == 'self' or varName == 'kwargs' or varName.startswith('_') or not varName in locals:
                return False
            if isinstance(locals[varName], Output):
                return True
            self.constArgs.append((varName, str(locals[varName])))
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
        self.output = Output[T](self)
        self.out = self.output.assign
        if 'uuid' in argNames:
            self.uuid = locals['uuid']
        else:
            self.uuid = uuid()[:5]

        self.name = locals['__class__'].__name__
        self.name += f'_{self.uuid}'

        self.constArgStr = ''
        if len(self.constArgs) > 0:
            self.constArgStr += '(\n'
            for constArg in self.constArgs:
                if constArg[0] in hiddenVars:
                    continue
                self.constArgStr += f'{constArg[0]}={constArg[1]}\n'
            self.constArgStr += ')'

        self.inputArgStr = ''
        for inputVar in self.inputs:
            self.inputArgStr += f'\n{inputVar.name} ← {inputVar.sourceName()}'
        self.threadNum = 0

        if 'kwargs' in locals:
            kwargs = locals['kwargs']
            if 'thread' in kwargs:
                print('thread overrun')
                self.threadNum = kwargs['thread']
            getThread(self.threadNum).attachFunc(self)

    def initFunc(*args, **kwargs):
        print(f'No init {args}, {kwargs}')
        
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

hiddenVars = ['lastFrame']

def isGlvIn(memberTuple) -> bool:
    obj = memberTuple[1].__class__
    return obj is not None and issubclass(obj, Input)