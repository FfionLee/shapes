import pgzrun
import random

WIDTH=400
HEIGHT=400

def draw():
    screen.fill('lightblue1')
    s=150

    for i in range(10): 
        screen.draw.filled_circle((200,200),s,(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        s=s-15

pgzrun.go()