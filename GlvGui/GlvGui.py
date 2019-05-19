import pygame
from GlvCommon import *
from typing import List
from GlvGui.Gridder import Gridder
from time import time

pygame.init()

sansFont = pygame.font.SysFont("Calibri", 18)
serifFont = pygame.font.SysFont("Courier", 18)
detailFont = pygame.font.SysFont("Courier", 12)
accent = (255,255,255)
back = (0,0,0)

gridder = Gridder()

root = pygame.display.set_mode((0, 0), pygame.RESIZABLE)

# setting it directly to 648x480 means the update blanks only the smaller window
# instead of the whole thing
pygame.display.set_mode((648, 480), pygame.RESIZABLE)

dying = False
guiFuncs: List[Func] = list()
def registerSelf(func: Func):
    guiFuncs.append(func)

def startGui():
    global dying
    while not dying:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dying = True
        
        startTime = time()
        root.fill(back) # update blanking
        for guiFunc in guiFuncs:
            guiFunc.guiUpdate()
        pygame.display.flip()
        # hz display
        timeSpan = time() - startTime
        if timeSpan != 0:
            rate = 1 / timeSpan
            pygame.display.set_caption(f'Glv Gui ( {rate:05.2f} hz )')
        else:
            pygame.display.set_caption('Glv Gui ( ♾️ hz )')
    killThreads()