import numpy as np
import pygame
from pygame.locals import *

import OpenGL

import OpenGL.GL

import OpenGL.GLE

import OpenGL.GLUT

from OpenGL.GL import *
from OpenGL.GLU import *

def main():
    pygame.init()
    screen =pygame.display.set_mode((500,400))

    pygame.display.set_caption("my canvas")

    screen.set_at((300, 300),(221,160,221) )

    running = True
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_A:
                running = False
        
        screen.fill((255,255,255))

        pygame.draw.line(screen,(255,0,0),(50,50),(50,200),3)

        pygame.draw.polygon(screen,(255,0,0),[(100,150),(150,100),(200,150)])
        pygame.draw.polygon(screen,(0,0,255),[(150,200),(100,150),(200,150)])

        pygame.draw.circle(screen,[221,160,221],[150, 150], 5)                

    
        
        pygame.display.update()

    pygame.quit()


# main()

def triangle():
    pygame.init()

    screen = pygame.display.set_mode((500,400))

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
        
        pygame.draw.polygon(screen,(221,160,221),[(100,150),(150,100),(200,150)])

        

        pygame.display.update()
    
    pygame.quit()

# triangle()




def draw_line(x1, y1, x2, y2):
    glBegin(GL_LINES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(x1, y1)
    glVertex2f(x2, y2)
    glEnd()

def draw():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluOrtho2D(0, 800, 0, 600)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT)
        draw_line(100, 100, 700, 500)
        pygame.display.flip()
        pygame.time.wait(10)

# draw()
