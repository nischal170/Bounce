#sprite classes for Bounce
import pygame as pg
from Settings import *
import os
game_folder=os.path.dirname(__file__)
img_folder=os.path.join(game_folder,"img")

vec=pg.math.Vector2
class Ball(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image=pg.image.load(os.path.join(img_folder,"image1.png")).convert()
        self.image.set_colorkey(WHITE)
        self.rect=self.image.get_rect()
        self.rect.center=(WIDTH/2,HEIGHT/2)
        self.pos=vec(WIDTH/2,HEIGHT/2)
        self.vel=vec(0,0)
        self.acc=vec(0,0)


    def bounce(self):
        self.vel.y=-4



    def update(self):
        self.acc=vec(0,0.6) #initial acceleration in x and y direction
        keys =pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x=-ball_acc
        if keys[pg.K_RIGHT]:
            self.acc.x=ball_acc

        self.acc.x+=self.vel.x*ball_friction
        self.vel +=self.acc

        self.pos +=self.vel+0.9*self.acc
        if self.pos.x >WIDTH:
            self.pos.x=WIDTH-10
        if self.pos.x<0:
            self.pos.x=0+10


        self.rect.midbottom=self.pos
        #self.rect.midtop=


class Platform(pg.sprite.Sprite):
        def __init__(self,x,y,w,h):
            pg.sprite.Sprite.__init__(self)
            self.image=pg.Surface((w,h))
            self.image.fill(LIMEGREEN)
            self.rect=self.image.get_rect()
            self.rect.x=x
            self.rect.y=y


