import random
from pico2d import *
import game_world
import Framework
import os
import main_state

os.chdir("C:\\Users\\김민규\\Documents\\Github\\2DGP_Project\\Resources")

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 0.5
Frame_Monster1 = 8

class Monster1:
    image = None
    text = None
    def __init__(self):
        if Monster1.image == None:
            Monster1.image = load_image('Monster1.png')
        if Monster1.text == None:
            Monster1.text = load_image('Text.png')
        self.x,self.y = 700, 50
        self.frame = 0
        self.count = 0
        self.cnt_frame = 0

    def update(self):
        self.frame = (self.frame + Frame_Monster1 * ACTION_PER_TIME * Framework.frame_time) % 8
        self.count += 1
        if(self.count  == 250 and self.cnt_frame < 5):
            self.cnt_frame += 1
            self.count = 0


    def get_bb(self):
        return self.x - 40 - main_state.muk.x, self.y - 75, self.x + 40 - main_state.muk.x , self.y + 50

    def draw(self):
        self.text.clip_draw(0,350 - self.cnt_frame * 50,200,50, 100 + self.x-main_state.muk.x,self.y + 75)
        if main_state.muk.Mode == 1:
            self.image.clip_draw(int(self.frame) * 100, 0 , 100, 150, self.x - main_state.muk.x,self.y)
        #draw_rectangle(*self.get_bb())


class Arrow:
    def __init(self):
        pass

class Hurdle_Up:
    image = None
    Dx,Dy = 0,0
    def __init__(self):
        if Hurdle_Up.image == None:
            Hurdle_Up.image = load_image('Hurdle1.png')
        self.x,self.y = 1500, 350
        Hurdle_Up.Dx = self.x
        Hurdle_Up.Dy = self.y

        self.frame = 0

    def update(self):
        pass;
    def draw(self):
        self.image.clip_composite_draw(1,0,200,350,0,'',self.x - main_state.muk.x ,self.y,200,350)
        #draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 5 - main_state.muk.x, self.y - 350, self.x + 5 - main_state.muk.x , self.y - 200

class Hurdle_Down:
    def __init__(self):
        self.x = Hurdle_Up.Dx
        self.y = Hurdle_Up.Dy + 170
    def update(self):
        pass
    def draw(self):
        pass
        #draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 5 - main_state.muk.x, self.y + 30, self.x + 5 - main_state.muk.x , self.y + 1000
