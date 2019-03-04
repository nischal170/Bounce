#sprite classes for Bounce
import pygame as pg
from Settings import *
import os
vec=pg.math.Vector2 #2d vector

game_folder=os.path.dirname(__file__)
img_folder=os.path.join(game_folder,"img")

vec=pg.math.Vector2#vector
class Ball(pg.sprite.Sprite):    #pg.sprite.Sprite is a Simple base class for visible game objects.
    def __init__(self,game):
        pg.sprite.Sprite.__init__(self) #first thing you need to do after dunder init metod in sprite class
        self.game=game
        self.image=pg.image.load(os.path.join(img_folder,"image1.png")).convert()
        self.image.set_colorkey(WHITE)
        self.rect=self.image.get_rect()
        self.rect.center=(WIDTH/2,HEIGHT/2)
        self.pos=vec(WIDTH/2,HEIGHT/2)
        self.vel=vec(0,0) #initial velocity in x and y direction
        self.acc=vec(0,0)


    def bounce(self):
        self.rect.x=self.rect.x+1
        hits=pg.sprite.spritecollide(self,self.game.platforms,False)
        self.rect.x=self.rect.x-1
        if hits:
            self.vel.y=-20

       # hits = pg.sprite.spritecollide(self.game.ball, self.game.platforms, False)
        #if hits:
            # self.game.ball.pos.y = hits[0].rect.bottom
             #self.game.ball.vel.y =+20
             #pass





    def update(self):
        self.acc=vec(0,0.7) #initial acceleration in x and y direction
        keys =pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x=-ball_acc
        if keys[pg.K_RIGHT]:
            self.acc.x=ball_acc

        self.acc.x+=self.vel.x*ball_friction #apply friction only in x direction

        self.vel +=self.acc
        self.pos +=self.vel+1*self.acc

        # wrap around the sides of the screen
        if self.pos.x >WIDTH:
            self.pos.x=WIDTH
        if self.pos.x<0:
            self.pos.x=0


        self.rect.midbottom=self.pos #calculate the position as middbottom
        #self.rect.midtop=


class Platform(pg.sprite.Sprite):
        def __init__(self,x,y,w,h):
            pg.sprite.Sprite.__init__(self)
            self.image=pg.Surface((w,h))
            self.image.fill(LIMEGREEN)
            self.rect=self.image.get_rect()
            self.rect.x=x
            self.rect.y=y


