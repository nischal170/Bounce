import pygame as pg
import random
from Settings import *
from sprites import *
import os


class Game:
    def __init__(self):

        pg.init()#initialize game window,etc
        pg.mixer.init()#initialize mixer for all the sound effects and music in game
        self.screen= pg.display.set_mode((WIDTH, HEIGHT))  # set the window size to 800*600
        self.clock = pg.time.Clock()
        self.Bouncing=True

    def new(self):
        self.all_sprites = pg.sprite.Group()  # group of all sprites(entities of the games)
        self.platforms=pg.sprite.Group()
        self.ball=Ball()

        self.all_sprites.add(self.ball)
        p1=Platform(0,HEIGHT-40,WIDTH,40)
        self.all_sprites.add(p1)
        self.platforms.add(p1)
        p2=Platform(WIDTH/2-50,HEIGHT*3/4,100,20)
        self.all_sprites.add(p2)
        self.platforms.add(p2)

        self.run()

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
        hits=pg.sprite.spritecollide(self.ball ,self.platforms,False)
        if hits:
            self.ball.pos.y=hits[0].rect.top
            self.ball.vel.y=0
            #self.ball.pos.y=hits[0].rect.bottom
            #self.ball.vel.y=0


    def events(self):
        #game Loop-events
        for event in pg.event.get():
            #check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing=False
                self.Bouncing = False

            #self.ball.bounce()

    def draw(self):
        #Game Loop -draw
        self.screen.fill(SKY)  # fills the screen with sky colur
        self.all_sprites.draw(self.screen)  # draw all the entities on the screen
        pg.display.flip()  # flipping the board after its drawn


    def show_start_screen(self):
        pass
    def show_go_screen(self):
        pass


g=Game()#creating Object of the class
g.show_start_screen()
while g.Bouncing:
    g.new()
    g.show_go_screen()


pg.quit()





