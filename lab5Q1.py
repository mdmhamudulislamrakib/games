from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

legAngle = 25.0
walkToggle = True


def draw_horse(baseX, leftLeg, rightLeg):
	# Body
	glColor3f(1.0, 0.9, 0.0)
	glBegin(GL_QUADS)
	glVertex2f(baseX + 65, 200)
	glVertex2f(baseX + 235, 200)
	glVertex2f(baseX + 235, 300)
	glVertex2f(baseX + 65, 300)
	glEnd()

	# Left leg
	glPushMatrix()
	glTranslatef(baseX + 110, 200, 0)
	glRotatef(leftLeg, 0, 0, 1)
	glColor3f(0.4, 0.7, 1.0)
	glBegin(GL_QUADS)
	glVertex2f(-15, 0)
	glVertex2f(15, 0)
	glVertex2f(15, -100)
	glVertex2f(-15, -100)
	glEnd()
	glPopMatrix()

	# Right leg
	glPushMatrix()
	glTranslatef(baseX + 190, 200, 0)
	glRotatef(rightLeg, 0, 0, 1)
	glColor3f(1.0, 0.3, 0.3)
	glBegin(GL_QUADS)
	glVertex2f(-15, 0)
	glVertex2f(15, 0)
	glVertex2f(15, -100)
	glVertex2f(-15, -100)
	glEnd()
	glPopMatrix()


def display():
	glClear(GL_COLOR_BUFFER_BIT)
	glLoadIdentity()

	# alternating leg angles for walking pose
	if walkToggle:
		leftLeg = legAngle
		rightLeg = -legAngle
	else:
		leftLeg = -legAngle
		rightLeg = legAngle

	# First output (left horse)
	draw_horse(0, leftLeg, rightLeg)

	# Second output (right horse) with opposite pose
	draw_horse(250, -leftLeg, -rightLeg)

	glutSwapBuffers()


def keyboard(key, x, y):
	global walkToggle

	# Press H to flip leg pose for both outputs.
	if key in (b'h', b'H'):
		walkToggle = not walkToggle

	glutPostRedisplay()


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
glutCreateWindow(b"Horse Move X Axis")
init()
glutDisplayFunc(display)
glutKeyboardFunc(keyboard)
glutMainLoop()