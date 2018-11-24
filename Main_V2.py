#15-112: Fundamentals of Programming and Computer Science
#Final Project
#Name      : Ahmad Hanif
#AndrewID  : ahanif   

import pygame 
import random
from settings import *
from sprites import *

class Game:
    def __init__(self):
        # initialize game window, etc
        pygame.init()
        pygame.mixer.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(Title)
        self.clock = pygame.time.Clock()
        self.running = True

    def new(self):
        # start a new game
        self.all_sprites = pygame.sprite.Group()
        self.feild = pygame.sprite.Group()
        self.player = Player(self)
        self.player2 = Player2(self)
        self.soccer = Soccer()
        self.ground = ground()
        
        self.all_sprites.add(self.player)
        self.all_sprites.add(self.player2)
        self.all_sprites.add(self.soccer)
        self.feild.add(self.ground)

        self.run()

    def run(self):
        # Game Loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def update(self):
        # Game Loop - Update
        self.all_sprites.update()
        # check if player hits a ground - only if falling
        if self.player.vel.y > 0:
            hits = pygame.sprite.spritecollide(self.player, self.feild, False)
            if hits:
                self.player.pos.y = hits[0].rect.top+1
                self.player.vel.y = 0
        if self.player2.vel.y > 0:
            hits = pygame.sprite.spritecollide(self.player2, self.feild, False)
            if hits:
                self.player2.pos.y = hits[0].rect.top+1
                self.player2.vel.y = 0


    def events(self):
        # Game Loop - events
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.player.jump()
                if event.key == pygame.K_w:
                    self.player2.jump()
           
    def draw(self):
        # Game Loop - draw
        self.screen.fill(BLACK)
        self.feild.draw(self.screen)
        self.screen.blit(bg,(0,0))
        self.screen.blit(GoalL,(0,247))
        self.screen.blit(GoalR,(683,247))
        self.all_sprites.draw(self.screen)
        # *after* drawing everything, flip the display
        pygame.display.flip()

    def show_start_screen(self):
        # game splash/start screen
        pass

    def show_go_screen(self):
        # game over/continue
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()
