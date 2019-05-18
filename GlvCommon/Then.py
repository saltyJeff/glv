from GlvCommon import Func
from GlvCommon.Infix import Infix

def then(*args):
    @Infix
    def ret(fromFunc: Func, toFunc):
        return toFunc(fromFunc.output, *args)
    return ret
