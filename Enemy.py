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
        self.cnt_frame1 = 0
        self.cnt_frame2 = 7


    def update(self):
        self.frame = (self.frame + Frame_Monster1 * ACTION_PER_TIME * Framework.frame_time) % 8
        if(main_state.muk.Mode == 1):
            self.count += 1
            if (self.count == 250 and self.cnt_frame1 < 5):
                self.cnt_frame1 += 1
                self.count = 0
        elif(main_state.muk.Mode == 3):
            self.count+=1
            if (self.count == 250 and self.cnt_frame2 < 10):
                self.cnt_frame2 += 1
                self.count = 0


    def get_bb(self):
        if main_state.muk.Mode == 1:
            return self.x - 40 - main_state.muk.x, self.y - 75, self.x + 40 - main_state.muk.x , self.y + 50
        else:
            return 9000 - 40 - main_state.muk.x, 800 - 75, 9000 + 40 - main_state.muk.x, 800 + 50

    def draw(self):
        if main_state.muk.Mode == 1:
            self.text.clip_draw(0,500 - self.cnt_frame1 * 50,200,50, 100 + self.x-main_state.muk.x,self.y + 75)
            self.image.clip_draw(int(self.frame) * 100, 0 , 100, 150, self.x - main_state.muk.x,self.y)
        if main_state.muk.Mode == 3:
            self.text.clip_composite_draw(0, 500 - self.cnt_frame2 * 50, 200, 50,3.14,'', -100 +  9000 - main_state.muk.x, 800 - 150,200,50)
            self.image.clip_composite_draw(int(self.frame) * 100, 0, 100, 150,3.14,'', 9000 - main_state.muk.x, 800, 100,300)

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

    def update(self):
        pass;
    def draw(self):
        if (main_state.muk.Mode == 1):
            self.image.clip_composite_draw(1,0,200,350,0,'',self.x - main_state.muk.x ,self.y,200,350)
        # draw_rectangle(*self.get_bb())

    def get_bb(self):
        if (main_state.muk.Mode == 1):
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
        if(main_state.muk.Mode == 1):
            return self.x - 5 - main_state.muk.x, self.y + 30, self.x + 5 - main_state.muk.x , self.y + 1000

class Box_Up:

    image = None
    Dx, Dy = 0, 0

    def __init__(self):
        if Box_Up.image == None:
            Box_Up.image = load_image('Hurdle2.png')
        self.x, self.y = 1400, 1500
        Box_Up.Dx = self.x
        Box_Up.Dy = self.y

    def update(self):
        pass;

    def draw(self):
        if (main_state.muk.Mode == 2):
            self.image.clip_composite_draw(1, 0, 200, 350, 3.14 / 2, '', self.x, self.y - main_state.muk.y, 200, 350)
            #draw_rectangle(*self.get_bb())

    def get_bb(self):
        if (main_state.muk.Mode == 2):
            return self.x , self.y - main_state.muk.y - 30, self.x + 150, self.y - main_state.muk.y + 30

class Thorn_Up:

    image = None
    Dx, Dy = 0, 0

    def __init__(self):
        if Thorn_Up.image == None:
            Thorn_Up.image = load_image('Hurdle3.png')
        self.x, self.y = 8000, 800
        Thorn_Up.Dx = self.x
        Thorn_Up.Dy = self.y

    def update(self):
        pass;

    def draw(self):
        if (main_state.muk.Mode == 3):
            self.image.clip_draw(1, 0, 200, 350, self.x - main_state.muk.x , self.y, 200, 350)
            draw_rectangle(*self.get_bb())

    def get_bb(self):
        #if (main_state.muk.Mode == 3):
        return self.x - 20 -main_state.muk.x, self.y - 75, self.x + 20-main_state.muk.x, self.y + 100
