from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import math
import time

# =========================
# Window settings
# =========================
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# World coordinates
LEFT = -1.0
RIGHT = 1.0
BOTTOM = -1.0
TOP = 1.0

# =========================
# Game state
# =========================
score = 0
green_streak = 0
red_streak = 0
game_over = False
winner = False
freeze_until = 0.0

# Pac-Man properties
pacman_x = 0.0
pacman_y = 0.0
pacman_radius = 0.07
pacman_speed = 0.05

# Pac-Man direction for mouth animation
pacman_dir = "RIGHT"  # RIGHT, LEFT, UP, DOWN
mouth_open = True

# Point counts
NUM_GREEN = 5
NUM_RED = 3
greens = []
reds = []


# =========================
# Utility Functions
# =========================
def random_position(radius=0.03):
	x = random.uniform(LEFT + radius, RIGHT - radius)
	y = random.uniform(BOTTOM + radius, TOP - radius)
	return x, y


def distance(x1, y1, x2, y2):
	return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# =========================
# Drawing Functions
# =========================
def draw_text(x, y, text, font=None):
	if font is None:
		font = globals().get("GLUT_BITMAP_HELVETICA_18")
		if font is None:
			return

	glRasterPos2f(x, y)
	for ch in text:
		glutBitmapCharacter(font, ord(ch))


def draw_filled_circle(x, y, radius, sides=100):
	glBegin(GL_TRIANGLE_FAN)
	glVertex2f(x, y)  # center
	for i in range(sides + 1):
		theta = 2.0 * math.pi * i / sides
		glVertex2f(x + radius * math.cos(theta), y + radius * math.sin(theta))
	glEnd()


def draw_pacman(x, y, radius):
	global mouth_open, pacman_dir

	# Mouth angle
	mouth_angle = math.radians(35 if mouth_open else 10)

	# Direction angle
	direction_angle = 0.0
	if pacman_dir == "RIGHT":
		direction_angle = 0.0
	elif pacman_dir == "UP":
		direction_angle = math.pi / 2
	elif pacman_dir == "LEFT":
		direction_angle = math.pi
	elif pacman_dir == "DOWN":
		direction_angle = 3 * math.pi / 2

	# Yellow Pac-Man
	glColor3f(1.0, 1.0, 0.0)
	start_angle = direction_angle + mouth_angle
	end_angle = direction_angle + (2 * math.pi - mouth_angle)
	glBegin(GL_TRIANGLE_FAN)
	glVertex2f(x, y)
	sides = 100
	for i in range(sides + 1):
		theta = start_angle + (end_angle - start_angle) * i / sides
		glVertex2f(x + radius * math.cos(theta), y + radius * math.sin(theta))
	glEnd()

	# Eye
	eye_offset_x = 0.02
	eye_offset_y = 0.02
	ex, ey = x, y
	if pacman_dir == "RIGHT":
		ex = x + eye_offset_x
		ey = y + eye_offset_y
	elif pacman_dir == "LEFT":
		ex = x - eye_offset_x
		ey = y + eye_offset_y
	elif pacman_dir == "UP":
		ex = x - 0.01
		ey = y + 0.03
	elif pacman_dir == "DOWN":
		ex = x - 0.01
		ey = y - 0.01

	glColor3f(0.0, 0.0, 0.0)
	draw_filled_circle(ex, ey, 0.008, 30)


def draw_point_obj(obj):
	if obj["type"] == "green":
		glColor3f(0.0, 1.0, 0.0)
	else:
		glColor3f(1.0, 0.0, 0.0)

	glPointSize(10)
	glBegin(GL_POINTS)
	glVertex2f(obj["x"], obj["y"])
	glEnd()


def draw_border():
	if time.time() < freeze_until:
		glColor3f(1.0, 0.0, 0.0)  # red border during freeze penalty
	else:
		glColor3f(1.0, 1.0, 1.0)

	glLineWidth(2)
	glBegin(GL_LINE_LOOP)
	glVertex2f(LEFT, BOTTOM)
	glVertex2f(RIGHT, BOTTOM)
	glVertex2f(RIGHT, TOP)
	glVertex2f(LEFT, TOP)
	glEnd()


# =========================
# Game Logic
# =========================
def create_points():
	global greens, reds
	greens = []
	reds = []

	for _ in range(NUM_GREEN):
		x, y = random_position()
		vx = random.choice([-1, 1]) * random.uniform(0.002, 0.006)
		vy = random.choice([-1, 1]) * random.uniform(0.002, 0.006)
		greens.append({
			"x": x,
			"y": y,
			"vx": vx,
			"vy": vy,
			"type": "green",
		})

	for _ in range(NUM_RED):
		x, y = random_position()
		vx = random.choice([-1, 1]) * random.uniform(0.003, 0.007)
		vy = random.choice([-1, 1]) * random.uniform(0.003, 0.007)
		reds.append({
			"x": x,
			"y": y,
			"vx": vx,
			"vy": vy,
			"type": "red",
		})


def respawn_point(obj):
	x, y = random_position()
	obj["x"] = x
	obj["y"] = y
	obj["vx"] = random.choice([-1, 1]) * random.uniform(0.002, 0.007)
	obj["vy"] = random.choice([-1, 1]) * random.uniform(0.002, 0.007)


