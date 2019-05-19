COL_WIDTH = 200
ROW_HEIGHT = 175
TEXT_HEIGHT = 25
RIGHT_PAD = 15
BOTTOM_PAD = 10
LEFT_PAD = 15
TOP_PAD = 15
WINDOW_WIDTH = 0
WINDOW_HEIGHT = 0
class Gridder:
    def __init__(self):
        self.thisX = LEFT_PAD
        self.thisY = TOP_PAD
        self.maxCol = 0
    def shareRow(self):
        return self.thisY
    def nextRow(self, rowHeight=ROW_HEIGHT):
        self.thisY = self.thisY + rowHeight + BOTTOM_PAD
        self.thisX = LEFT_PAD
        return self.thisY
    def takeRow(self, rowHeight=ROW_HEIGHT):
        ret = self.thisY
        self.nextRow(rowHeight=rowHeight)
        return ret
    def takeCol(self, colWidth=COL_WIDTH, overflowHeight=ROW_HEIGHT):
        ret = self.thisX
        self.thisX = self.thisX + colWidth + RIGHT_PAD
        return ret