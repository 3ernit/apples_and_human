from prop import Prop
from screen import Screen
import random


class World:
    def __init__(self, apple_count, width, height, void_symbol="_", apple_symbol=".", human_symbol="@"):
        self.screen = Screen(width, height, void_symbol, apple_symbol, human_symbol)

        self.apple_count = int(
            apple_count if (
                    apple_count < self.screen.get_max_apples() or apple_count > 0) else self.screen.get_max_apples() / 4)

        self.apple_arr = []
        self.create_apples()
        self.human = Prop(self.screen.get_player_start_pos().x, self.screen.get_player_start_pos().y)

    def create_apples(self):
        flag = True
        for i in range(self.apple_count):
            apple = Prop(0, 0)

            while flag:
                flag = False
                apple = Prop(
                    random.randrange(random.randrange(0, self.screen.width - 1)),
                    random.randrange(random.randrange(0, self.screen.height - 1)))
                if apple.pos.x == self.human.pos.x and apple.pos.y == self.human.pos.y:
                    flag = True
                    continue
                for a in range(len(self.apple_arr)):
                    if apple.pos.x == self.apple_arr[a].pos.x and apple.pos.y == self.apple_arr[a].pos.y:
                        flag = True
                        break

            self.apple_arr.append(apple)

    def screen_props(self):
        self.screen.clear()
        for i in range(len(self.apple_arr)):
            self.screen.display_prop(
                self.apple_arr[i].pos.x,
                self.apple_arr[i].pos.x,
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
                return True
        return False
