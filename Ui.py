from pico2d import *
import os
import main_state

os.chdir("C:\\Users\\김민규\\Documents\\Github\\2DGP\\Drills\\Game Project\\Resources")


class Life:
    def __init__(self):
        self.image = load_image('Life.png')

    def enter(self):
        pass

    def update(self):
        pass

    def draw(self):
        for i in range(0, main_state.muk.Life):
            self.image.draw(100 + 50 * i, 850)
