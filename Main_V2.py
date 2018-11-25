#15-112: Fundamentals of Programming and Computer Science
#Final Project
#Name      : Ahmad Hanif
#AndrewID  : ahanif   

import pygame 
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
        self.P1 = pygame.sprite.Group()
        self.P2 = pygame.sprite.Group()
        self.feild = pygame.sprite.Group()
        self.L_goal_post = pygame.sprite.Group()
        self.R_goal_post = pygame.sprite.Group()
        self.football = pygame.sprite.Group()

        self.player = Player(self)
        self.player2 = Player2(self)
        self.soccer = Soccer(self)
        self.ground = ground()
        self.R_Goal = R_Goal()
        self.L_Goal = L_Goal()
        
        self.P1.add(self.player)
        self.P2.add(self.player2)
        self.feild.add(self.ground)
        self.L_goal_post.add(self.L_Goal)
        self.R_goal_post.add(self.R_Goal)
        self.football.add(self.soccer)


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
        self.P1.update()
        self.P2.update()
        self.feild.update()
        self.L_goal_post.update()
        self.R_goal_post.update()
        self.football.update()
        
        # check if player hits ground - only if falling
        if self.player.vel.y > 0:
            hits = pygame.sprite.spritecollide(self.player, self.feild, False)
            if hits:
                self.player.pos.y = hits[0].rect.top+1
                self.player.vel.y = 0

        # check if player2 hits ground - only if falling
        if self.player2.vel.y > 0:
            hits = pygame.sprite.spritecollide(self.player2, self.feild, False)
            if hits:
                self.player2.pos.y = hits[0].rect.top+1
                self.player2.vel.y = 0

        # check if soccer hits ground, then bounce slowly coming to rest
        if self.soccer.vel.y > 0:
            hits = pygame.sprite.spritecollide(self.soccer, self.feild, False)
            if hits:
                self.soccer.pos.y = hits[0].rect.top+1
                self.soccer.vel.y = self.soccer.bounce
                if self.soccer.bounce <= 0:
                    self.soccer.bounce = self.soccer.bounce + 1

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

        self.P1.draw(self.screen)
        self.P2.draw(self.screen)
        self.L_goal_post.draw(self.screen)
        self.R_goal_post.draw(self.screen)
        self.football.draw(self.screen)
        # *after* drawing everything, flip the display
        pygame.display.flip()

    def show_start_screen(self):
        # game splash/start screen
        pass

    def show_go_screen(self):
        # game over/continue
        pass

game = Game()
game.show_start_screen()
while game.running:
    game.new()
    game.show_go_screen()

pygame.quit()
