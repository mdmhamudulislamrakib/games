from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

# Window size
WIDTH = 500
HEIGHT = 500

# Rain storage
raindrops = []

# Create initial raindrops
for i in range(100):
	x = random.randint(0, WIDTH)
	y = random.randint(0, HEIGHT)
	raindrops.append([x, y])


def draw_rain():
	glColor3f(0.4, 0.7, 1.0)
	for drop in raindrops:
		x, y = drop

		# Slanted raindrop using GL_QUADS (not vertical 90-degree fall).
		glBegin(GL_QUADS)
		glVertex2f(x, y)
		glVertex2f(x + 4, y)
		glVertex2f(x + 1, y - 15)
		glVertex2f(x - 3, y - 15)
		glEnd()


def update(value):
	for drop in raindrops:
		# Move downward and slightly left for slanted rain.
		drop[0] -= 2
		drop[1] -= 8

		# Reset when raindrop goes out of screen.
		if drop[1] < 0 or drop[0] < 0:
			drop[0] = random.randint(50, WIDTH)
			drop[1] = random.randint(HEIGHT, HEIGHT + 100)

	glutPostRedisplay()
	glutTimerFunc(30, update, 0)


def display():
	glClear(GL_COLOR_BUFFER_BIT)
	glLoadIdentity()
	draw_rain()
	glutSwapBuffers()


def init():
	glClearColor(0.0, 0.0, 0.0, 1.0)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	glOrtho(0, WIDTH, 0, HEIGHT, -1, 1)
	glMatrixMode(GL_MODELVIEW)


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
glutInitWindowSize(WIDTH, HEIGHT)
glutInitWindowPosition(100, 100)
glutCreateWindow(b"Virtual Rain Animation")
init()
glutDisplayFunc(display)
glutTimerFunc(30, update, 0)
glutMainLoop()