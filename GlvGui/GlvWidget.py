from GlvCommon import Func, Input, Output
from GlvGui.GlvGui import *
from inspect import currentframe

class GlvWidget(Func):
    page: int
    def __init__(self, **kwargs):
        super().__init__(lastFrame=currentframe().f_back)
        self.page = registerSelf(self)
    def guiUpdate(self):
        print(f'unimplemented graphics update on {self.name}')
