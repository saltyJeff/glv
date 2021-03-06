import pygame
from GlvCommon import *
from typing import List, Dict
from GlvGui.Gridder import Gridder
from time import time
from GlvGui.ColorManager import ColorManager
import traceback
from random import *
import sys

pygame.font.init()

sansFont = pygame.font.SysFont("Calibri", 18)
serifFont = pygame.font.SysFont("Courier", 18)
detailFont = pygame.font.SysFont("Courier", 12)

colors = ColorManager()

pageIndex = 0
grids: List[Gridder] = [Gridder()]
pageWidgets: List[List] = [[]]
def grid():
    return grids[pageIndex]
def registerSelf(func):
    pageWidgets[pageIndex].append(func)
def nextPage():
    global pageIndex, pageWidgets, pageGrids
    pageIndex = pageIndex + 1
    if pageIndex >= len(pageWidgets):
        pageWidgets.append([])
        grids.append(Gridder())
def prevPage():
    global pageIndex
    if pageIndex is 0:
        return
    pageIndex = pageIndex - 1
pageBack = prevPage
def pageForward():
    global pageIndex
    if pageIndex >= len(grids) - 1:
        return
    pageIndex = pageIndex + 1
root_surface = None
WINDOW_WIDTH = 0 
WINDOW_HEIGHT = 0
def root():
    return root_surface
def startGui():
    global pageIndex, root_surface
    try:
        pygame.init()
        # exit is CMD OPT Q
        openFlags = pygame.RESIZABLE
        if sys.platform == 'darwin':
            openFlags = pygame.FULLSCREEN | pygame.HWSURFACE
            macRant()
        root_surface = pygame.display.set_mode((0, 0), openFlags)
        WINDOW_WIDTH, WINDOW_HEIGHT = pygame.display.get_surface().get_size()
        pageIndex = 0
        startThreads()
        grid()
        glvLoop()
    except Exception as e:
        print(e)
        traceback.print_exc()
        killThreads()

dying = False

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
                pageBack()
            elif event.key == pygame.K_F4:
                pageForward()
            elif event.key == pygame.K_ESCAPE:
                dying = True

def resetEvents():
    global mousePressedEvt, mouseReleasedEvt
    mousePressedEvt = False
    mouseReleasedEvt = False
def glvLoop():
    pageCount = len(grids)
    while not dying:
        startTime = time()
        processEvents()
        root().fill(colors.back()) # update blanking
        for guiFunc in pageWidgets[pageIndex]:
            guiFunc.guiUpdate()
        
        # hz display
        timeSpan = time() - startTime
        caption = f'pg {pageIndex+1}/{pageCount} '
        refreshCaption = '( ♾️ hz )'
        if timeSpan != 0:
            rate = 1 / timeSpan
            refreshCaption = f'( {rate:06.2f} hz )'
        caption += refreshCaption
        surface = serifFont.render(caption, False, colors.text())
        root().blit(surface, (WINDOW_WIDTH - surface.get_width(), 0))
        pygame.display.flip()

        resetEvents()
    killThreads()

def macRant():
    print('<<< MAC USER DETECTED >>>')
    print("I see you're on a mac and you should be ashamed of yourself")
    print("This screen will freeze for like 5 seconds, then move your mouse")
    print("to the top and minimize the screen. This is a mac-only hac.")
    print("Don't forget: hold FN key to trigger function keys")
    print('<<< ESC KEY TO CLOSE GUI >>>')