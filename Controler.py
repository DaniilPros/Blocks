import View
import random
from tkinter import *
import tkinter.messagebox
import Model


class Game:
    def __init__(self, master: Tk, count: int):
        self.master, self.field = master, None
        self.area = Model.Field({'height': 900, 'width': 1000})
        self.field = View.Field(self.master, self.area['height'], self.area['width'])
        self.ball = Model.Ball(conf={'x': 400, 'y': 400, 'radius': 10})
        self.player = Model.Player(conf={'x': self.area['width'] - 550, 'y': self.area['height'] - 50, 'height': 50,
                                         'width': 200})
        self.blocks = self.create_blocks(count + 1 % 30)
        self.field_create()
        import time
        self.player['last_time'] = time.time()
        self.player['last_x'] = self.player['x']

    def field_create(self):
        self.field.create_player(self.player['x'],
                                 self.player['y'],
                                 self.player['x'] + self.player['width'],
                                 self.player['y'] + self.player['height'],
                                 "black")
        self.field.create_ball(self.ball['x'], self.ball['y'], self.ball['radius'], "red")
        for i in self.blocks:
            self.field.create_block(i['x'], i['y'], i['x'] + i['size'], i['y'] + i['size'], "red")

    def start(self):
        self.field.draw()
        self.__set_bind()
        self.move_ball()

    @staticmethod
    def __check(l: list, item: int):
        for i in l:
            if i == item:
                return False
        return True

    def create_blocks(self, count):
        l = []
        list_of_blocks = [Model.Block({'size': 100}) for i in range(0, count)]
        i = 0
        while i != count:
            j = random.randint(0, 30)
            if self.__check(l, j):
                l.append(j)
                x = (j % 10) * 100
                y = int(j % 3) * 100
                list_of_blocks[i]['x'] = x
                list_of_blocks[i]['y'] = y
                i += 1
        return list_of_blocks

    def move_right(self, step):
        if self.player['x'] + step + self.player['width'] < self.area['width']:
            self.player['last_x'] = self.player['x']
            self.player['x'] += step
            self.field.move_right(step)

    def move_left(self, step):
        if self.player['x'] - step >= 0:
            self.player['last_x'] = self.player['x']
            self.player['x'] -= step
            self.field.move_left(step)

    def move_ball(self):
        import time
        self.make_speed(time.time())
        if self.blocks .__len__() == 0:
            answer = tkinter.messagebox.askyesno("The End", "Close?")
            if answer:
                self.master.destroy()
                exit(0)
            else:
                return None
        if self.ball['x'] + self.ball['directions'][self.ball['direction']][0]\
                + self.ball['radius'] >= self.area['width'] \
                or self.ball['x'] + self.ball['directions'][self.ball['direction']][0]\
                - self.ball['radius'] <= 0:
            self.ball['direction'] = (self.ball['direction'][0] * (-1), self.ball['direction'][1])
        elif self.ball['y'] + self.ball['directions'][self.ball['direction']][1]\
                + self.ball['radius'] > self.area['height'] - self.player['height']+5:
            answer = tkinter.messagebox.askyesno("The End", "Close?")
            if answer:
                self.master.destroy()
                exit(0)
            else:
                return None
        elif self.check_collision_player() and self.ball['direction'][1] == 0:
            self.calculate_direction()
        elif not self.collision_blocks():
            if self.ball['y'] + self.ball['directions'][self.ball['direction']][1] - self.ball['radius'] <= 0:
                self.ball['direction'] = (self.ball['direction'][0], (self.ball['direction'][1] + 1) % 2)

        self.ball['y'] += self.ball['directions'][self.ball['direction']][1]
        self.ball['x'] += self.ball['directions'][self.ball['direction']][0]
        self.field.move_ball(self.ball['directions'][self.ball['direction']])
        self.master.after(self.ball['speed'], self.move_ball)

    def move_player(self, event):
        import math
        if self.player['x'] < event.x:
            self.move_right(math.fabs(self.player['x'] - event.x))
        else:
            self.move_left(math.fabs(self.player['x'] - event.x))

    def __set_bind(self):
        self.field.field.bind("<Motion>", lambda e: self.move_player(e))

    def check_collision_block(self, index):
        cx = [self.ball['x'] - self.ball['radius'], self.ball['x'] + self.ball['radius']]
        cy = [self.ball['y'] - self.ball['radius'], self.ball['y'] + self.ball['radius']]
        px = [self.blocks[index]['x'], self.blocks[index]['x'] + self.blocks[index]['size']]
        py = [self.blocks[index]['y'], self.blocks[index]['y'] + self.blocks[index]['size']]
        dx = None
        dy = None
        if px[0] <= cx[0] <= px[1]:
            dx = px[1]
        if px[0] <= cx[1] <= px[1]:
            dx = px[0]
        if dx is not None:
            if py[0] <= cy[0] <= py[1]:
                dy = py[1]
            if py[0] <= cy[1] <= py[1]:
                dy = py[0]
            if dy is not None:
                from math import pow
                if pow(dx-self.ball['x'], 2) + pow(dy-self.ball['y'], 2) <= pow(self.ball['radius'], 2):
                    return True
                return self.ball['radius'] <= self.blocks[index]['size'] or self.ball['radius'] <= self.blocks[index]['size']
        return False

    def collision_blocks(self):
        for i in range(0, self.blocks.__len__()):
            if self.check_collision_block(i):
                self.calculate_direction_hit_with_blocks(i)
                self.field.delete_block(i)
                self.blocks.pop(i)
                return True
        return False

    def check_collision_player(self):
        cx = [self.ball['x'] - self.ball['radius'], self.ball['x'] + self.ball['radius']]
        cy = [self.ball['y'] - self.ball['radius'], self.ball['y'] + self.ball['radius']]
        px = [self.player['x'], self.player['x'] + self.player['width']]
        py = [self.player['y'], self.player['y'] + self.player['height']]
        dx = None
        dy = None
        if px[0] <= cx[0] <= px[1]:
            dx = px[1]
        if px[0] <= cx[1] <= px[1]:
            dx = px[0]
        if dx is not None:
            if py[0] <= cy[0] <= py[1]:
                dy = py[1]
            if py[0] <= cy[1] <= py[1]:
                dy = py[0]
            if dy is not None:
                from math import pow
                if pow(dx-self.ball['x'], 2) + pow(dy-self.ball['y'], 2) <= pow(self.ball['radius'], 2):
                    return True
                return self.ball['radius'] <= self.player['height'] or self.ball['radius'] <= self.player['width']
        return False

    def make_speed(self, current_time):
        self.player['speed'] = int(((self.player['last_x'] - self.player['x']) /
                                    (current_time - self.player['last_time'])) * 100)
        if self.player['speed'] > 90:
            self.player['speed'] = 9
        elif self.player['speed'] < -90:
            self.player['speed'] = -9
        else:
            self.player['speed'] = int(self.player['speed'] / 10)

    def calculate_direction(self):
        if self.ball['direction'][0] - self.player['speed'] > 9:
            self.ball['direction'] = (9, (self.ball['direction'][1] + 1) % 2)
        elif self.ball['direction'][0] - self.player['speed'] < -9:
            self.ball['direction'] = (-9, (self.ball['direction'][1] + 1) % 2)
        else:
            self.ball['direction'] = (self.ball['direction'][0] - self.player['speed'],
                                      (self.ball['direction'][1] + 1) % 2)

    def determine_side(self, index: int):
        import math
        d = self.ball['radius']/math.sqrt(2)
        l = [(self.blocks[index]['x'] - d, self.blocks[index]['y'] - d),
             (self.blocks[index]['x'] + self.blocks[index]['size'] + d, self.blocks[index]['y'] - d),
             (self.blocks[index]['x'] + self.blocks[index]['size'] + d, self.blocks[index]['y'] + self.blocks[index]['size'] + d),
             (self.blocks[index]['x'] - d, self.blocks[index]['y'] + self.blocks[index]['size'] + d)]
        if (self.ball['x'], self.ball['y']) in l:
            return 1
        if self.ball['x'] < self.blocks[index]['x'] - d or \
                self.ball['x'] > self.blocks[index]['x'] + self.blocks[index]['size'] + d:
            return 2
        return 3

    def calculate_direction_hit_with_blocks(self, index):
        var = self.determine_side(index)
        if var == 1:
            self.ball['direction'] = (self.ball['direction'][0]*(-1), (self.ball['direction'][1] + 1) % 2)
        elif var == 2:
            self.ball['direction'] = (self.ball['direction'][0] * (-1), (self.ball['direction'][1]))
        else:
            self.ball['direction'] = (self.ball['direction'][0], (self.ball['direction'][1] + 1) % 2)
