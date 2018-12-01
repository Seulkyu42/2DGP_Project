import Framework
from pico2d import *
import os
import Game_Over

os.chdir("C:\\Users\\김민규\\Documents\\Github\\2DGP_Project\\Resources")

PIXEL_PER_METER = (10.0/0.3)
RUN_SPEED_KMPH = 90.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

Jump_Height = 15.0

TIME_PER_ACTION = 1.0
ACTION_PER_TIME = 1.5
Frame_Idle = 4
Frame_Run = 6
Frame_Jump = 8
Frame_Down = 7

RIGHT_DOWN, RIGHT_UP, SPACE,Mode1,Mode2,Mode3,Mode4, Down = range(8)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RIGHT_DOWN,
    (SDL_KEYUP, SDLK_RIGHT): RIGHT_UP,
    (SDL_KEYDOWN, SDLK_SPACE): SPACE,
    (SDL_KEYDOWN, SDLK_1): Mode1,
    (SDL_KEYDOWN, SDLK_2): Mode2,
    (SDL_KEYDOWN, SDLK_3): Mode3,
    (SDL_KEYDOWN, SDLK_4): Mode4,
}

# X와 Cam X 를 구분한 이유 : 카메라는 중심고정 X는 계속 진행이기 때문

class IdleState:
    @staticmethod
    def enter(muk, event):
        if event == RIGHT_DOWN:
            muk.velocity += RUN_SPEED_PPS
        elif event == RIGHT_UP:
            muk.velocity -= RUN_SPEED_PPS


    @staticmethod
    def exit(muk, event):
        pass

    @staticmethod
    def do(muk):
        muk.frame = (muk.frame + Frame_Idle * ACTION_PER_TIME * Framework.frame_time) % 4

    @staticmethod
    def draw(muk):
        if muk.Mode == 1:
            muk.Idle_image.clip_draw(int(muk.frame) * 100, 0, 100, 200, muk.camx, muk.camy)
        elif muk.Mode == 2:
            muk.Idle_image.clip_composite_draw(int(muk.frame) * 100, 0, 100, 200, 3.141492 / 2, '', muk.camx, muk.camy, 100,200)
        elif muk.Mode == 3:
            muk.Idle_image.clip_composite_draw(int(muk.frame) * 100, 0, 100, 200, 3.141492, '', muk.camx, muk.camy, 100, 200)
        elif muk.Mode == 4:
            muk.Idle_image.clip_composite_draw(int(muk.frame) * 100, 0, 100, 200, -3.141492 / 2, '', muk.camx, muk.camy, 100,200)

class RunState:
    @staticmethod
    def enter(muk, event):
        if event == RIGHT_DOWN:
            muk.velocity += RUN_SPEED_PPS
        elif event == RIGHT_UP:
            muk.velocity -= RUN_SPEED_PPS


    @staticmethod
    def exit(muk, event):
        if muk.Mode == 1:
            muk.y = 90

    @staticmethod
    def do(muk):
        muk.Score += muk.frame / 8
        if muk.Mode == 1:
            muk.frame = (muk.frame + Frame_Run * ACTION_PER_TIME * Framework.frame_time) % 6
            muk.x += muk.velocity * Framework.frame_time
            muk.camx += muk.velocity * Framework.frame_time
            if(muk.x > 750 and muk.x < 8400): #750 : X중심
                muk.camx = 750
        elif muk.Mode == 2:
            muk.frame = (muk.frame + Frame_Run * ACTION_PER_TIME * Framework.frame_time) % 6
            muk.y += muk.velocity * Framework.frame_time
            muk.camy += muk.velocity * Framework.frame_time
            if (muk.y > 400 and muk.y < 8400): #400 : Y중심
                muk.camy = 400
        elif muk.Mode == 3:
            muk.frame = (muk.frame + Frame_Run * ACTION_PER_TIME * Framework.frame_time) % 6
            muk.x -= muk.velocity * Framework.frame_time
            muk.camx -= muk.velocity * Framework.frame_time
            if(muk.x > 750 and muk.x < 8400): #750 : X중심
                muk.camx = 750
        elif muk.Mode == 4:
            muk.frame = (muk.frame + Frame_Run * ACTION_PER_TIME * Framework.frame_time) % 6
            muk.y -= muk.velocity * Framework.frame_time
            muk.camy -= muk.velocity * Framework.frame_time
            if (muk.y > 400 and muk.y < 8400): #400 : Y중심
                muk.camy = 350

        if muk.Mode == 1 or muk.Mode == 3:
            muk.x = clamp(0, muk.x, 9000)
            muk.camx = clamp(0,muk.camx,1550)

        if muk.Mode == 2 or muk.Mode == 4:
            muk.y = clamp(0, muk.y, 9000)
            muk.camy = clamp(0, muk.camy, 850)

    @staticmethod
    def draw(muk):
        if muk.Mode == 1:
            muk.Run_image.clip_draw(int(muk.frame) * 110, 0, 110, 200, muk.camx, muk.camy)
        elif muk.Mode == 2:
            muk.Run_image.clip_composite_draw(int(muk.frame) * 110, 0, 110, 200, 3.141492 / 2, '', muk.camx, muk.camy, 110,200)
        elif muk.Mode == 3:
            muk.Run_image.clip_composite_draw(int(muk.frame) * 110, 0, 110, 200, 3.141492, '', muk.camx, muk.camy, 110, 200)
        elif muk.Mode == 4:
            muk.Run_image.clip_composite_draw(int(muk.frame) * 110, 0, 110, 200, -3.141492 / 2, '', muk.camx, muk.camy, 110,200)

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

