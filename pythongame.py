import pygame
import random
import sys

pygame.init()

# Screen
WIDTH, HEIGHT = 400, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Car Game")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()

# Player car
player_width = 50
player_height = 90
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 10
player_speed = 6

# Enemy car
enemy_width = 50
enemy_height = 90
enemy_x = random.randint(0, WIDTH - enemy_width)
enemy_y = -enemy_height
enemy_speed = 5

# Score
score = 0
font = pygame.font.SysFont(None, 36)

def show_score():
    text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(text, (10, 10))

def game_over():
    text = font.render("GAME OVER", True, RED)
    screen.blit(text, (120, 250))
    pygame.display.update()
    pygame.time.delay(2000)
    pygame.quit()
    sys.exit()

# Game loop
while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    enemy_y += enemy_speed
    if enemy_y > HEIGHT:
        enemy_y = -enemy_height
        enemy_x = random.randint(0, WIDTH - enemy_width)
        enemy_speed += 0.3
        score += 1

    # Collision
    if (player_x < enemy_x + enemy_width and
        player_x + player_width > enemy_x and
        player_y < enemy_y + enemy_height and
        player_y + player_height > enemy_y):
        game_over()

    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_width, player_height))
    pygame.draw.rect(screen, RED, (enemy_x, enemy_y, enemy_width, enemy_height))

    show_score()

    pygame.display.update()
    clock.tick(60)