def update_points(points):
	for obj in points:
		obj["x"] += obj["vx"]
		obj["y"] += obj["vy"]

		# Bounce from borders
		if obj["x"] <= LEFT or obj["x"] >= RIGHT:
			obj["vx"] *= -1
		if obj["y"] <= BOTTOM or obj["y"] >= TOP:
			obj["vy"] *= -1

		# Clamp
		obj["x"] = max(LEFT + 0.01, min(RIGHT - 0.01, obj["x"]))
		obj["y"] = max(BOTTOM + 0.01, min(TOP - 0.01, obj["y"]))


def check_collisions():
	global score, green_streak, red_streak, freeze_until, game_over, winner

	if game_over:
		return

	# Green collisions
	for g in greens:
		if distance(pacman_x, pacman_y, g["x"], g["y"]) <= pacman_radius + 0.02:
			score += 10
			green_streak += 1
			red_streak = 0

			# Combo bonus
			if green_streak == 3:
				score += 20
				green_streak = 0
				print("COMBO BONUS! +20")

			respawn_point(g)

	# Red collisions
	for r in reds:
		if distance(pacman_x, pacman_y, r["x"], r["y"]) <= pacman_radius + 0.02:
			score -= 10
			red_streak += 1
			green_streak = 0

			# Freeze penalty
			if red_streak == 2:
				freeze_until = time.time() + 1.0  # freeze for 1 second
				red_streak = 0
				print("FREEZE PENALTY! 1 second")

			respawn_point(r)

	# Required end condition: game stops once score reaches 100.
	if score >= 100:
		winner = True
		game_over = True


# =========================
# GLUT Callbacks
# =========================
def display():
	glClear(GL_COLOR_BUFFER_BIT)

	# Border
	draw_border()

	# Draw points
	for g in greens:
		draw_point_obj(g)
	for r in reds:
		draw_point_obj(r)

	# Draw Pac-Man
	draw_pacman(pacman_x, pacman_y, pacman_radius)

	# UI Text
	glColor3f(1.0, 1.0, 1.0)
	draw_text(-0.95, 0.92, f"Score: {score}")
	draw_text(-0.95, 0.84, f"Green Combo: {green_streak}/3")
	draw_text(-0.95, 0.76, f"Red Trap: {red_streak}/2")

	if time.time() < freeze_until and not game_over:
		glColor3f(1.0, 0.3, 0.3)
		draw_text(-0.15, 0.92, "FROZEN!")

	if winner:
		glColor3f(0.0, 1.0, 0.0)
		draw_text(-0.24, 0.02, "GAME OVER")
		draw_text(-0.30, -0.08, "You reached 100!")
		draw_text(-0.35, -0.18, "Press R to Restart")

	glutSwapBuffers()


def update(value):
	global mouth_open

	if not game_over:
		update_points(greens)
		update_points(reds)
		check_collisions()

	# Mouth animation toggle
	mouth_open = not mouth_open
	glutPostRedisplay()
	glutTimerFunc(100, update, 0)  # ~10 FPS logic timer


def special_keys(key, x, y):
	global pacman_x, pacman_y, pacman_dir

	if game_over:
		return

	# Freeze check
	if time.time() < freeze_until:
		return

	if key == GLUT_KEY_LEFT:
		pacman_x -= pacman_speed
		pacman_dir = "LEFT"
	elif key == GLUT_KEY_RIGHT:
		pacman_x += pacman_speed
		pacman_dir = "RIGHT"
	elif key == GLUT_KEY_UP:
		pacman_y += pacman_speed
		pacman_dir = "UP"
	elif key == GLUT_KEY_DOWN:
		pacman_y -= pacman_speed
		pacman_dir = "DOWN"

	# Keep Pac-Man inside boundary
	pacman_x = max(LEFT + pacman_radius, min(RIGHT - pacman_radius, pacman_x))
	pacman_y = max(BOTTOM + pacman_radius, min(TOP - pacman_radius, pacman_y))

	glutPostRedisplay()


def keyboard(key, x, y):
	global game_over, winner, score, green_streak, red_streak
	global pacman_x, pacman_y, freeze_until

	key = key.decode("utf-8").lower()
	if key == "r":
		# Restart game
		score = 0
		green_streak = 0
		red_streak = 0
		game_over = False
		winner = False
		freeze_until = 0.0
		pacman_x = 0.0
		pacman_y = 0.0
		create_points()
		glutPostRedisplay()
	elif key == "q" or key == chr(27):  # q or ESC
		glutLeaveMainLoop()


# =========================
# OpenGL Init
# =========================
def init():
	glClearColor(0.0, 0.0, 0.0, 1.0)  # black background
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	gluOrtho2D(LEFT, RIGHT, BOTTOM, TOP)
	glMatrixMode(GL_MODELVIEW)


# =========================
# Main
# =========================
def main():
	global pacman_x, pacman_y

	pacman_x = 0.0
	pacman_y = 0.0
	create_points()

	glutInit()
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
	glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
	glutInitWindowPosition(100, 100)
	glutCreateWindow(b"PAC-MAN Point Hunt (PyOpenGL)")
	init()
	glutDisplayFunc(display)
	glutSpecialFunc(special_keys)
	glutKeyboardFunc(keyboard)
	glutTimerFunc(100, update, 0)
	glutMainLoop()


if __name__ == "__main__":
	main()