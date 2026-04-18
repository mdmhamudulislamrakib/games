from OpenGL.GL import *
from OpenGL.GLUT import *


def bresenham_line(x0, y0, x1, y1):
    """Draw a line using Bresenham's algorithm"""
    points = []
    dx = abs(x1 - x0)
    dy = abs(y1 - y0)
    sx = 1 if x0 < x1 else -1
    sy = 1 if y0 < y1 else -1
    err = dx - dy
    x, y = x0, y0
    
    while True:
        glVertex2f(x, y)
        if x == x1 and y == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x += sx
        if e2 < dx:
            err += dx
            y += sy


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()


#normal line
    glBegin(GL_LINES)
    glColor3f(1.0, 1.0, 1.0)
    glVertex2f(50, 50)
    glVertex2f(100, 50)
    glEnd()

#bresenham_line
    glBegin(GL_LINES)
    glColor3f(1.0, 1.0, 1.0)
    bresenham_line(50, 100, 150, 100)
    glEnd()


    glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"Drawing Pixels")
glutDisplayFunc(showScreen)

glutMainLoop()