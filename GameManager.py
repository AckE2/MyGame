from re import S, X
from tkinter import Y
import pygame, sys
from sys import exit
from random import randint
from os import path
import pickle
import json
from game import Game


class gamemanager:

    def control(self):
        loaded_Game = Game()
        dir = path.dirname(__file__)
        with open(path.join(dir, 'control.txt'), 'r') as s:
            self.check = int(s.read())
    
    def save(self, game):
        dir = path.dirname(__file__)

        with open(path.join(dir, 'control.txt'), 'w') as s:
            s.write(str(1))

        if game.score >= game.highscore:
            self.dir = path.dirname(__file__)
            with open(path.join(dir, 'highscore.txt'),'w') as f:
                f.write(str(game.score))

        with open(path.join(dir, 'save_lives.txt'), 'w') as g:
            g.write(str(game.lives))

        with open(path.join(dir, 'save_meteor_time.txt'),'w') as t:
            t.write(str(game.meteor_spawn_time))

        with open('save_meteor.json', 'w') as file:
            data = [(meteor.rect.topleft) 
                    for meteor in game.meteors]   
            json.dump(data, file)

        with open('save_player.json', 'w') as file:
            data = [(player.rect.midbottom) 
                    for player in game.player]   
            json.dump(data, file)

        with open('save_laser.json', 'w') as file:
            data = [(laser.rect.center) 
                    for laser in game.player.sprite.lasers]   
            json.dump(data, file)
            
        with open(path.join(self.dir, 'save_score.txt'),'w') as h:
            h.write(str(game.score))



    def load(self):
        loaded_Game = Game()
        dir = path.dirname(__file__)

        with open(path.join(dir, 'control.txt'), 'w') as s:
            s.write(str(3))

        with open(path.join(dir, 'save_meteor_time.txt'),'r') as t:
            q = t.read()
            loaded_Game.load_meteor_time(int(q))

        with open(path.join(dir, 'save_lives.txt'),'r') as g:
            d = g.read()
            loaded_Game.load_lives(int(d))

        with open('save_meteor.json', 'r') as file:
            data = json.load(file)
            for x, y in data:
                loaded_Game.load_meteor(x,y)
                
        with open('save_player.json', 'r') as file:
            data = json.load(file)
            for pos in data:
                loaded_Game.load_player(pos)
                
        with open('save_laser.json', 'r') as file:
            data = json.load(file)
            for pos in data:
                    loaded_Game.load_laser(pos)
               
        with open(path.join(dir, 'save_score.txt'),'r') as h:
            x = h.read()
            try:
                loaded_Game.load_score(int(x))
            except:
                loaded_Game.load_score(0)

        with open(path.join(dir, 'highscore.txt'),'r') as f:
            print('helo')
            s = f.read()
            loaded_Game.set_high_score(int(s))

        return loaded_Game
            
    def new_game(self):
        new_Game = Game()
        new_Game.load_player(pos=(300,300))
        new_Game.load_meteor_time(75)
        new_Game.load_score(0) 

        self.dir = path.dirname(__file__)
        with open(path.join(self.dir, 'highscore.txt'),'r') as f:
            s = f.read()
            new_Game.set_high_score(int(s))
        
        return new_Game


    def start_game(self):
        
        dir = path.dirname(__file__)
        with open(path.join(dir, 'control.txt'), 'r') as s:
            check = int(s.read())
        
        if check == 1:
            has_files = True
        else:
            has_files = False
    
        if has_files:
            game = self.load()
            return game
        else:
            game_ = self.new_game()
            return game_


    



