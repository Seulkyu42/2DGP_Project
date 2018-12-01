from pico2d import *
import os
import game_world

os.chdir("C:\\Users\\김민규\\Documents\\Github\\2DGP_Project\\Resources")

class Over:
    def __init__(self):
        self.image = load_image("Over.png")
        self.image2 = load_image("Over1.png")
        self.alpha = 0
        self.alpha2 = 0
        self.y = 0
        self.y2 = 0

    def draw(self):
        self.image.opacify(self.alpha)
        self.image.draw(800,350 + self.y)
        self.image2.opacify(self.alpha2)
        self.image2.draw(800,350 + self.y)

    def update(self):
        if(self.alpha < 1):
            self.alpha += 0.001
            self.y += 0.3
            if(self.y > 100):
                self.alpha2 += 0.001
                self.y2 += 0.1
