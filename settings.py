import pygame

# game options
Title = "Soccer Heads"
WIDTH = 759
HEIGHT = 418
FPS = 60

# player settings
player1_fwd_acc = -0.4
player1_bkd_acc = 0.3
player1_jump = -12

player2_fwd_acc = 0.4
player2_bkd_acc = -0.3
player2_jump = -12

player_friction = -0.12

player_Grav = 0.8

# soccer settings
soccer_friction = -0.2
soccer_Grav = 0.3

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BROWN = (100,76,71)

#Stadium
bg = pygame.image.load("images\Stadium.png")
