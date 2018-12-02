import random
import json
import os

from pico2d import *
import Framework
import game_world

from Muk import Muk
from background import Back
from Grass import Grass
from Enemy import Monster1,Arrow,Hurdle_Up,Hurdle_Down,Box_Up,Thorn_Up
from Ui import Life
from Game_Over import Over

name = "MainState"

muk = None
back = None
grass = None
monster1 = None
arrow = None
life = None
over = None
hurdle_up = []
hurdle_down = []
box_up = []
thron =[]

j = 0

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b : return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True


def enter():
    global muk
    muk = Muk()
    game_world.add_object(muk, 1)

    global back
    back = Back()
    game_world.add_object(back, 0)

    global grass
    grass = Grass()
    game_world.add_object(grass,0)

    global monster1,arrow,hurdle_up,hurdle_down
    monster1 = Monster1()
    game_world.add_object(monster1, 2)

    #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    o1 = 1
    hurdle_up = [Hurdle_Up() for i in range(10)]
    for i in hurdle_up:
        i.x += 700 * o1
        o1 += 1
        game_world.add_object(i, 2)
    o2 = 1
    hurdle_down = [Hurdle_Down() for i in range(10)]
    for i in hurdle_down:
        i.x += 700 * o2
        o2 += 1
        game_world.add_object(i,2)

    #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    global box_up
    o3 = 1
    box_up = [Box_Up() for i in range(10)]
    for i in box_up:
        if(o3 % 2 == 0):
            i.x -= 200
        i.y += 700 * o3
        o3 += 1
        game_world.add_object(i, 2)
    #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    global thron
    o4 = 1
    thron = [Thorn_Up() for i in range(9)]
    for i in thron:
        if(o4 % 2 == 0):
            i.y -= 100
        i.x -= 700 * o4
        o4 += 1
        game_world.add_object(i, 2)
    #//////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    global life
    life = Life()
    game_world.add_object(life,4)

    global over
    over = Over()


def exit():
    game_world.clear()

def pause():
    pass

def resume():
    pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            Framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            Framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_r:
            global j
            exit()
            j = 0
            game_world.objects = [[],[],[],[],[]]
            enter()
            update()
        else:
            muk.handle_event(event)

def update():
    global muk,monster1,brick,hurdle_up,hurdle_down
    for game_object in game_world.all_objects():
        game_object.update()

    if collide(muk,monster1):
        muk.Damage_cnt = 1
        print("충돌")
        if(muk.Mode == 1):
            muk.x -= 100
        elif(muk.Mode == 3):
            muk.x += 100
        muk.Life -= 1
        monster1.cnt_frame = 7

        #game_world.remove_object(monster1)

    if (muk.Mode == 1):
        for ups in hurdle_up:
            for downs in hurdle_down:
                if collide(muk, ups):
                    muk.Damage_cnt = 1
                    muk.x -= 200
                    hurdle_up.remove(ups)
                    hurdle_down.remove(downs)
                    game_world.remove_object(ups)
                    game_world.remove_object(downs)
                    muk.Life -= 1
                elif collide(muk, downs):
                    muk.Damage_cnt = 1
                    muk.x -= 200
                    hurdle_up.remove(ups)
                    hurdle_down.remove(downs)
                    game_world.remove_object(ups)
                    game_world.remove_object(downs)
                    muk.Life -= 1

    elif (muk.Mode == 2):
        for ups in box_up:
            if collide(muk, ups):
                muk.Damage_cnt = 1
                muk.y -= 200
                box_up.remove(ups)
                game_world.remove_object(ups)
                muk.Life -= 1

    elif (muk.Mode == 3):
        for ups in thron:
            if collide(muk, ups):
                muk.Damage_cnt = 1
                muk.x += 200
                thron.remove(ups)
                game_world.remove_object(ups)
                muk.Life -= 1


    if(muk.Life < 1):
        global j
        j += 1
        if(j == 1):
            game_world.add_object(over, 4)


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()






