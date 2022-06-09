import pygame as pg
import random
from Settings import *
from sprites import *
import os


class Game:
    def __init__(self):  # Like constructor in C++ used to initialize the class elements

        pg.init()#initialize game window,etc
        pg.mixer.init()#initialize mixer for all the sound effects and music in game
        self.screen= pg.display.set_mode((WIDTH, HEIGHT))  # set the window size to Width*Height
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock() # create an object to help track time
        self.Bouncing=True
        self.font_name=pg.font.match_font(FONT_NAME)

    def new(self):
        #start a new game
        self.score=0
        self.all_sprites = pg.sprite.Group()  #A  container class to hold and manage multiple Sprite objects ,group of all sprites(entities of the games)
        self.platforms=pg.sprite.Group()
        self.ball=Ball(self)

        self.all_sprites.add(self.ball)
        for plat in PLATFORM_LIST:
            p=Platform(*plat)#exploding the list ie multiple platforms
            self.all_sprites.add(p)
            self.platforms.add(p)

        self.run()

    def run(self):
        #game loop
        self.playing=True
        while self.playing:    #loop continues until self.playing is true
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()



    def update(self):
        #Game Loop-Update
        self.all_sprites.update()  # update all the entities after key press
        if self.ball.vel.y>0:
            hits=pg.sprite.spritecollide(self.ball ,self.platforms,False)
            if hits:

                self.ball.pos.y=hits[0].rect.top   #sets to whatever we hit to its top
                self.ball.vel.y=0
                #if(hits[0].rect.bottom):
                    #self.ball.pos.y  = 300
                        #-=abs(self.ball.vel.y)

        #if player reaches top 1/4 of screen
        if self.ball.rect.top<=HEIGHT/4:
            self.ball.pos.y+=abs(self.ball.vel.y)
            for plat in self.platforms:
                plat.rect.y+=abs(self.ball.vel.y)
                if plat.rect.top>=HEIGHT:
                    plat.kill()
                    self.score+=10


        #die
        if self.ball.rect.bottom > HEIGHT:
            self.playing=False








        while len(self.platforms)< 9: #no of platforms in a screen
            width=random.randrange(80,150)

            p=Platform(random.randrange(0,WIDTH-width),0,width,20)
            self.platforms.add(p)
            self.all_sprites.add(p)



    def events(self):
        #game Loop-events
        for event in pg.event.get():
            #check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing=False
                self.Bouncing = False
            if event.type==pg.KEYDOWN:
                if event.key ==pg.K_SPACE:
                    self.ball.bounce()

            #self.ball.bounce()

    def draw(self):
        #Game Loop -draw
        self.screen.fill(SKY)  # fills the screen with sky colour
        self.all_sprites.draw(self.screen)  # draw all the entities on the screen
        self.draw_text(str(self.score),22,BLACK,WIDTH/2,15)
        pg.display.flip()  # flipping the board after its drawn


    def show_start_screen(self):
        self.screen.fill(SKY)
        self.draw_text(TITLE,50,TOMATO,WIDTH/2,HEIGHT/4)
        self.draw_text("Press Arrows to Move,Space to jump",22,TOMATO,WIDTH/2,HEIGHT/2)
        self.draw_text("press any key to start playing ",20,TOMATO,WIDTH/2,HEIGHT*3/4)
        self.draw_text("Developed By Nischal and Rohit",30, FIREBRICK, WIDTH / 2, HEIGHT*0.95)
        pg.display.flip()
        self.wait_for_key()


    def show_go_screen(self):
        self.screen.fill(SKY)
        self.draw_text("GAME OVER", 48, TOMATO, WIDTH / 2, HEIGHT / 4)
        self.draw_text("Score:"+str(self.score), 22, TOMATO, WIDTH / 2, HEIGHT / 2)
        self.draw_text("press any key to start playing again ", 22, TOMATO, WIDTH/2,HEIGHT*3/4)
        pg.display.flip()
        self.wait_for_key()


    def wait_for_key(self):
        waiting=True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type==pg.QUIT:
                    waiting=False
                    self.Bouncing=False
                if event.type==pg.KEYUP:
                    waiting=False

    def draw_text(self,text,size,color,x,y):
        font=pg.font.Font(self.font_name,size)
        text_surface=font.render(text,True,color)
        text_rect =text_surface.get_rect()
        text_rect.midtop=(x,y)
        self.screen.blit(text_surface,text_rect)


g=Game()#creating Object of the class
g.show_start_screen()
while g.Bouncing:#Loop continues until g.bouncing is true
    g.new()
    g.show_go_screen()


pg.quit()





