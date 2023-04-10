import pygame
from pygame.locals import *
from inputField import *

from OpenGL.GL import *
from OpenGL.GLU import *

class Cube:
    def __init__(self,x,y,z,rx,ry,rz,sx,sy,sz):
        self.x = x
        self.y = y
        self.z = z