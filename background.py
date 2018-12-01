from pico2d import *
import os
import game_world
import main_state
os.chdir("C:\\Users\\김민규\\Documents\\Github\\2DGP_Project\\Resources")

class Back:
    def __init__(self):
        self.image = load_image('BackGround_1.png')
        #self.image2 = load_image('BackGround_2.png')

    def update(self):
        pass

    def draw(self):
        for i in range(0,30):
            for j in range(0,30):
                #self.image2.draw(600 * i - main_state.muk.x, 300 * j - main_state.muk.y)
                self.image.draw(600 * i - main_state.muk.x / 2, 300 * j - main_state.muk.y / 2)

