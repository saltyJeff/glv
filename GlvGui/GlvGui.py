import pygame
from GlvCommon import *
from typing import List
from GlvGui.Gridder import Gridder, WINDOW_HEIGHT, WINDOW_WIDTH
from time import time
from GlvGui.ColorManager import ColorManager
import traceback

pygame.init()

sansFont = pygame.font.SysFont("Calibri", 18)
serifFont = pygame.font.SysFont("Courier", 18)
detailFont = pygame.font.SysFont("Courier", 12)

gridder = Gridder()
colors = ColorManager()

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
            elif event.type == pygame.KEYDOWN:
                if event.unicode == 'd':
                    colors.toggle()
                if event.unicode == 'g':
                    graph = makeGraph()
                    try:
                        graph.view()
                    except Exception as e:
                        print(e)
                        print('Could not open graphview visualizer, do you have them installed from https://www.graphviz.org/download/')
                        print('Dumping graph below:')
                        print(graph)
                
        root.fill(colors.back()) # update blanking
        for guiFunc in guiFuncs:
            guiFunc.guiUpdate()
        
        # hz display
        timeSpan = time() - startTime
        caption = '( ♾️ hz )'
        if timeSpan != 0:
            rate = 1 / timeSpan
            caption = f'{rate:06.2f} hz '
        surface = serifFont.render(caption, False, colors.text())
        root.blit(surface, (WINDOW_WIDTH - surface.get_width(), 0))
        pygame.display.flip()
    killThreads()