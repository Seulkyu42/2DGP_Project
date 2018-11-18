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
    def __init__(self):
        if Monster1.image == None:
            Monster1.image = load_image('Monster1.png')
        self.x,self.y = random.randint(0,1600), 50
        self.frame = 0

    def update(self):
        self.frame = (self.frame + Frame_Monster1 * ACTION_PER_TIME * Framework.frame_time) % 8

    def get_bb(self):
        return self.x - 40 - main_state.muk.x / 2, self.y - 75, self.x + 40 - main_state.muk.x / 2, self.y + 50

    def draw(self):
        self.image.clip_draw(int(self.frame) * 100, 0 , 100, 150, self.x - main_state.muk.x / 2,self.y)
        draw_rectangle(*self.get_bb())

class Brick:
    def __init__(self):
        self.x = 3400
        self.y = 0

    def update(self):
        pass

    def get_bb(self):
        return self.x - 10 - main_state.muk.x / 2, self.y,self.x + 10 - main_state.muk.x / 2, self.y + 600

    def draw(self):
        draw_rectangle(*self.get_bb())