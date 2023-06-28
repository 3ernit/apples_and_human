from pos import Pos


class Prop:
    def __init__(self, x, y):
        self.pos = Pos(x, y)

    def move(self, x_speed, y_speed):
        self.pos.x += int(x_speed)
        self.pos.y += int(y_speed)
