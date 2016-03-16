from tkinter import*


class Field:
    class Block:
        def __init__(self, master: Canvas, x, y, x1, y1, fill):
            self.conf = [x, y, x1, y1]
            self.color = fill
            self.master = master
            self.index = None

        def draw(self):
            self.index = self.master.create_rectangle(self.conf, fill=self.color)

    class Ball:
        def __init__(self, master: Canvas, x, y, r, color):
            self.conf = [x-r, y-r, x+r, y+r]
            self.color = color
            self.master = master
            self.radius = r
            self.index = None

        def draw(self):
            self.index = self.master.create_oval(self.conf, fill=self.color)

    def __init__(self, master: Tk, height, width):
        self.master = master
        self.height = height
        self.width = width
        self.field = Canvas(self.master, height=self.height, width=self.width)
        self.field.pack(side="top")
        self.list_of_blocks = []
        self.player = None
        self.ball = None

# operation with block
    def create_block(self, x, y, x1, y1, fill):
        self.list_of_blocks.append(self.Block(self.field, x, y, x1, y1, fill))

    def delete_block(self, index):
        self.field.delete(self.list_of_blocks[index].index)
        self.list_of_blocks.pop(index)

# operation with player
    def create_player(self, x, y, x1, y1, fill):
        self.player = self.Block(self.field, x, y, x1, y1, fill)

    def delete_player(self):
        self.field.delete(self.player.index)

    def draw_player(self):
        self.player.draw()

    def move_left(self, step):
        self.field.move(self.player.index, step * (-1), 0)

    def move_right(self, step):
        self.field.move(self.player.index, step, 0)

# operation with ball
    def create_ball(self, x, y, radius, fill):
        self.ball = self.Ball(self.field, x, y, radius, fill)

    def delete_ball(self):
        self.field.delete(self.ball.index)

    def move_ball(self, xy):
        self.field.move(self.ball.index, xy[0], xy[1])

    def draw(self):
        for i in self.list_of_blocks:
            i.draw()
        self.player.draw()
        self.ball.draw()
        self.master.update()
