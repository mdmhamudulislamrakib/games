from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def drawLine(xa, ya, xb, yb):
dx = xb - xa
dy = yb - ya
m = dy / dx if dx != 0 else None
points = []
if abs(dx) >= abs(dy):
if xa > xb:
xa, xb = xb, xa
ya, yb = yb, ya
x, y = xa, ya

while x <= xb:
points.append((round(x), round(y)))
x += 1
if m is not None:
y += m

else:
if ya > yb:
xa, xb = xb, xa
ya, yb = yb, ya
x, y = xa, ya
inv = 1 / m if (m is not None and m != 0) else 0
while y <= yb:
points.append((round(x), round(y)))
y += 1
if m is not None:
x += inv
glBegin(GL_POINTS)
for px, py in points:
glVertex2f(px, py)
glEnd()

def drawPoint(x, y):
glBegin(GL_POINTS)
glVertex2f(x, y)
glEnd()

def drawText(x, y, text):
glRasterPos2f(x + 5, y + 5)
for ch in text:
glutBitmapCharacter(GLUT_BITMAP_HELVETICA_10, ord(ch))
def display():
glClear(GL_COLOR_BUFFER_BIT)
glColor3f(0.0, 1.0, 1.0)
drawLine(50, 50, 130, 50)
drawLine(130, 50, 130, 130)
drawLine(130, 130, 50, 130)
drawLine(50, 130, 50, 50)
drawLine(30, 70, 110, 70)
drawLine(110, 70, 110, 150)
drawLine(110, 150, 30, 150)
drawLine(30, 150, 30, 70)

drawLine(50, 50, 30, 70)
drawLine(130, 50, 110, 70)
drawLine(130, 130, 110, 150)
drawLine(50, 130, 30, 150)
points = [
(50, 50), (130, 50), (130, 130), (50, 130),
(30, 70), (110, 70), (110, 150), (30, 150)
]
glColor3f(1.0, 0.0, 0.0)
glPointSize(6)
for x, y in points:
drawPoint(x, y)
glColor3f(0.0, 1.0, 1.0)
for x, y in points:
drawText(x, y, f"({x},{y})")
glFlush()

glutInit()
glutInitWindowSize(500, 500)
glutCreateWindow(b"Cube using DDA Algorithm ")
gluOrtho2D(0, 500, 0, 500)
glutDisplayFunc(display)
glutMainLoop()