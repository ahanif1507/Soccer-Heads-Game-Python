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
                
        # apply friction
        self.acc.x += self.vel.x * player_friction
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
       
        self.rect.midbottom = self.pos


class singlePlayer(pygame.sprite.Sprite):
    def __init__(self, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pygame.Surface((40, 40))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.image = pygame.image.load("images/SinglePlayer.png")
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
        
        if (self.pos.x -20 > 0 and self.pos.x +20 < WIDTH) and self.pos.x > self.game.soccer.pos.x:
            self.acc.x = -0.3

        if (self.pos.x -20 > 0 and self.pos.x +20 < WIDTH) and self.pos.x < self.game.soccer.pos.x:
            self.acc.x = 0.4
         
        if self.game.soccer.acc.x == 0 and (self.pos.x -20 > 0 and self.pos.x +20 < WIDTH):
            self.acc.x = 0.25

        if self.game.soccer.pos.y < 300 and (self.pos.x -20 > 0 and self.pos.x +20 < WIDTH):
            self.jump()

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
        
    def update(self):
        
        if self.vel.y > 0:
            hits = pygame.sprite.spritecollide(self, self.game.feild, False)
            if hits:
                self.pos.y = hits[0].rect.top+1
                self.vel.y = self.bounce
                if self.bounce <= 0:
                    self.bounce = self.bounce + 1
        
        hits = pygame.sprite.spritecollide(self, self.game.P1, False)
        if hits:
            self.vel.x = -15
            self.vel.y = -5
            self.bounce = -5
            
        if self.game.MP == True:
            hits2 = pygame.sprite.spritecollide(self, self.game.P2, False)
            if hits2:
                self.vel.x = 15
                self.vel.y = -5
                self.bounce = -5

        if self.game.SP == True:
            hits3 = pygame.sprite.spritecollide(self, self.game.S_P, False)
            if hits3:
                self.vel.x = 15
                self.vel.y = -5
                self.bounce = -5
        
        self.acc = vec(0, soccer_Grav)
        # apply friction
        self.acc.x += self.vel.x * soccer_friction
        # equations of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.rect.midbottom = self.pos

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
