#SENTDEX-OpenGL with PyOpenGL tutorial Python and PyGame - Part 2.2
#--- HD Colouring of Surfaces -Example-Nov 6th 2014

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

# 8 verticies(nodes)
verticies = (
    (1,-1,-1),
    (1,1,-1),
    (-1,1,-1),
    (-1,-1,-1),
    (1,-1,1),
    (1,1,1),
    (-1,-1,1),
    (-1,1,1)
    )

# 12 egdes:
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

surfaces=(
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6)
    
    )

colors = (
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (0,0,0),
    (1,1,1),
    (0,1,1),
    (1,0,0),
    (0,1,0),
    (0,0,1),
    (1,0,0),
    (1,1,1),
    (0,1,1)
    )

def Cube():

    glBegin(GL_QUADS)
    
    for surface in surfaces:
        x =0

        for vertex in surface:
            x += 1
            glColor3fv(colors[x])   ##glColor3fv((0,1,0))  #  0:minimum ; 1:maximum
            glVertex3fv(verticies[vertex])





    glEnd()











    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])

    glEnd()


def main():
    pygame.init()
    display =(800,600)
    pygame.display.set_mode(display,DOUBLEBUF|OPENGL)

    gluPerspective(45,(display[0]/display[1]) ,0.1, 50)


    """Notation:glTranslate(x,y,z)"""
    glTranslate(0,0.1,-5)

    """ EXPLANATION:glRotate(degree,move in x,?,?)"""
    glRotate(26,3,1,0)   #  this "rotation function is at STATIC POINT"  but will makes the ANIMATION IN 3D later on

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        """Notation:glRotate(x,y,z)"""
        #glRotate(1,3,2,1)
        #glRotate(1,1,-1,1)
        glRotate(1,4,1,1)         #--- This " rotation Function" IGNITES The rotation in FULL motion""
                

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)

main()
