from prop import Prop
from screen import Screen
from math import sqrt
from numpy import random


class World:
    def __init__(self, apple_count, width, height, void_symbol=".", apple_symbol="*", human_symbol="@"):
        self.screen = Screen(width, height, void_symbol, apple_symbol, human_symbol)

        self.apple_count = int(
            apple_count if (
                    apple_count < self.screen.get_max_apples() or apple_count > 0) else self.screen.get_max_apples() / 4)

        self.apple_arr = []
        self.human = Prop(self.screen.get_player_start_pos().x, self.screen.get_player_start_pos().y)
        self.create_apples()

    def create_apples(self):
        for i in range(self.apple_count):
            apple = Prop(0, 0)
            flag = True

            while flag:
                flag = False
                apple = Prop(
                    random.randint(0, self.screen.width),
                    random.randint(0, self.screen.height))
                for banana in self.apple_arr:
                    if apple.pos.x == banana.pos.x or apple.pos.y == banana.pos.y:
                        flag = True
                if apple.pos.x == self.human.pos.x and apple.pos.y == self.human.pos.y:
                    flag = True

            self.apple_arr.append(apple)

    def screen_props(self):
        self.screen.clear()
        for i in range(len(self.apple_arr)):
            self.screen.display_prop(
                self.apple_arr[i].pos.x,
                self.apple_arr[i].pos.y,
                1
            )
        self.screen.display_prop(
            self.human.pos.x,
            self.human.pos.y,
            2
        )

    def is_collide(self):
        for i in range(len(self.apple_arr)):
            if self.human.pos.x == self.apple_arr[i].pos.x and self.human.pos.y == self.apple_arr[i].pos.y:
                del self.apple_arr[i]
                return True
        return False

    def get_apples_distance(self):
        distances = []
        for i in range (len(self.apple_arr)):
            dis = sqrt((self.apple_arr[i].pos.x - self.human.pos.x)**2+(self.apple_arr[i].pos.x - self.human.pos.x)**2)
            distances.append(dis)
        return distances

    def border(self):
        if self.human.pos.x < 0:
            self.human.pos.x = 0
        if self.human.pos.y < 0:
            self.human.pos.y = 0
        if self.human.pos.x > self.screen.width - 1:
            self.human.pos.x = self.screen.width - 1
        if self.human.pos.y > self.screen.height - 1:
            self.human.pos.y = self.screen.height - 1
