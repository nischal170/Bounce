import pygame
import random
from Settings import *
import os

pygame.init()
#initialize all the modules with pygame


game_folder=os.path.dirname(__file__)

img_folder=os.path.join(game_folder,"img")

class Ball(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load(os.path.join(img_folder,"image1.png")).convert()
        #pygame.Surface((50,50))
        self.image.set_colorkey(WHITE)

        self.rect = self.image.get_rect()
        self.rect.centerx =WIDTH/2
        self.rect.bottom=HEIGHT/2
        self.y_speed=5
        self.x_change=0


    def update (self):
        self.x_change = 0
        keystate = pygame.key.get_pressed()

        self.rect.y+=self.y_speed
        if self.rect.bottom >HEIGHT-200:
            self.y_speed=-7
        if self.rect.top < 200:
            self.y_speed=5


        if keystate[pygame.K_LEFT]:
            self.x_change=-5

        self.rect.x += self.x_change

        if keystate[pygame.K_RIGHT]:
            self.x_change = 5
        self.rect.x += self.x_change
        if self.rect.right>WIDTH:
            self.rect.right=WIDTH
        if self.rect.left<0:
            self.rect.left=0






pygame.mixer.init()#initialize mixer for all the sound effects and music in game

gameDisplay=pygame.display.set_mode((WIDTH,HEIGHT)) #set the window size to 800*600

pygame.display.set_caption(TITLE) #set the title of window

clock=pygame.time.Clock()


all_sprites=pygame.sprite.Group()# group of all sprites(entities of the games)

ball=Ball() #creating an object out of a class

all_sprites.add(ball)

#only thing that will break the loop is when the ball crashes

#we initialize the Bounce Variable with True
x_change=0 #initializing the change of the horizontal value to zero

#Game Loop
Running=True
while  Running:#while Running still equal True
    clock.tick(FPS)
#Process Input(events)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            Bounce=False










    #update game
    all_sprites.update()#update all the entities after key press

    #draw/Render
    gameDisplay.fill(SKY)#fills the screen with sky colur
    all_sprites.draw(gameDisplay)#draw all the entities on the screen




    pygame.display.flip()#flipping the board after its drawn

pygame.quit()
quit()






