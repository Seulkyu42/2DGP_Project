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
        for i in range(0,20):
            if main_state.muk.Mode == 1:
                self.image.composite_draw(3.14 / 2,'',10150 - main_state.muk.x, 450 + 900 * i - main_state.muk.y)
                self.image.draw( 1600 * i - main_state.muk.x,400)
            if main_state.muk.Mode == 2:
                self.image.composite_draw(3.14 / 2,'',10150, 450 + 900 * i - main_state.muk.y)
                self.image.draw( 1600 * i - main_state.muk.x,400-main_state.muk.y)
                self.image.composite_draw(3.14, '', 1600, 10150 - main_state.muk.y)
            #self.image.composite_draw(3.14,'',1600 * i - main_state.muk.x,500)
            #self.image.composite_draw(-3.14 / 2,'',400, 450 + 900 * i - main_state.muk.y)