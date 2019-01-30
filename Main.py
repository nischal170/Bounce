import pygame as pg
import random
from Settings import *
from sprites import *
import os

class Game:
    def __init__(self):
        #initialize game window,etc
        pg.init()
        pg.mixer.init()#initialize mixer for all the sound effects and music in game
        self.screen= pg.display.set_mode((WIDTH, HEIGHT))  # set the window size to 800*600
        self.clock = pg.time.Clock()

    def new(self):
        self.all_sprites = pg.sprite.Group()  # group of all sprites(entities of the games)

    def run(self):
        #game loop
        self.playing=True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()



    def update(self):
        #Game Loop-Update
        self.all_sprites.update()  # update all the entities after key press

    def events(self):
        #game Loop-events
        for event in pg.event.get():
            #check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing=False
                self.running = False

    def draw(self):
        #Game Loop -draw
        self.screen.fill(SKY)  # fills the screen with sky colur
        self.all_sprites.draw(self.screen)  # draw all the entities on the screen
        pg.display.flip()  # flipping the board after its drawn


    def show_start_screen(self):
        pass
    def show_go_screen(self):
        pass


g=Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()


pg.quit()





