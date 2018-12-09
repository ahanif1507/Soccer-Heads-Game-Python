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
        self.font_name = pygame.font.match_font(FONT_NAME)
        
    def new(self):
        #start a new game
        self.P1_score = 0
        self.P2_score = 0
        self.SP_score = 0
        self.Timer = 60
        
        self.P1 = pygame.sprite.Group()
        self.feild = pygame.sprite.Group()
        self.L_goal_post = pygame.sprite.Group()
        self.R_goal_post = pygame.sprite.Group()
        self.football = pygame.sprite.Group()

        self.player = Player(self)
        self.soccer = Soccer(self)
        self.ground = ground()
        self.R_Goal = R_Goal()
        self.L_Goal = L_Goal()

        self.P1.add(self.player)
        self.feild.add(self.ground)
        self.L_goal_post.add(self.L_Goal)
        self.R_goal_post.add(self.R_Goal)
        self.football.add(self.soccer)

        if self.SP == True:
            self.S_P = pygame.sprite.Group()
            self.Single_Player = singlePlayer(self)
            self.S_P.add(self.Single_Player)

        if self.MP == True:
            self.P2 = pygame.sprite.Group()
            self.player2 = Player2(self)
            self.P2.add(self.player2)

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

        if self.MP == True:
            self.P2.update()

        if self.SP == True:
            self.Single_Player.update()

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
        if self.MP == True:
            if self.player2.vel.y > 0:
                hits = pygame.sprite.spritecollide(self.player2, self.feild, False)
                if hits:
                    self.player2.pos.y = hits[0].rect.top+1
                    self.player2.vel.y = 0

        if self.SP == True:
            if self.Single_Player.vel.y > 0:
                hits = pygame.sprite.spritecollide(self.Single_Player, self.feild, False)
                if hits:
                    self.Single_Player.pos.y = hits[0].rect.top+1
                    self.Single_Player.vel.y = 0
        
        # Palyer 1 goal score count
        P1_scores = pygame.sprite.spritecollide(self.soccer, self.L_goal_post, False)
        if P1_scores:
            self.soccer.pos = vec(377, 145)
            self.P1_score += 1
            self.draw_text(str(self.P1_score), 22, WHITE, 664, 15)
            self.player.pos = vec (659, 386)
            if self.MP == True:
                self.player2.pos = vec (100, 386)
            if self.SP == True:
                self.Single_Player.pos = vec (100, 386)    
            self.soccer.bounce = -10

        # Player 2 goal score count
        if self.MP == True:
            P2_scores = pygame.sprite.spritecollide(self.soccer, self.R_goal_post, False)
            if P2_scores:
                self.soccer.pos = vec(377, 145)
                self.P2_score += 1
                self.draw_text(str(self.P2_score), 22, WHITE, 95, 15)
                self.player.pos = vec (659, 386)
                self.player2.pos = vec (100, 386)
                self.soccer.bounce = -10

        if self.SP == True:
            SP_scores = pygame.sprite.spritecollide(self.soccer, self.R_goal_post, False)
            if SP_scores:
                self.soccer.pos = vec(377, 145)
                self.SP_score += 1
                self.draw_text(str(self.P2_score), 22, WHITE, 95, 15)
                self.player.pos = vec (659, 386)
                self.Single_Player.pos = vec (100, 386)
                self.soccer.bounce = -10

        int(round(self.Timer))
        self.draw_text(str(int(round(self.Timer))), 30, WHITE, WIDTH/2, 15)
        self.Timer -= 0.0167
        if self.Timer <= 0:
            self.playing = False
                
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
                if event.key == pygame.K_w and self.MP == True:
                    self.player2.jump()
                #if event.key == pygame.K_UP and self.SP == True:
                    #self.Single_Player.jump()
              
    def draw(self):
        # Game Loop - draw
        self.screen.fill(BLACK)
        self.feild.draw(self.screen)
        self.screen.blit(bg,(0,0))

        self.P1.draw(self.screen)
        if self.MP == True:
            self.P2.draw(self.screen)
        if self.SP == True:
            self.S_P.draw(self.screen)
        
        self.L_goal_post.draw(self.screen)
        self.R_goal_post.draw(self.screen)
        self.football.draw(self.screen)
        self.draw_text(str(self.P1_score), 22, WHITE, 664, 15)

        if self.MP == True:
            self.draw_text(str(self.P2_score), 22, WHITE, 95, 15)
        if self.SP == True:
            self.draw_text(str(self.SP_score), 22, WHITE, 95, 15)
            
        self.draw_text(str(int(round(self.Timer))), 30, WHITE, WIDTH/2, 15)        
        # after drawing everything, flip the display
        pygame.display.flip()

    def start_screen(self):
        self.screen.blit(intro,(0,0))
        pygame.display.update()
        self.game_mode()
        if self.MP == True:
            self.MP_instructions()
        if self.SP == True:
            self.SP_instructions()

    def MP_instructions(self):
        self.screen.blit(MP_instructions,(0,0))
        pygame.display.update()
        pygame.display.flip()
        self.wait_for_key()

    def SP_instructions(self):
        self.screen.blit(SP_instructions,(0,0))
        pygame.display.update()
        pygame.display.flip()
        self.wait_for_key()
    
    def go_screen(self):
        # game over/continue
        if not self.running:
            return
        self.screen.fill(BLACK)
        self.screen.blit(GameOver,(0,0))

        if self.MP == True:
            self.draw_text("GAME OVER", 48, WHITE, WIDTH / 2, HEIGHT / 4)
            if self.P1_score > self.P2_score:
                self.draw_text("Player 1 won the Game", 36, WHITE, WIDTH / 2, HEIGHT / 2)
            if self.P2_score > self.P1_score:
                self.draw_text("Player 2 won the Game", 36, WHITE, WIDTH / 2, HEIGHT / 2)
            if self.P2_score == self.P1_score:
                self.draw_text("It's a Draw!", 36, WHITE, WIDTH / 2, HEIGHT / 2)
            self.draw_text("Press any key to Continue", 36, WHITE, WIDTH / 2, HEIGHT * 3 / 4)

        if self.SP == True:
            self.draw_text("GAME OVER", 48, WHITE, WIDTH / 2, HEIGHT / 4)
            if self.P1_score > self.SP_score:
                self.draw_text("You won the Game", 36, WHITE, WIDTH / 2, HEIGHT / 2)
            if self.SP_score > self.P1_score:
                self.draw_text("You lost the Game", 36, WHITE, WIDTH / 2, HEIGHT / 2)
            if self.SP_score == self.P1_score:
                self.draw_text("It's a Draw!", 36, WHITE, WIDTH / 2, HEIGHT / 2)
            self.draw_text("Press any key to Continue", 36, WHITE, WIDTH / 2, HEIGHT * 3 / 4)
            
        pygame.display.flip()
        self.Continue()

    def draw_text(self, text, size, color, x, y):
        font = pygame.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_surface, text_rect)

    def game_mode(self):
        spButton = pygame.draw.rect(self.screen, WHITE,(306,174,147,48))
        mpButton = pygame.draw.rect(self.screen, WHITE,(306,258,147,48))
        waiting = True
        self.SP = False
        self.MP = False
        while waiting:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if spButton.collidepoint(mouse_pos):
                        mouse = pygame.mouse.get_pos()
                        if 306+147 > mouse[0] > 306 and 174+48 > mouse[1] > 174:
                            waiting = False
                            self.SP = True         
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if mpButton.collidepoint(mouse_pos):
                        mouse = pygame.mouse.get_pos()
                        if 306+147 > mouse[0] > 306 and 258+48 > mouse[1] > 258:
                            waiting = False
                            self.MP = True                   

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pygame.KEYUP:
                    waiting = False
    
    def Continue(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pygame.KEYUP:
                    self.start_screen()
                    waiting = False

    
game = Game()
game.start_screen()

while game.running:
    game.new()
    game.go_screen()
    
pygame.quit()
