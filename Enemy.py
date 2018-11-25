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
        return self.x - 40 - main_state.muk.x, self.y - 75, self.x + 40 - main_state.muk.x , self.y + 50

    def draw(self):
        if main_state.muk.Mode == 1:
            self.image.clip_draw(int(self.frame) * 100, 0 , 100, 150, self.x - main_state.muk.x,self.y)
        elif main_state.muk.Mode == 2:
            self.image.clip_composite_draw(int(self.frame) * 100, 0, 100,150, 3.141492 / 2, '',self.x,self.y,100,150)
        elif main_state.muk.Mode == 3:
            self.image.clip_composite_draw(int(self.frame) * 100, 0, 100,150, 3.141492, '',self.x,self.y,100,150)
        elif main_state.muk.Mode == 4:
            self.image.clip_composite_draw(int(self.frame) * 100, 0, 100,150, -3.141492 / 2, '',self.x,self.y,100,150)

        draw_rectangle(*self.get_bb())


class Arrow:
    def __init(self):
        pass
