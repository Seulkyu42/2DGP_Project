from pico2d import *
import os
import game_world

os.chdir("C:\\Users\\김민규\\Documents\\Github\\2DGP_Project\\Resources")

class Back:
    def __init__(self):
        self.image = load_image('BackGround_1.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(800,450)

