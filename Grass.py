from pico2d import *
import os
import main_state

os.chdir("C:\\Users\\김민규\\Documents\\Github\\2DGP_Project\\Resources")

class Grass:
    def __init__(self):
        self.image = load_image('Ground_gray.png')

    def enter(self):
        pass

    def update(self):
        pass

    def draw(self):
        for i in range(0,5):
            self.image.draw(800 + 1600 * i - main_state.muk.x,400)