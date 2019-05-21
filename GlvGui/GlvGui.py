import pygame
from GlvCommon import *
from typing import List, Dict
from GlvGui.Gridder import Gridder, WINDOW_HEIGHT, WINDOW_WIDTH
from time import time
from GlvGui.ColorManager import ColorManager
import traceback
from random import *

pygame.init()

sansFont = pygame.font.SysFont("Calibri", 18)
serifFont = pygame.font.SysFont("Courier", 18)
detailFont = pygame.font.SysFont("Courier", 12)

colors = ColorManager()

root = pygame.display.set_mode((0, 0), pygame.RESIZABLE)

pageIndex = 0
grids: Dict[int, Gridder] = {}
pageWidgets: Dict[int, List] = {}
def grid():
    global pageIndex
    if not pageIndex in grids:
        grids[pageIndex] = Gridder()
    return grids[pageIndex]
def registerSelf(func):
    global pageWidgets, pageIndex
    if not pageIndex in grids:
        pageWidgets[pageIndex] = []
    pageWidgets[pageIndex].append(func)
def nextPage():
    global pageIndex
    pageIndex = pageIndex + 1
def prevPage():
    global pageIndex
    pageIndex = pageIndex - 1
def startGui():
    global pageIndex
    try:
        pageIndex = 0
        grid()
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
    global dying, mousePressedEvt, mouseReleasedEvt, events, WINDOW_HEIGHT, WINDOW_WIDTH
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
            elif event.key == pygame.K_F2:
                graph = makeGraph()
                try:
                    graph.view()
                except Exception as e:
                    print(e)
                    print(graph)
                    print('Could not open graphview visualizer, do you have them installed from https://www.graphviz.org/download/ ?')
            elif event.key == pygame.K_F3:
                prevPage()
            elif event.key == pygame.K_F4:
                nextPage()

def resetEvents():
    global mousePressedEvt, mouseReleasedEvt
    mousePressedEvt = False
    mouseReleasedEvt = False
def glvLoop():
    while not dying:
        startTime = time()
        processEvents()
        root.fill(colors.back()) # update blanking
        if pageIndex in pageWidgets:
            for guiFunc in pageWidgets[pageIndex]:
                guiFunc.guiUpdate()
        
        # hz display
        timeSpan = time() - startTime
        caption = f'pg {pageIndex} '
        refreshCaption = '( ♾️ hz )'
        if timeSpan != 0:
            rate = 1 / timeSpan
            refreshCaption = f'( {rate:06.2f} hz )'
        caption += refreshCaption
        surface = serifFont.render(caption, False, colors.text())
        root.blit(surface, (WINDOW_WIDTH - surface.get_width(), 0))
        pygame.display.flip()

        resetEvents()
    killThreads()