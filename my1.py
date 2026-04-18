
import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# ====================== CONSTANTS ======================
XMAX = 1200
YMAX = 700
SPACESHIP_SPEED = 20

# ====================== GLOBAL VARIABLES ======================
mouseX = 0.0
mouseY = 0.0
mButtonPressed = False

class View:
    INTRO = 0
    MENU = 1
    INSTRUCTIONS = 2
    GAME = 3
    GAMEOVER = 4

viewPage = View.INTRO

keyStates = [False] * 256
laser1Dir = [False, False]
laser2Dir = [False, False]

alienLife1 = 100
alienLife2 = 100

xOne = 500.0
yOne = 0.0
xTwo = 500.0
yTwo = 0.0

laser1 = False
laser2 = False

CI = 0

LightColor = [[1,1,0], [0,1,1], [0,1,0]]

AlienBody = [[-4,9], [-6,0], [0,0], [0.5,9], [0.15,12], [-14,18], [-19,10], [-20,0], [-6,0]]
AlienCollar = [[-9,10.5], [-6,11], [-5,12], [6,18], [10,20], [13,23], [16,30], [19,39], [16,38],
               [10,37], [-13,39], [-18,41], [-20,43], [-20.5,42], [-21,30], [-19.5,23], [-19,20],
               [-14,16], [-15,17], [-13,13], [-9,10.5]]
ALienFace = [[-6,11], [-4.5,18], [0.5,20], [0.,20.5], [0.1,19.5], [1.8,19], [5,20], [7,23], [9,29],
             [6,29.5], [5,28], [7,30], [10,38],[11,38], [11,40], [11.5,48], [10,50.5],[8.5,51], [6,52],
             [1,51], [-3,50],[-1,51], [-3,52], [-5,52.5], [-6,52], [-9,51], [-10.5,50], [-12,49], [-12.5,47],
             [-12,43], [-13,40], [-12,38.5], [-13.5,33],[-15,38],[-14.5,32], [-14,28], [-13.5,33], [-14,28],
             [-13.8,24], [-13,20], [-11,19], [-10.5,12], [-6,11]]
ALienBeak = [[-6,21.5], [-6.5,22], [-9,21], [-11,20.5], [-20,20], [-14,23], [-9.5,28], [-7,27], [-6,26.5],
             [-4.5,23], [-4,21], [-6,19.5], [-8.5,19], [-10,19.5], [-11,20.5]]

# ====================== HELPER ======================
def displayRasterText(x, y, z, text):
    glRasterPos3f(x, y, z)
    for char in text:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(char))

def init():
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1200, 1200, -700, 700)#set cordinates for 2D drawing
    glMatrixMode(GL_MODELVIEW)

# ====================== SCREENS ======================
def introScreen():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0.0, 0.0, 1.0)
    displayRasterText(-425, 490, 0.0, " Daffodil International University ")
    glColor3f(1.0, 1.0, 1.0)
    displayRasterText(-600, 385, 0.0, " Department of computer science and engineering")
    glColor3f(0.0, 0.0, 1.0)
    displayRasterText(-250, 300, 0.0, "A MINI PROJECT ON ")
    glColor3f(1.0, 0.0, 1.0)
    displayRasterText(-225, 225, 0.0, " Space Shooter ")
    glColor3f(1.0, 0.7, 0.8)
    displayRasterText(-150, 150, 0.0, "Created by")
    glColor3f(1.0, 1.0, 1.0)
    displayRasterText(-100, 80, 0.0, " RAKIB ")
    glColor3f(1.0, 0.0, 0.0)
    displayRasterText(-800, -100, 0.0, " STUDENT NAMES & ID")
    glColor3f(1.0, 1.0, 1.0)
    displayRasterText(-800, -200, 0.0, " Name: Md.Mhamudul Islam Rakib")
    displayRasterText(-800, -285, 0.0, " ID:222-15-6437")
    glColor3f(1.0, 0.0, 0.0)
    displayRasterText(500, -100, 0.0, " SUBMITTED TO ")
    glColor3f(1.0, 1.0, 1.0)
    displayRasterText(500, -200, 0.0, " Lecturer  Md. Alvee Ehsan ")
    glColor3f(1.0, 0.0, 0.0)
    displayRasterText(-250, -400, 0.0, " Academic Year SPRING 2026 ")
    glColor3f(1.0, 1.0, 1.0)
    displayRasterText(-300, -550, 0.0, " Press ENTER to start the game ")

