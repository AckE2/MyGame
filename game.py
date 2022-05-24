from curses import COLOR_BLUE
from re import S, X
from tkinter import Y
from turtle import color
import pygame, sys
from sys import exit
from player import Player 
from meteor import Meteor
from random import randint
from os import path
import pickle
from laser import Laser





class Game:
    def __init__(self): 
        self.meteors = pygame.sprite.Group()
        self.meteor_setup(rows = 1, cols = 1)
        self.meteor_direction = 1
        
        self.lives = 3
        self.live_image = pygame.image.load('lives.png').convert_alpha()
        self.live_image = pygame.transform.scale(self.live_image, (20, 20))
        self.live_x_start_pos = 600 - (self.live_image.get_size()[0] * 2 +20)
        self.font = pygame.font.Font('upheavtt.ttf', 20)
        self.over_font = pygame.font.Font('upheavtt.ttf', 50)

        screen_width = 600
        screen_height = 600
        self.screen = pygame.display.set_mode((screen_width,screen_height))

        self.once = True
        self.clicked = False
        self.lasers = pygame.sprite.Group()
   
    def set_high_score(self, highscore_value):
        self.highscore = highscore_value

    def load_score(self, score):
        self.score = score

    def load_lives(self, lives):
        self.lives = lives
    
    def load_meteor_time(self, time):
        self.meteor_spawn_time = time
            
    def high_score(self):
        if self.score >= self.highscore:
            self.highscore = self.score
        highscore_image = self.font.render(f'highscore: {self.highscore}', False,'white')
        highscore_rect = highscore_image.get_rect(topleft=(5,0))
        self.screen.blit(highscore_image,highscore_rect)
    
    def meteor_setup(self,rows,cols,x_distance = 60,y_distance = 60, x_offset = randint(70,530), y_offset = -60):
        for row_index, row in enumerate(range(rows)):
            for col_index, row in enumerate(range(cols)):
                x = col_index * x_distance + x_offset
                y = row_index * y_distance + y_offset
                meteor_sprite = Meteor(x,y)

    def load_meteor(self, x, y):
        meteor_sprite = Meteor(x,y)
        self.meteors.add(meteor_sprite)

    def load_player(self, pos):
        player_sprite = Player(pos)
        self.player = pygame.sprite.GroupSingle(player_sprite)

    def load_laser(self, pos):
        laser_sprite = Laser(pos) 
        self.player.sprite.lasers.add(laser_sprite)

    def meteor_movement(self):
        for meteor in self.meteors.sprites():
            if self.lives<=0:
                meteor.move(0)
            else:
                meteor.move(2)

    def meteor_timer(self):
        self.meteor_spawn_time -= 1
        if self.lives <=0:
            if self.meteor_spawn_time <= 0:
                self.meteors.add(Meteor(randint(70,530), -60))
                self.meteor_spawn_time = 99999999999999999999
        
        else:    
            if self.meteor_spawn_time <= 0:
                self.meteors.add(Meteor(randint(70,530), -60))
                self.meteor_spawn_time = 75

    def collision_control(self):
        if self.player.sprite.lasers:
            for laser in self.player.sprite.lasers:
                if pygame.sprite.spritecollide(laser,self.meteors,True):
                    self.score += 100
                    laser.kill()
        
        if self.meteors:
            for meteor in self.meteors:
                if pygame.sprite.spritecollide(meteor,self.player,False) and self.lives > 0:
                    meteor.kill()
                    self.lives -= 1
                    
                    if self.lives <= 0:
                        game_over_image = self.font.render(f'GAME OVER', False, 'white')
                        game_over_rect = game_over_image.get_rect(topleft=(250,250))
                        self.screen.blit(game_over_image,game_over_rect)
                    
                    return
              
    def button(self):
        self.clicked = False
        pos = pygame.mouse.get_pos()
        bot= pygame.draw.rect(self.screen, (251,191,0), (225, 350, 150, 50))
        restart_image = self.font.render(f'RESTART', False, 'black')
        restart_rect = restart_image.get_rect(topleft=(265,365))
        self.screen.blit(restart_image,restart_rect)
        

        if bot.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:    
                self.lives=3
                self.clicked = True
                self.score = 0
                player_sprite = Player(pos=(300,300))
                self.player = pygame.sprite.GroupSingle(player_sprite)
                for meteor in self.meteors:
                    meteor.kill()
                for laser in self.player.sprite.lasers:
                    laser.kill()


    def display_lives(self):
        for live in range(self.lives - 1):
            x = self.live_x_start_pos + (live * (self.live_image.get_size()[0] + 10))
            self.screen.blit(self.live_image,(x,8)) 

    def score_counter(self):
        score_image = self.font.render(f'score: {self.score}', False,'white')
        score_rect = score_image.get_rect(topleft=(5,20))
        self.screen.blit(score_image,score_rect) 

    def game_over(self):
        game_over_image = self.over_font.render(f'GAME OVER', False, 'white')
        game_over_rect = game_over_image.get_rect(topleft=(175,250))
        self.screen.blit(game_over_image,game_over_rect)
        
    def gather(self):
        self.player.update()
        self.meteor_movement()
        self.player.sprite.lasers.draw(self.screen)
        self.player.draw(self.screen)
        self.meteors.draw(self.screen)
        self.meteor_timer()
        self.collision_control()
        self.display_lives()
        self.score_counter()
        self.high_score()
        
    def run(self):   
        if self.lives <= 0:     
            self.game_over()
            self.button()
            self.high_score()
                
        else:
            self.gather()
                    
            



