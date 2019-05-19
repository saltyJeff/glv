from GlvGui.GlvGui import root

class Gridder:
    def __init__(self):
        self.thisRow = 0
        self.thisCol = 0
        self.maxCol = 0
    def shareRow(self):
        return self.thisRow
    def nextRow(self):
        self.thisRow = self.thisRow + 1
        self.thisCol = 0
        return self.thisRow
    def takeRow(self):
        ret = self.thisRow
        self.nextRow()
        return ret
    def takeCol(self):
        ret = self.thisCol
        if ret == self.maxCol:
            root.grid_columnconfigure(ret, minsize=200)
            self.maxCol = self.maxCol + 1
        self.thisCol = self.thisCol + 1
        return ret