def startScreenDisplay():
    global alienLife1, alienLife2, viewPage, mButtonPressed
    glLineWidth(10)
    glColor3f(1, 0, 0)
    glBegin(GL_LINE_LOOP)
    glVertex2f(-750, -500); glVertex2f(-750, 550)
    glVertex2f(750, 550); glVertex2f(750, -500)
    glEnd()
    glLineWidth(1)

    glColor3f(1, 1, 0)
    # Start Game
    glBegin(GL_POLYGON)
    glVertex2f(-200, 300); glVertex2f(-200, 400)
    glVertex2f(200, 400); glVertex2f(200, 300)
    glEnd()
    # Instructions
    glBegin(GL_POLYGON)
    glVertex2f(-200, 50); glVertex2f(-200, 150)
    glVertex2f(200, 150); glVertex2f(200, 50)
    glEnd()
    # Quit
    glBegin(GL_POLYGON)
    glVertex2f(-200, -200); glVertex2f(-200, -100)
    glVertex2f(200, -100); glVertex2f(200, -200)
    glEnd()

    # Button logic
    if -100 <= mouseX <= 100 and 150 <= mouseY <= 200:
        glColor3f(0, 0, 1)
        if mButtonPressed:
            alienLife1 = alienLife2 = 100
            viewPage = View.GAME
            mButtonPressed = False
    else:
        glColor3f(0, 0, 0)
    displayRasterText(-100, 340, 0.4, "Start Game")

    if -100 <= mouseX <= 100 and 30 <= mouseY <= 80:
        glColor3f(0, 0, 1)
        if mButtonPressed:
            viewPage = View.INSTRUCTIONS
            mButtonPressed = False
    else:
        glColor3f(0, 0, 0)
    displayRasterText(-120, 80, 0.4, "Instructions")

    if -100 <= mouseX <= 100 and -90 <= mouseY <= -40:
        glColor3f(0, 0, 1)
        if mButtonPressed:
            mButtonPressed = False
            sys.exit(0)
    else:
        glColor3f(0, 0, 0)
    displayRasterText(-100, -170, 0.4, "Quit")

def backButton():
    global mButtonPressed, viewPage
    if -500 <= mouseX <= -450 and -275 <= mouseY <= -250:
        glColor3f(0, 0, 1)
        if mButtonPressed:
            viewPage = View.MENU
            mButtonPressed = False
    else:
        glColor3f(1, 0, 0)
    displayRasterText(-1000, -550, 0, "Back")

def instructionsScreenDisplay():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glColor3f(1, 0, 0)
    displayRasterText(-900, 550, 0.4, "INSTRUCTIONS")
    glColor3f(1, 0, 0)
    displayRasterText(-1000, 400, 0.4, "PLAYER 1")
    displayRasterText(200, 400, 0.4, "PLAYER 2")
    glColor3f(1, 1, 1)
    displayRasterText(-1100, 300, 0.4, "Key 'w' to move up.")
    displayRasterText(-1100, 200, 0.4, "Key 's' to move down.")
    displayRasterText(-1100, 100, 0.4, "Key 'd' to move right.")
    displayRasterText(-1100, 0,   0.4, "Key 'a' to move left.")
    displayRasterText(100, 300, 0.4, "Key 'i' to move up.")
    displayRasterText(100, 200, 0.4, "Key 'k' to move down.")
    displayRasterText(100, 100, 0.4, "Key 'j' to move right.")
    displayRasterText(100, 0,   0.4, "Key 'l' to move left.")
    displayRasterText(-1100, -100, 0.4, "Key 'c' to shoot, Use 'w' and 's' to change direction.")
    displayRasterText(100, -100, 0.4, "Key 'm' to shoot, Use 'i' and 'k' to change direction.")
    displayRasterText(-1100, -300, 0.4, "The Objective is to kill your opponent.")
    displayRasterText(-1100, -370, 0.4, "Each time a player gets shot, LIFE decreases by 5 points.")
    backButton()

# ====================== DRAWING FUNCTIONS ======================
def DrawAlienBody(isPlayer1):
    glColor3f(0,1,0) if isPlayer1 else glColor3f(1,1,0)
    glBegin(GL_POLYGON)
    for v in AlienBody: glVertex2fv(v)
    glEnd()
    glColor3f(0,0,0)
    glBegin(GL_LINE_STRIP)
    for v in AlienBody: glVertex2fv(v)
    glEnd()

def DrawAlienCollar():
    glColor3f(1,0,0)
    glBegin(GL_POLYGON)
    for v in AlienCollar: glVertex2fv(v)
    glEnd()
    glColor3f(0,0,0)
    glBegin(GL_LINE_STRIP)
    for v in AlienCollar: glVertex2fv(v)
    glEnd()

