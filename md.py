 
from OpenGL.GL import * 
from OpenGL.GLUT import * 
 
def iterate(): 
    glViewport(0, 0, 1000, 1000) 
    glMatrixMode(GL_PROJECTION) 
    glLoadIdentity() 
    glOrtho(0.0, 1000, 0.0, 1000, 0.0, 1.0) 
    glMatrixMode(GL_MODELVIEW) 
    glLoadIdentity() 
 
# ...existing code... 
def showScreen(): 
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 
    glLoadIdentity() 
    iterate() 
    glColor3f(1.0, 1.0, 1.0) 
    glBegin(GL_LINES) 
 
    # M 
    glVertex2f(400, 480); glVertex2f(400, 520) 
    glVertex2f(400, 520); glVertex2f(420, 500) 
    glVertex2f(420, 500); glVertex2f(440, 520) 
    glVertex2f(440, 520); glVertex2f(440, 480) 
 
    # D 
    glVertex2f(460, 480); glVertex2f(460, 520) 
    glVertex2f(460, 520); glVertex2f(480, 520) 
    glVertex2f(480, 520); glVertex2f(490, 510) 
    glVertex2f(490, 510); glVertex2f(490, 490) 
    glVertex2f(490, 490); glVertex2f(480, 480) 
    glVertex2f(480, 480); glVertex2f(460, 480) 
 
 
    # 7 
    glVertex2f(622, 520); glVertex2f(650, 520) 
    glVertex2f(650, 520); glVertex2f(630, 480) 
 
    glEnd() 
    glutSwapBuffers() 
 
 
glutInit() 
glutInitDisplayMode(GLUT_RGBA) 
glutInitWindowSize(1000, 1000)
glutInitWindowPosition(0, 0) 
wind = glutCreateWindow(b"Drawing Pixels") 
glutDisplayFunc(showScreen) 
 
glutMainLoop() 