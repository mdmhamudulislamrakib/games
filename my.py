import pygame
import random
import sys

pygame.init()

# Screen
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2 Player Catch Game")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 200, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Players
p1 = pygame.Rect(50, 50, 30, 30)
p2 = pygame.Rect(500, 300, 30, 30)

speed = 5

# Enemy
enemy = pygame.Rect(random.randint(0, WIDTH-30), random.randint(0, HEIGHT-30), 30, 30)

# Scores
score1 = 0
score2 = 0

font = pygame.font.SysFont(None, 36)

# Timer
start_ticks = pygame.time.get_ticks()
game_duration = 30

clock = pygame.time.Clock()
game_over = False

while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()

    if not game_over:
        # Player 1 Movement (WASD)
        if keys[pygame.K_a]:
            p1.x -= speed
        if keys[pygame.K_d]:
            p1.x += speed
        if keys[pygame.K_w]:
            p1.y -= speed
        if keys[pygame.K_s]:
            p1.y += speed

        # Player 2 Movement (Arrow Keys)
        if keys[pygame.K_LEFT]:
            p2.x -= speed
        if keys[pygame.K_RIGHT]:
            p2.x += speed
        if keys[pygame.K_UP]:
            p2.y -= speed
        if keys[pygame.K_DOWN]:
            p2.y += speed

        # Collision
        if p1.colliderect(enemy):
            score1 += 1
            enemy.x = random.randint(0, WIDTH-30)
            enemy.y = random.randint(0, HEIGHT-30)

        if p2.colliderect(enemy):
            score2 += 1
            enemy.x = random.randint(0, WIDTH-30)
            enemy.y = random.randint(0, HEIGHT-30)

        # Timer
        seconds = (pygame.time.get_ticks() - start_ticks) / 1000
        if seconds > game_duration:
            game_over = True

    # Draw
    pygame.draw.rect(screen, BLUE, p1)
    pygame.draw.rect(screen, GREEN, p2)
    pygame.draw.rect(screen, RED, enemy)

    # Score display
    text1 = font.render(f"P1 Score: {score1}", True, BLACK)
    text2 = font.render(f"P2 Score: {score2}", True, BLACK)

    screen.blit(text1, (10, 10))
    screen.blit(text2, (400, 10))

    # Game Over
    if game_over:
        if score1 > score2:
            result = "Player 1 Wins!"
        elif score2 > score1:
            result = "Player 2 Wins!"
        else:
            result = "DRAW!"

        over_text = font.render("GAME OVER", True, BLACK)
        result_text = font.render(result, True, BLACK)

        screen.blit(over_text, (200, 150))
        screen.blit(result_text, (180, 200))

    pygame.display.update()
    clock.tick(60)