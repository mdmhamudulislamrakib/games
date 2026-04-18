from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Quad 1 starts at bottom-left (0,0), moves toward top-right
# Quad 2 starts at top-right (450,450), moves toward bottom-left
pos1X, pos1Y = 0.0,   0.0
pos2X, pos2Y = 450.0, 450.0

speed = 3.0
dirX, dirY = 1.0, 1.0      # Quad 1 direction: right+up
SIZE = 50                   # Quad size
angle = 0.0
rot_speed = 2.0             # degrees per frame (clockwise)

def draw_quads():
    # Quad 1 with clockwise rotation around its own center.
    glPushMatrix()
    glTranslatef(pos1X + SIZE / 2, pos1Y + SIZE / 2, 0)
    glRotatef(angle, 0, 0, 1)
    glTranslatef(-(SIZE / 2), -(SIZE / 2), 0)
    glColor3f(0.2, 0.9, 0.5)
    glBegin(GL_QUADS)
    glVertex2f(0, 0)
    glVertex2f(SIZE, 0)
    glVertex2f(SIZE, SIZE)
    glVertex2f(0, SIZE)
    glEnd()
    glPopMatrix()

    # Quad 2 with clockwise rotation around its own center.
    glPushMatrix()
    glTranslatef(pos2X + SIZE / 2, pos2Y + SIZE / 2, 0)
    glRotatef(angle, 0, 0, 1)
    glTranslatef(-(SIZE / 2), -(SIZE / 2), 0)
    glColor3f(1.0, 0.6, 0.1)
    glBegin(GL_QUADS)
    glVertex2f(0, 0)
    glVertex2f(SIZE, 0)
    glVertex2f(SIZE, SIZE)
    glVertex2f(0, SIZE)
    glEnd()
    glPopMatrix()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    draw_quads()
    glutSwapBuffers()

def update(value):
    global pos1X, pos1Y, pos2X, pos2Y, dirX, dirY, angle

    # Move quad 1 diagonally right+up
    pos1X += speed * dirX
    pos1Y += speed * dirY


    # Move quad 2 in the exact opposite direction
    pos2X -= speed * dirX
    pos2Y -= speed * dirY


    # Bounce quad 1 off walls — quad 2 mirrors it automatically
    if pos1X <= 0 or pos1X + SIZE >= 500:
        dirX *= -1
    if pos1Y <= 0 or pos1Y + SIZE >= 500:
        dirY *= -1

    # Bonus: both quads rotate clockwise continuously.
    angle -= rot_speed

    glutPostRedisplay()
    glutTimerFunc(16, update, 0)
    
def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, 500, 0, 500, -1, 1)
    glMatrixMode(GL_MODELVIEW)

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(500, 500)
glutInitWindowPosition(100, 100)
glutCreateWindow(b"Diagonal Quads")

init()

glutDisplayFunc(display)
glutTimerFunc(16, update, 0)

print("Two quads moving diagonally from opposite corners")

glutMainLoop()