class JumpState:
    @staticmethod
    def enter(muk, event):
        muk.velocity = RUN_SPEED_PPS
        muk.jump_frame = 1

    @staticmethod
    def exit(muk, event):
        if (event != SPACE):
            muk.jump_frame = 0
            if muk.Mode == 1:
                muk.y = 90
                muk.camy = 90
            if muk.Mode == 2:
                muk.x = 9500
                muk.camx = 1500

    @staticmethod
    def do(muk):
        print('%d', muk.jump_frame)
        if muk.Mode == 1:
            muk.jump_frame = (muk.jump_frame + Frame_Jump * ACTION_PER_TIME * Framework.frame_time) % 7
            muk.x += muk.velocity * Framework.frame_time
            muk.y += Jump_Height * -math.cos(muk.jump_frame + 1)

            muk.camx += muk.velocity * Framework.frame_time
            muk.camy += Jump_Height * -math.cos(muk.jump_frame + 1)

            if(muk.x > 750 and muk.x < 8400): #750 : X중심
                muk.camx = 750

            if(int(muk.jump_frame) == 0):
                muk.camy = 90
                muk.y = 90

            if(muk.x > 8500 and muk.jump_frame > 5):
                print("되는데??")
                muk.Life += 1
                muk.x = 9500
                muk.camx, muk.camy = 1500, 75
                muk.add_event(Mode2)
                muk.Mode = 2

        elif muk.Mode == 2:
            muk.jump_frame = (muk.jump_frame + Frame_Jump * ACTION_PER_TIME * Framework.frame_time) % 8
            muk.x -= Jump_Height * -math.cos(muk.jump_frame + 1)
            muk.y += muk.velocity * Framework.frame_time * 3

            muk.camx -= Jump_Height * -math.cos(muk.jump_frame + 1)
            muk.camy += muk.velocity * Framework.frame_time * 3

            if(muk.y > 400 and muk.y < 8400):
                muk.camy = 400

            if(int(muk.jump_frame) == 0):
                muk.x = 9500
                muk.camx = 1500

            if (muk.y > 8500 and muk.jump_frame > 5):
                muk.Life += 1
                muk.x = 9500
                muk.camx, muk.camy = 1500, 800
                muk.add_event(Mode3)
                muk.Mode = 3

        elif muk.Mode == 3:
            muk.jump_frame = (muk.jump_frame + Frame_Jump * ACTION_PER_TIME * Framework.frame_time) % 8
            muk.x -= muk.velocity * Framework.frame_time * 2
            muk.y -= Jump_Height * -math.cos(muk.jump_frame + 1)

            muk.camx -= muk.velocity * Framework.frame_time * 2
            muk.camy -= Jump_Height * -math.cos(muk.jump_frame + 1)

            if(muk.x > 750 and muk.x < 8400): #750 : X중심
                muk.camx = 750

            if(int(muk.jump_frame) == 0):
                muk.y = 750
                muk.camy = 750

        elif muk.Mode == 4:
            muk.jump_frame = (muk.jump_frame + Frame_Jump * ACTION_PER_TIME * Framework.frame_time) % 8
            muk.y -= muk.velocity * Framework.frame_time * 3
            muk.x += Jump_Height * -math.cos(muk.jump_frame + 1)

            muk.camy -= muk.velocity * Framework.frame_time * 3
            muk.camx += Jump_Height * -math.cos(muk.jump_frame + 1)

            if(muk.y > 350 and muk.y < 8400):
                muk.camy = 350

            if(int(muk.jump_frame) == 0):
                muk.x = 100
                muk.camx = 100

        if muk.Mode == 1 or muk.Mode == 3:
            muk.x = clamp(0, muk.x, 9000)

        if (int(muk.jump_frame) == 0):
            if(muk.Mode == 1):
                muk.y = 90
            elif(muk.Mode == 2):
                muk.x = 9500
            muk.add_event(RIGHT_DOWN)

 # ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    @staticmethod
    def draw(muk):
        if muk.Mode == 1:
            muk.Jump_image.clip_draw(int(muk.jump_frame) * 120, 0, 120, 190, muk.camx, muk.camy)
        elif muk.Mode == 2:
            muk.Jump_image.clip_composite_draw(int(muk.jump_frame) * 120, 0, 120, 190, 3.141492 / 2, '', muk.camx, muk.camy, 120, 190)
        elif muk.Mode == 3:
            muk.Jump_image.clip_composite_draw(int(muk.jump_frame) * 120, 0, 120, 190, 3.141492, '', muk.camx, muk.camy, 120, 190)
        elif muk.Mode == 4:
            muk.Jump_image.clip_composite_draw(int(muk.jump_frame) * 120, 0, 120, 190, -3.141492 / 2, '', muk.camx, muk.camy, 120,190)

