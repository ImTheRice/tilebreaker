
import pygame 
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Tile breaker')
clock = pygame.time.Clock()

background = pygame.image.load("background.jpg").convert()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create the player paddle object
player_paddle = pygame.Rect(350, 550, 100, 10)

# Create the ball
ball = pygame.Rect(345, 490, 10, 10)

# Set the initial speed of the ball
x_speed = 3
y_speed = 3

#Create tiles
tile_width = 40
tile_height = 20
tile_color = WHITE

#Draw tiles
tiles = []
for i in range(8):
    for j in range(7):
        tiles.append(pygame.Rect(i*tile_width, j*tile_height, tile_width, tile_height))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    # Move the paddles according to keys pressed
    key = pygame.key.get_pressed()
    if key[K_LEFT]:
        player_paddle.left -= 5
    if key[K_RIGHT]:
        player_paddle.right += 5

    # Make sure the paddle stays within the screen
    if player_paddle.left < 0:
        player_paddle.left = 0
    if player_paddle.right > 800:
        player_paddle.right = 800

    # Move the ball
    ball.left += x_speed
    ball.top += y_speed

    # Bounce the ball off the walls
    if ball.left < 0 or ball.right > 800:
        x_speed = -x_speed
    if ball.top < 0:
        y_speed = -y_speed

    # Check if the ball hits the player paddle
    if ball.colliderect(player_paddle):
        y_speed = -3

    # Check if the ball collides with any of the tiles
    for tile in tiles:
        if ball.colliderect(tile):
            tiles.remove(tile)
            y_speed = -3

    # Draw the background
    screen.blit(background, (0, 0))

    # Draw the tiles
    for tile in tiles:
        pygame.draw.rect(screen, tile_color, tile)

    # Draw the player paddle
    pygame.draw.rect(screen, BLACK, player_paddle)

    # Draw the ball
    pygame.draw.rect(screen, BLACK, ball)

    pygame.display.update()
    clock.tick(30)