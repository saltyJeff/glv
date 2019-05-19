COL_WIDTH = 200
ROW_HEIGHT = 175
TEXT_HEIGHT = 25
class Gridder:
    def __init__(self):
        self.thisX = 0
        self.thisY = 0
        self.maxCol = 0
    def shareRow(self):
        return self.thisY
    def nextRow(self, rowHeight=ROW_HEIGHT):
        self.thisY = self.thisY + rowHeight
        self.thisX = 0
        return self.thisY
    def takeRow(self, rowHeight=ROW_HEIGHT):
        ret = self.thisY
        self.nextRow(rowHeight=rowHeight)
        return ret
    def takeCol(self, colWidth=COL_WIDTH):
        ret = self.thisX
        self.thisX = self.thisX + colWidth
        return ret