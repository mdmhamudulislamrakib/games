#1.using Gl_lines to write character "B" in a 2D plane, use glrotate() function to rotate the 
#character clockwise continuously. [ Based on Tmain.py file] 
#a) change the default background color of the viewing window. 
#b) Complete the “B” character lines. 

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

angleZ = 0.0
rotSpeed = 2.0  # degrees per frame (clockwise)

def draw_B():
    glColor3f(0.4, 0.9, 1.0)
    glLineWidth(3.0)
    glBegin(GL_LINES)

    # --- Vertical spine (left side of B) ---
    glVertex2f(200, 350)   # top
    glVertex2f(200, 150)   # bottom
    
    # --- Top horizontal bar ---
    glVertex2f(200, 350)
    glVertex2f(270, 350)

    # --- Middle horizontal bar ---
    glVertex2f(270, 350)
    glVertex2f(325, 310)

    # --- Middle connector from spine ---
    glVertex2f(200, 250)
    glVertex2f(270, 250)

    # --- Bottom horizontal bar ---
    glVertex2f(320, 220)
    glVertex2f(320, 180)

    # --- Bottom connector from spine ---
    glVertex2f(200, 150)
    glVertex2f(270, 150)


    # --- Top bump (upper curve of B) ---
    glVertex2f(325, 310)
    glVertex2f(310, 325)

    glVertex2f(310, 325)
    glVertex2f(310, 275)

    glVertex2f(310, 275)
    glVertex2f(270, 250)

    # --- Bottom bump (lower curve, slightly wider) ---
    glVertex2f(270, 250)
    glVertex2f(320, 220)

    glVertex2f(320, 180)
    glVertex2f(270, 150)

    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()

    glTranslatef(250, 250, 0)       # Move origin to center
    glRotatef(angleZ, 0, 0, 1)      # Rotate around Z axis (clockwise)
    glTranslatef(-250, -250, 0)     # Move origin back

    draw_B()
    glutSwapBuffers()

def update(value):

    global angleZ
    angleZ -= rotSpeed

    glutPostRedisplay()
    glutTimerFunc(16, update, 0)

def init():
    glClearColor(0.06, 0.08, 0.15, 1.0)
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, 500, 0, 500, -1, 1)
    glMatrixMode(GL_MODELVIEW)

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(100, 100)
glutCreateWindow(b"Letter B - GL_LINES Rotating")

init()

glutDisplayFunc(display)
glutTimerFunc(16, update, 0)

print("Letter B rotating clockwise continuously")

glutMainLoop()