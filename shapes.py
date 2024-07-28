import pgzrun
import random

WIDTH=700
HEIGHT=700

def draw():
    screen.fill('white')
    w=300
    h=100


    for i in range(20):
        r=Rect((0,0),(w,h))
        r.center=350,350
        screen.draw.rect(r,(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        w=w-10
        h=h+10





'''def update():
    pass'''
pgzrun.go()