import Framework
import math
import Game_Over
from pico2d import *
import os

open_canvas(1600,900)

image = None
Right = None
Back = None
Front = None
Ui = None

Jump_Switch = False
Run_Switch = False

class KimMuk:
    image = None
    def __init__(self):
        global Jump_Switch
        self.x, self.y, self.x1 = 110, 100, 110
        self.life = 5
        self.frame = 0
        os.chdir("C:\\Users\\김민규\\Documents\\Github\\2DGP\\Drills\\Game Project\\Resources")
        if KimMuk.image == None:
            self.Run = load_image('Right_run.png')
            self.Jump = load_image("Jump_Right.png")
            self.Idle = load_image("Idle.png")
            self.Fall = load_image("Fall_down.png")

    def draw(self):
        self.frame = (self.frame + 1) % 4
        self.Idle.clip_draw(self.frame * 100, 0, 100, 200, self.x, self.y)
        delay(0.15)

    def jump(self):
        global Jump_Switch
        #self.Jump.clip_composite_draw(self.frame * 120, 0 , 120, 190, 3.141592 / 2, '' , self.x , self.y, 120, 190)
        self.Jump.clip_draw(self.frame * 120, 0, 120, 190, self.x, self.y)

        if (Jump_Switch == True):
            self.frame = (self.frame + 1) % 8
            self.y += 90 * math.sin(self.frame)

            if (self.x > 750):
                self.x1 += 20
            else:
                self.x += 20

            if (self.frame == 4):
                self.y += 25
                if (self.x > 750):
                    self.x1 += 40
                else:
                    self.x += 40
            elif(self.frame == 7):
                self.x += 15
                self.y -= 45
            if (self.frame == 0):
                self.y = 100
                Jump_Switch = False
            delay(0.06)

    def run(self):
        self.Run.clip_draw(self.frame * 110, 0, 110, 190, self.x, self.y)
        self.frame = (self.frame + 1) % 6
        if(self.x > 750 and self.x + self.x1 < 5000):
            self.x1 += 10
        elif( self.x + self.x1 < 5000):
            self.x +=10
        else:
            self.x += 10
        delay(0.03)

    def walk(self):
        pass

    def die(self):
        if self.life == 0:
            self.frame = (self.frame + 1) % 7
            self.Fall.clip_draw(self.frame * 200, 0, 200, 200, self.x, self.y)
            self.x -= 10
            delay(0.2)
            if self.frame == 0:
                e

    def update(self):
        pass

    def lives(self):
        if(self.life == 0):
            self.die()

class Background:
    def __init__(self):
        os.chdir("C:\\Users\\김민규\\Documents\\Github\\2DGP\\Drills\\Game Project\\Resources")
        self.image = load_image("BackGround_1.png")
    def draw(self):
        for i in range(0,5):
           self.image.draw(-2500 + 5000 * i - Right.x / 5 - Right.x1/5, 1000)

class Frontground:
    def __init__(self):
        os.chdir("C:\\Users\\김민규\\Documents\\Github\\2DGP\\Drills\\Game Project\\Resources")
        self.image = load_image("Grass.png")
    def draw(self):
        for i in range(0,5):
            self.image.draw(2500 * i - Right.x - Right.x1,1000)

class UI:
    def __init__(self):
        os.chdir("C:\\Users\\김민규\\Documents\\Github\\2DGP\\Drills\\Game Project\\Resources")
        self.life = load_image("Life.png")

    def Life(self):
        for i in range (0,Right.life):
            self.life.draw(100 + 50 * i, 800)

    def draw(self):
        self.Life()


def enter():
    global Right,Back,Front, Ui
    Ui = UI()
    Back = Background()
    Right = KimMuk()
    Front = Frontground()

def handle_events():
    events = get_events()
    global Jump_Switch
    global Run_Switch
    for event in events:
        if event.type == SDL_QUIT:
            pass
        if (event.type, event.key) == (SDL_KEYDOWN,SDLK_RIGHT):
            Run_Switch = True
        elif(event.type, event.key) == (SDL_KEYUP,SDLK_RIGHT):
            Run_Switch = False
        if(Jump_Switch == False):
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                Right.frame = 0
                Jump_Switch = True
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_l):
            Right.life -= 1

def exit():
    pass

def pause():
    pass

def resume():
    pass

def update():
    Right.update()

def draw():
    clear_canvas()
    Back.draw()
    if Right.life ==0:
        Right.die()
    else:
        if (Jump_Switch == True):
            Right.jump()
        elif (Run_Switch == True):
            Right.run()
            delay(0.01)
        else:
            Right.draw()


    Front.draw()
    Ui.draw()
    update_canvas()


enter()
