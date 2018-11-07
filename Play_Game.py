import Framework
import pico2d

import main_state

pico2d.open_canvas(1600, 900)
Framework.run(main_state)
pico2d.close_canvas()