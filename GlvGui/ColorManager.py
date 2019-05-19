class ColorManager(object):
    def __init__(self):
        self._dark = True
        self.setColors()
    def setColors(self):
        if self._dark:
            self._text = (255, 255, 255)
            self._back = (0,0,0) 
            self._accent = (255, 0, 0)
        else:
            self._text = (0,0,0)
            self._back = (255,255,255) 
            self._accent = (0, 0, 255)
    def toggle(self):
        self._dark = not self._dark
        self.setColors()
        return self._dark
    def text(self):
        return self._text
    def back(self):
        return self._back
    def accent(self):
        return self._accent