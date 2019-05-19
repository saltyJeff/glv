import pygame
from GlvCommon import *
from typing import List
from GlvGui.Gridder import Gridder, WINDOW_HEIGHT, WINDOW_WIDTH
from time import time

pygame.init()

sansFont = pygame.font.SysFont("Calibri", 18)
serifFont = pygame.font.SysFont("Courier", 18)
detailFont = pygame.font.SysFont("Courier", 12)
accent = (255,255,255)
back = (0,0,0)

gridder = Gridder()

root = pygame.display.set_mode((0, 0), pygame.RESIZABLE)

guiFuncs: List[Func] = list()
def registerSelf(func: Func):
    guiFuncs.append(func)

def startGui():
    try:
        glvLoop()
    except Exception as e:
        print(e)
        traceback.print_exc()
    finally:
        killThreads()

dying = False
WINDOW_WIDTH, WINDOW_HEIGHT = pygame.display.get_surface().get_size()
def glvLoop():
    global dying
    while not dying:
        startTime = time()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                dying = True
            elif event.type == pygame.VIDEORESIZE:
                WINDOW_WIDTH = event.w
                WINDOW_HEIGHT = event.h
                
        root.fill(back) # update blanking
        for guiFunc in guiFuncs:
            guiFunc.guiUpdate()
        pygame.display.flip()
        # hz display
        timeSpan = time() - startTime
        if timeSpan != 0:
            rate = 1 / timeSpan
            #pygame.display.set_caption(f'Glv Gui ( {rate:05.2f} hz )')
            print(f'Glv Gui ( {rate:05.2f} hz )', end='\r')
        else:
            pygame.display.set_caption('Glv Gui ( ♾️ hz )')
    killThreads()