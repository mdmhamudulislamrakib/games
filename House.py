import os

from OpenGL.GL import *
from OpenGL.GLUT import *
 

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, -1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def draw_house():
    # House body
    glColor3f(0.82, 0.71, 0.55)
    glBegin(GL_QUADS)
    glVertex2f(200, 100)
    glVertex2f(400, 100)
    glVertex2f(400, 300)
    glVertex2f(200, 300)
    glEnd()

    # Roof
    glColor3f(0.85, 0.2, 0.2)
    glBegin(GL_TRIANGLES)
    glVertex2f(200, 300)
    glVertex2f(400, 300)
    glVertex2f(300, 450)
    glEnd()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    draw_house()
    glutSwapBuffers()


def main():
    # Some terminals export DISPLAY in a way that confuses freeglut on Windows.
    os.environ.pop("DISPLAY", None)

    glutInit([])
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"House")
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glutDisplayFunc(showScreen)
    glutIdleFunc(showScreen)
    glutMainLoop()


if __name__ == "__main__":
    main()