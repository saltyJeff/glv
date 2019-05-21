COL_WIDTH = 200
ROW_HEIGHT = 175
TEXT_HEIGHT = 25
RIGHT_PAD = 15
BOTTOM_PAD = 10
LEFT_PAD = 15
TOP_PAD = 15
class Gridder:
    def __init__(self):
        self.thisX = LEFT_PAD
        self.thisY = TOP_PAD
        self.maxCol = 0
        self.xMax = 0
    def shareRow(self, rowHeight=ROW_HEIGHT):
        self.xMax = max(self.xMax, rowHeight)
        return self.thisY
    def nextRow(self, rowHeight=0):
        self.thisY = self.thisY + self.xMax + BOTTOM_PAD
        self.xMax = 0
        self.thisX = LEFT_PAD
        return self.shareRow(rowHeight=rowHeight)
    def takeCol(self, colWidth=COL_WIDTH):
        ret = self.thisX
        self.thisX = self.thisX + colWidth + RIGHT_PAD
        return ret