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

events = None
def getEvents():
    return events
mousePressedEvt = False
mouseReleasedEvt = False
def mousePos():
    return pygame.mouse.get_pos()
def mousePressed():
    return mousePressedEvt
def mouseReleased():
    return mouseReleasedEvt
def processEvents():
    global dying, mousePressedEvt, mouseReleasedEvt, events
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            dying = True
        elif event.type == pygame.VIDEORESIZE:
            WINDOW_WIDTH = event.w
            WINDOW_HEIGHT = event.h
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mousePressedEvt = True
        elif event.type == pygame.MOUSEBUTTONUP:
            mouseReleasedEvt = True        
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F1:
                colors.toggle()
            if event.key == pygame.K_F2:
                graph = makeGraph()
                try:
                    graph.view()
                except Exception as e:
                    print(e)
                    print(graph)
                    print('Could not open graphview visualizer, do you have them installed from https://www.graphviz.org/download/ ?')
def resetEvents():
    global mousePressedEvt, mouseReleasedEvt
    mousePressedEvt = False
    mouseReleasedEvt = False
def glvLoop():
    while not dying:
        startTime = time()
        processEvents()
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

        resetEvents()
    killThreads()