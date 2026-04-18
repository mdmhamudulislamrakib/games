from OpenGL.GL import *
from OpenGL.GLUT import * 
import random 
 
def iterate(): 
    glViewport(0, 0, 500, 500) 
    glMatrixMode(GL_PROJECTION) 
    glLoadIdentity() 
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0) 
    glMatrixMode(GL_MODELVIEW) 
    glLoadIdentity() 
 
def main_draw_random_pixels(): 
    glColor3f(1.0, 1.0, 1.0) 
    glPointSize(5) 
    glBegin(GL_POINTS) 
     
    for i in range(50): 
        x = random.randint(0, 300) 
        y = random.randint(0, 300) 
        glVertex2f(x, y) 
    glEnd() 
 
def showScreen(): 
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) 
    glLoadIdentity() 
    iterate() 
    main_draw_random_pixels() 
    glutSwapBuffers() 
 
glutInit() 
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH) 
glutInitWindowSize(500, 500) 
glutInitWindowPosition(0, 0) 
wind = glutCreateWindow(b"Drawing Pixels") 
glutDisplayFunc(showScreen) 
glutMainLoop() 