from pico2d import *
import os
import game_world

os.chdir("C:\\Users\\김민규\\Documents\\Github\\2DGP_Project\\Resources")

class Back:
    def __init__(self):
        self.image = load_image('Trees.png')

    def update(self):
        pass

    def draw(self):
        for i in range(0, 2):
            self.image.draw(-2500 + 5000 * i, 1000)
