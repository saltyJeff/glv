from typing import Type, Any, Set, Generic, TypeVar, Optional
from inspect import *

T = TypeVar('T')

class Output(Generic[T]):
    last: Optional[T]
    value: Optional[T]
    def __init__(self, func, val: Optional[T] = None):
        self.last = None
        self.value = None
        self.func = func
        self.listeners: Set[Input[T]] = set() #not sure why i can't declare earlier
        self.assign(val)
        
    def assign(self, newValue: Any, notify=True):
        self.last = self.value
        self.value = newValue
        if notify:
            for listener in self.listeners:
                listener.dirty = True
    def name(self):
        return self.func.name
    
class Input(Generic[T]):
    dirty: bool
    name: str
    def __init__(self, func, listenTo: Output[T]):
        self.attatchTo(listenTo)
        self.dirty = True
        self.func = func
        self.name = 'unbound'
    def attatchTo(self, listenTo: Output[T]):
        self.attachedTo = listenTo
        if listenTo is not None:
            listenTo.listeners.add(self)    
    def value(self, clean=True):
        if clean:
            self.dirty = False
        return self.attachedTo.value
    def last(self):
        return self.attachedTo.last
    def attached(self):
        return self.attachedTo
    def sourceName(self):
        return self.attachedTo.name()

def typesEqual(typ1: Type, typ2: Type):
    if typ1 is None or typ2 is None:
        return True
    if typ1 is type(None) or typ2 is type(None):
        return True
    if typ1 is Any or typ2 is Any:
        return True
    if typ1 is typ2:
        return True
    return issubclass(typ1, typ2)
    