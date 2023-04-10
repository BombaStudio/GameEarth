import pygame
from pygame.locals import *
from inputField import *

from OpenGL.GL import *
from OpenGL.GLU import *

x = 0
y = 0
z = 0

verticies = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (1, -1, 1),
    (1, 1, 1),
    (-1, -1, 1),
    (-1, 1, 1)
    )
v2 = (
    (-1,0,0),
    (-1,1,0),
    (1,1,0),
    (1,0,0)
)
edges = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )
edge2 = (
    (0,1),
    (1,2),
    (2,3),
    (3,4)
    
)

def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            try:
                glVertex3fv(v2[vertex])
            except:
                pass
                #print("error: ")
    glEnd()


def main():
    z = -5
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, z)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        keys=pygame.key.get_pressed()
        if keys[K_a]: 
            x = 1
            glTranslatef(x/10,0,0)
        if keys[K_d]: 
            x = -1
            glTranslatef(x/10,0,0)
        if keys[K_w]: 
            z = 1
            glTranslatef(0,0, z/10)
        if keys[K_s]: 
            z = -1
            glTranslatef(0,0, z/10)
        if keys[K_LEFT]:
            glRotatef(1,0,1,0)
        if keys[K_RIGHT]:
            glRotatef(-1,0,1,0)
        #glRotatef(1, 3, 1, 1)
        
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)


main()