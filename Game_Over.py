from pico2d import *
import os
import game_world

os.chdir("C:\\Users\\김민규\\Documents\\Github\\2DGP_Project\\Resources")

class Over:
    def __init__(self):
        self.image = load_image("Over.png")
        self.alpha = 0
        self.y = 0

    def draw(self):
        self.image.opacify(self.alpha)
        self.image.draw(800,350 + self.y)

    def update(self):
        if(self.alpha < 1):
            self.alpha += 0.001
            self.y += 0.2