def DrawAlienFace(isPlayer1):
    glColor3f(0,0,1)
    glBegin(GL_POLYGON)
    for v in ALienFace: glVertex2fv(v)
    glEnd()
    glColor3f(0,0,0)
    glBegin(GL_LINE_STRIP)
    for v in ALienFace: glVertex2fv(v)
    glEnd()

def DrawAlienBeak():
    glColor3f(1,1,0)
    glBegin(GL_POLYGON)
    for v in ALienBeak: glVertex2fv(v)
    glEnd()
    glColor3f(0,0,0)
    glBegin(GL_LINE_STRIP)
    for v in ALienBeak: glVertex2fv(v)
    glEnd()

def DrawAlienEyes(isPlayer1):
    glColor3f(0,1,1)
    glPushMatrix()
    glRotated(-10, 0, 0, 1)
    glTranslated(-6, 32.5, 0)
    glScalef(2.5, 4, 0)
    glutSolidSphere(1, 20, 30)
    glPopMatrix()
    glPushMatrix()
    glRotated(-1, 0, 0, 1)
    glTranslated(-8, 36, 0)
    glScalef(2.5, 4, 0)
    glutSolidSphere(1, 100, 100)
    glPopMatrix()

def DrawAlien(isPlayer1):
    DrawAlienBody(isPlayer1)
    DrawAlienCollar()
    DrawAlienFace(isPlayer1)
    DrawAlienBeak()
    DrawAlienEyes(isPlayer1)

def DrawSpaceshipBody(isPlayer1):
    glColor3f(1,0,0) if isPlayer1 else glColor3f(0.5,0,0.5)
    glPushMatrix()
    glScalef(70, 20, 1)
    glutSolidSphere(1, 50, 50)
    glPopMatrix()

    glPushMatrix()
    glScalef(3, 3, 1)
    glTranslated(-20, 0, 0)
    for i in range(9):
        glColor3fv(LightColor[(CI + i) % 3])
        glutSolidSphere(1, 1000, 1000)
        glTranslated(5, 0, 0)
    glPopMatrix()

def DrawSteeringWheel():
    glPushMatrix()
    glLineWidth(3)
    glColor3f(0.2, 0, 0.2)
    glScalef(7, 4, 1)
    glTranslated(-1.9, 5.5, 0)
    glutWireSphere(1, 8, 8)
    glPopMatrix()

def DrawSpaceshipDoom():
    glColor4f(0.7, 1, 1, 0.0011)
    glPushMatrix()
    glTranslated(0, 30, 0)
    glScalef(35, 50, 1)
    glutSolidSphere(1, 50, 50)
    glPopMatrix()

def DrawLaser(x, y, dir_list):
    xend = -XMAX
    yend = YMAX if dir_list[0] else (-YMAX if dir_list[1] else y)
    glLineWidth(5)
    glColor3f(1, 0, 0)
    glBegin(GL_LINES)
    glVertex2f(x, y)
    glVertex2f(xend, yend)
    glEnd()

def SpaceshipCreate(x, y, isPlayer1):
    glPushMatrix()
    glTranslated(x, y, 0)
    DrawSpaceshipDoom()
    glPushMatrix()
    glTranslated(4, 19, 0)
    DrawAlien(isPlayer1)
    glPopMatrix()
    DrawSteeringWheel()
    DrawSpaceshipBody(isPlayer1)
    glPopMatrix()

def DisplayHealthBar1():
    glColor3f(1,1,1)
    displayRasterText(-1100, 600, 0.4, f"LIFE = {alienLife1}")

def DisplayHealthBar2():
    glColor3f(1,1,1)
    displayRasterText(800, 600, 0.4, f"LIFE = {alienLife2}")

def checkLaserContact(x, y, dir_list, xp, yp, player1):
    global alienLife1, alienLife2
    xend = -XMAX
    yend = YMAX if dir_list[0] else (-YMAX if dir_list[1] else y)
    xp += 8
    yp += 8
    m = (yend - y) / (xend - x) if xend != x else 0
    k = y - m * x
    r = 50
    b = 2 * xp - 2 * m * (k - yp)
    a = 1 + m * m
    c = xp*xp + (k - yp)**2 - r*r
    d = b*b - 4*a*c
    if d >= 0:
        if player1:
            alienLife1 = max(0, alienLife1 - 5)
        else:
            alienLife2 = max(0, alienLife2 - 5)