class DownState:
    @staticmethod
    def enter(muk, event):
        pass

    @staticmethod
    def exit(muk, event):
        pass

    @staticmethod
    def do(muk):
        if(muk.frame < 8):
            muk.frame = (muk.frame + Frame_Down * ACTION_PER_TIME * Framework.frame_time / 2)
            if muk.Mode == 1:
                muk.camx -= 5
                clamp(0, muk.camx, 9000)
            elif muk.Mode == 2:
                muk.camy -= 5
                clamp(0, muk.y, 9000)
            elif muk.Mode == 3:
                muk.camx += 5
                clamp(0, muk.camx, 9000)
            elif muk.Mode == 4:
                muk.camy += 5
                clamp(0, muk.y, 9000)

    @staticmethod
    def draw(muk):
        if muk.Mode == 1:
            muk.Down_image.clip_draw(int(muk.frame) * 200, 0, 200, 200, muk.camx, 90)
        elif muk.Mode == 2:
            muk.Down_image.clip_composite_draw(int(muk.frame) * 200, 0, 200, 200, 3.141492 / 2, '', muk.camx, muk.camy, 200,200)
        elif muk.Mode == 3:
            muk.Down_image.clip_composite_draw(int(muk.frame) * 200, 0, 200, 200, 3.141492, '', muk.camx, muk.camy, 200, 200)
        elif muk.Mode == 4:
            muk.Down_image.clip_composite_draw(int(muk.frame) * 200, 0, 200, 200, -3.141492 / 2, '', muk.camx, muk.camy, 200,200)


next_state_table = {
    IdleState: {RIGHT_UP: IdleState, RIGHT_DOWN: RunState, SPACE: JumpState,
                Mode1: IdleState, Mode2: IdleState, Mode3: IdleState, Mode4: IdleState , Down : DownState},
    RunState: {RIGHT_UP: IdleState, RIGHT_DOWN: IdleState, SPACE: JumpState,
                Mode1 : RunState,Mode2 : RunState,Mode3 : RunState,Mode4 : RunState , Down : DownState},
    JumpState: {RIGHT_UP: JumpState, RIGHT_DOWN: RunState, SPACE: JumpState,
               Mode1: IdleState, Mode2: IdleState, Mode3: IdleState, Mode4: IdleState , Down : DownState},
    DownState: {RIGHT_UP: DownState, RIGHT_DOWN: DownState, SPACE: DownState,
               Mode1: DownState, Mode2: DownState, Mode3: DownState, Mode4: DownState , Down : DownState}
}

class Muk:
    def __init__(self):
        self.x, self.y = 0, 90
        self.camx = 0  #camera_x
        self.camy = 90  #camera_y
        self.Idle_image = load_image("Idle.png")
        self.Run_image = load_image("Right_run.png")
        self.Jump_image = load_image("Jump_Right.png")
        self.Down_image = load_image("Fall_down.png")
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.jump_frame = 0
        self.font1 = load_font('koverwatch.ttf', 40)
        self.font2 = load_font('koverwatch.ttf', 20)

        self.Mode = 1
        self.Life = 5
        self.Score = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def get_bb(self):
        if self.Mode == 1 or self.Mode == 3:
            return self.camx - 50, self.camy - 100, self.camx + 50, self.camy + 100
        elif self.Mode == 2 or self.Mode == 4:
            return self.camx - 100, self.camy - 50, self.camx + 100, self.camy + 50

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)
        if(self.Life < 1):
            self.event_que.insert(0,Down)

    def draw(self):
        self.cur_state.draw(self)
        self.font2.draw(self.camx - 55, self.camy + 110, 'X : %d' % self.x, (255, 0, 0))
        self.font2.draw(self.camx - 55, self.camy + 130, 'Y : %d' % self.y, (255, 0, 0))
        self.font1.draw(1200,840, 'Total Score : %d' % self.Score, (255, 0, 0))
        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

