import pygame
from settings import *
vec = pygame.math.Vector2

class Player(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pygame.Surface((40, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.image = pygame.image.load("images/player1.png")
        self.rect.midbottom = (659, 386)
        self.pos = vec(659, 386)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def jump(self):
        self.rect.x += 1
        hits = pygame.sprite.spritecollide(self, self.game.feild, False)
        self.rect.x -= 1
        self.vel.y = player1_jump
    
    def update(self):
        self.acc = vec(0, player_Grav)
        keystate = pygame.key.get_pressed()
    
        if keystate[pygame.K_LEFT]:
            # Check if player within frame
            if self.pos.x -20 > 0:
                self.acc.x = player1_fwd_acc
        if keystate[pygame.K_RIGHT]:
            # Check if player within frame
            if self.pos.x +20 < WIDTH:
                self.acc.x = player1_bkd_acc

        # apply friction
        self.acc.x += self.vel.x * player_friction
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        
        self.rect.midbottom = self.pos


class Player2(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pygame.Surface((40, 40))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.image = pygame.image.load("images/player2.png")
        self.rect.midbottom = (100, 386)
        self.pos = vec(100, 386)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def jump(self):
        self.rect.x += 1
        hits = pygame.sprite.spritecollide(self, self.game.feild, False)
        self.rect.x -= 1
        self.vel.y = player2_jump
        
    def update(self):
        self.acc = vec(0, player_Grav)
        keystate = pygame.key.get_pressed()
    
        if keystate[pygame.K_a]:
            # Check if player within frame
            if self.pos.x -20 > 0:
                self.acc.x = player2_bkd_acc
        if keystate[pygame.K_d]:
            # Check if player within frame
            if self.pos.x +20 < WIDTH :
                self.acc.x = player2_fwd_acc

        # apply friction
        self.acc.x += self.vel.x * player_friction
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
       
        self.rect.midbottom = self.pos

class Soccer(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((40, 40))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.image = pygame.image.load("images/soccer3.png")
        self.rect.center = (377 , 115)

    def update(self):
        pass

'''class soccer1:
    def __init__(self, (x,y), size, color=(255,255,255),width=1):
        self.x=x
        self.y=y
        self.size=size
        self.color=color
        self.width=width
    def update(self):
        pygame.draw.circle(screen, self.color, (self.x,self.y), self.size, self.width)
'''

class ground(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((759 , 56))
        self.image.fill(BROWN)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 386
    