def gameScreenDisplay():
    global viewPage, xOne, yOne, xTwo, yTwo
    DisplayHealthBar1()
    DisplayHealthBar2()
    glScalef(2, 2, 0)

    if alienLife1 > 0:
        SpaceshipCreate(xOne, yOne, True)
        if laser1:
            DrawLaser(xOne, yOne, laser1Dir)
            checkLaserContact(xOne, yOne, laser1Dir, -xTwo, yTwo, True)
    else:
        viewPage = View.GAMEOVER

    if alienLife2 > 0:
        glPushMatrix()
        glScalef(-1, 1, 1)
        SpaceshipCreate(xTwo, yTwo, False)
        if laser2:
            DrawLaser(xTwo, yTwo, laser2Dir)
            checkLaserContact(xTwo, yTwo, laser2Dir, -xOne, yOne, False)
        glPopMatrix()
    else:
        viewPage = View.GAMEOVER

    if viewPage == View.GAMEOVER:
        xOne = xTwo = 500
        yOne = yTwo = 0

def displayGameOverMessage():
    glColor3f(1, 1, 0)
    msg = "Game Over! Player 1 won the game" if alienLife1 > 0 else "Game Over! Player 2 won the game"
    displayRasterText(-350, 600, 0.4, msg)

# ====================== INPUT ======================
def keyOperations():
    global viewPage, laser1, laser2, xOne, yOne, xTwo, yTwo
    if keyStates[13] and viewPage == View.INTRO:        # ENTER
        viewPage = View.MENU

    if viewPage == View.GAME:
        laser1Dir[0] = laser1Dir[1] = laser2Dir[0] = laser2Dir[1] = False

        # Player 2
        if keyStates[ord('c')]:
            laser2 = True
            if keyStates[ord('w')]: laser2Dir[0] = True
            if keyStates[ord('s')]: laser2Dir[1] = True
        else:
            laser2 = False
            if keyStates[ord('d')]: xTwo -= SPACESHIP_SPEED
            if keyStates[ord('a')]: xTwo += SPACESHIP_SPEED
            if keyStates[ord('w')]: yTwo += SPACESHIP_SPEED
            if keyStates[ord('s')]: yTwo -= SPACESHIP_SPEED

        # Player 1
        if keyStates[ord('m')]:
            laser1 = True
            if keyStates[ord('i')]: laser1Dir[0] = True
            if keyStates[ord('k')]: laser1Dir[1] = True
        else:
            laser1 = False
            if keyStates[ord('l')]: xOne += SPACESHIP_SPEED
            if keyStates[ord('j')]: xOne -= SPACESHIP_SPEED
            if keyStates[ord('i')]: yOne += SPACESHIP_SPEED
            if keyStates[ord('k')]: yOne -= SPACESHIP_SPEED

def display():
    keyOperations()
    glClear(GL_COLOR_BUFFER_BIT)

    if viewPage == View.INTRO:
        introScreen()
    elif viewPage == View.MENU:
        startScreenDisplay()
    elif viewPage == View.INSTRUCTIONS:
        instructionsScreenDisplay()
    elif viewPage == View.GAME:
        gameScreenDisplay()
        glScalef(0.5, 0.5, 0)
    elif viewPage == View.GAMEOVER:
        displayGameOverMessage()
        startScreenDisplay()

    glFlush()
    glLoadIdentity()
    glutSwapBuffers()

def passiveMotionFunc(x, y):
    global mouseX, mouseY
    mouseX = x / (1200 / 1200.0) - 600.0
    mouseY = -(y / (600 / 700.0) - 350.0)
    glutPostRedisplay()

def mouseClick(button, state, x, y):
    global mButtonPressed
    mButtonPressed = (button == GLUT_LEFT_BUTTON and state == GLUT_DOWN)
    glutPostRedisplay()

def keyPressed(key, x, y):
    global keyStates
    if isinstance(key, bytes):
        key = key[0]
    keyStates[key] = True
    glutPostRedisplay()

def keyReleased(key, x, y):
    global keyStates
    if isinstance(key, bytes):
        key = key[0]
    keyStates[key] = False

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowPosition(0, 0)
    glutInitWindowSize(1200, 600)
    glutCreateWindow(b"Space Shooter - OpenGL in Python")
    init()
    glutKeyboardFunc(keyPressed)
    glutKeyboardUpFunc(keyReleased)
    glutMouseFunc(mouseClick)
    glutPassiveMotionFunc(passiveMotionFunc)
    glutDisplayFunc(display)
    glutIdleFunc(glutPostRedisplay)
    glutMainLoop()

if __name__ == "__main__":
    main()