import random
import pygame
from screens import BaseScreen
import requests

from ..components import Paddle, Ball, TileGroup, tile
from components import TextBox

pygame.display.set_caption('Tile breaker')

# Clock
clock = pygame.time.Clock()

#spirtes
pygame.init()
background = pygame.image.load("./breakout/images/background.jpg")

# Sounds
blip = pygame.mixer.Sound("./breakout/Sounds/blip.wav")
menu = pygame.mixer.Sound("./breakout/Sounds/menu.wav")
death = pygame.mixer.Sound("./breakout/Sounds/death.wav")

class GameScreen(BaseScreen):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Create the paddle
        self.paddle = Paddle(200, 30, (76, 201, 240), limits=self.rect)

        # Create the ball
        self.ball = Ball(limits=self.rect)
        self.ball.speed = 8
        self.ball.angle = random.randint(0, 31416) / 10000

        # Level
        self.level = 0
        self.tiles = TileGroup()

        self.score = 0
        self.combo = 1

        # Put all sprites in the group
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.paddle)
        self.sprites.add(self.ball)
        self.sprites.add(self.tiles)

    def update(self):

        # paddle
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.paddle.move("left")

        if keys[pygame.K_RIGHT]:
            self.paddle.move("right")

        # collided
        self.sprites.update()

        collided = self.ball.collidetiles(self.tiles)
        if collided:
            pygame.mixer.Sound.play(blip)
            self.score += 50 + (25*self.combo)
            self.combo += 1

        caught_the_ball = self.ball.collidepaddle(self.paddle.rect)
        if caught_the_ball:
            self.combo = 1
            pygame.mixer.Sound.play(menu)

        # time 
        clock.tick(60)
        self.time = pygame.time.get_ticks() / 1000
        font = pygame.font.SysFont('Arial', 24)
        

        # text 
        self.score_text = font.render("Score: " + str(self.score), True, (0,0,0))
        self.text = font.render("Time: " + str(self.time), True, (0, 0, 0))
        self.combo_text = font.render("Combo: " + str(self.combo), True, (0, 0, 0))
        
        # death
        if self.ball.rect.bottom > self.paddle.rect.top and not caught_the_ball:
            self.running = False
            self.time = 0
            pygame.mixer.Sound.play(death)
            pygame.time.delay(250)
            self.next_screen = "game_over"
            post = requests.post("http://127.0.0.1:5000/add", json={"score": self.score})

        # level 
        if not self.tiles:
            print('sprite_group is empty')
            if self.level == 4:
                self.level = 0
            else:
                self.level += 1 
                self.score += self.level*100
                self.ball.speed += 1
            self.tiles = TileGroup(level=self.level)

    def draw(self):
        self.window.fill((255, 255, 255))
        self.window.blit(background, (0,0))
        self.sprites.draw(self.window)
        self.tiles.draw(self.window)
        self.window.blit(self.text, [50, 5])
        self.window.blit(self.score_text, [250, 5])
        self.window.blit(self.combo_text, [350, 5])

    def manage_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            self.running = False
            self.next_screen = "welcome"

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                self.ball.angle = 1.5
