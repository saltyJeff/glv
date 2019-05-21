from GlvCommon import *
from GlvGui import *
from mainFuncs import *

def main():
    sine = Sinusoidal(1, 1)
    sine >> then(Gauge, minVal=-1, maxVal=1)
    sine >> then(Gauge, minVal=-1, maxVal=1)
    sine >> then(Gauge, minVal=-1, maxVal=1)
    bigSine = Sinusoidal(4, 2)
    grid().nextRow() # use nextRow to move all the gui stuff to the next row
    # AddN blocks for a second so we dump it on its own thread
    bigSine >> then(AddN, 1, thread=3) >> TextLabel
    bigSine >> TextLabel
    bigSine >> TextLabel
    grid().nextRow()
    ToggleButton(label='toggly boi') >> Counter >> TextLabel
    PushButton(label='pushy boi') >> Counter >> TextLabel
    nextPage()
    NumericInput(label='hi') >> TextLabel
    grid().nextRow()
    StringInput(label='string stuff') >> TextLabel
    startGui()

if __name__ == '__main__':
    main()