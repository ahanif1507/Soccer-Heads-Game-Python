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
        if hits:
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

        #if keystate[pygame.K_KP0]:
                #shoot()

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
        if hits:
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

        #if keystate[pygame.K_LSHIFT]:
                #shoot()

        # apply friction
        self.acc.x += self.vel.x * player_friction
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
       
        self.rect.midbottom = self.pos

class Soccer(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pygame.Surface((30, 30))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.image = pygame.image.load("images/soccer.png")
        self.rect.midbottom = (377 , 145)
        self.pos = vec(377, 145)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.bounce = -10
        self.P1_score = 0
        self.P2_score = 0

    def update(self):

        hits = pygame.sprite.spritecollide(self, self.game.P1, False)
        if hits:
            self.vel.x = -25

        hits2 = pygame.sprite.spritecollide(self, self.game.P2, False)
        if hits2:
            self.vel.x = 25

        P1_scores = pygame.sprite.spritecollide(self, self.game.L_goal_post, False)
        if P1_scores:
            self.pos = vec(377, 145)
            self.P1_score += 1

        P2_scores = pygame.sprite.spritecollide(self, self.game.R_goal_post, False)
        if P2_scores:
            self.pos = vec(377, 145)
            self.P2_score += 1
        
        self.acc = vec(0, soccer_Grav)
        # apply friction
        self.acc.x += self.vel.x * soccer_friction
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos

    def shoot(self):
        pass

'''
    def Player1_score(self):
        P1_score += 1
        pass

    def Player2_score(self):
        P2_score += 1
        pass
'''

'''
class soccer1:
    def __init__(self, (x,y), size, color=(255,255,255),width=1):
        self.x=x
        self.y=y
        self.size=size
        self.color=color
        self.width=width
    def update(self):
        pygame.draw.circle(screen, self.color, (self.x,self.y), self.size, self.width)
'''

class R_Goal(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((76, 138))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.image = pygame.image.load("images/Goal Post R.png")
        self.rect.bottomright = (759 , 386)

class L_Goal(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((76, 138))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.image = pygame.image.load("images/Goal Post L.png")
        self.rect.bottomleft = (0 , 386)

class ground(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((759 , 56))
        self.image.fill(BROWN)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 386
    
