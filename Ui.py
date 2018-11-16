from pico2d import *
import os
import main_state

os.chdir("C:\\Users\\김민규\\Documents\\Github\\2DGP_Project\\Resources")

class Life:
    def __init__(self):
        self.image = load_image('Life.png')

    def enter(self):
        pass

    def update(self):
        pass

    def draw(self):
        for i in range(0, main_state.muk.Life):
            if main_state.muk.Mode == 1:
                self.image.draw(100 + 50 * i, 850)
            elif main_state.muk.Mode == 2:
                self.image.composite_draw(3.14/2,'',50,100 + 50 * i)
            elif main_state.muk.Mode == 3:
                self.image.composite_draw(3.14,'',1500 - 50 * i, 50)
            elif main_state.muk.Mode == 4:
                self.image.composite_draw(3.14/2,'',1550,800 - 50 * i)