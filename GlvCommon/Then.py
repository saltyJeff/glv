from GlvCommon import Func
from GlvCommon.Infix import Infix

# higher order all the things
def then(toFunc, *args, **kwargs):
    def ret(_):
        return toFunc(_, *args, **kwargs)
    return ret
