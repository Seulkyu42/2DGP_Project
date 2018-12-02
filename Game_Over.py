from pico2d import *
import os
import game_world
import main_state

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

class Start:
    def __init__(self):
        self.image1 = load_image("Start1.png")
        self.image2 = load_image("Start2.png")
        self.switch = 1
        self.x1 = -800
        self.x2 = 800

    def draw(self):
        if(self.switch == 1):
            self.image1.draw(801+self.x1,700)
            self.image2.draw(799+self.x2,700)
    def update(self):
        if(self.switch == 1 and self.x1 != 0 and self.x2 != 0):
            self.x1 += 2
            self.x2 -= 2


class Clear:
    def __init__(self):
        self.image = load_image("Clear.png")
        self.font1 = load_font('koverwatch.ttf', 60)
        self.alpha = 0
        self.y = 0

    def draw(self):
        self.image.opacify(self.alpha)
        self.image.draw(800,350 + self.y)
        if self.y > 300:
            self.font1.draw(600,500, 'Total Score : %d' % main_state.muk.Score, (255, 0, 0))

    def update(self):
        if(self.alpha < 1):
            self.alpha += 0.001
            self.y += 0.3