from prop import Prop
from screen import Screen


class World:
    def __init__(self, apple_count, width, height, void_symbol="_", apple_symbol=".", human_symbol="@"):
        self.screen = Screen(width, height, void_symbol, apple_symbol, human_symbol)

        self.apple_count = int(
            apple_count if apple_count < self.screen.get_max_apples() else self.screen.get_max_apples() / 4)

        self.apple_arr = []
        self.human = Prop(self.screen.get_player_start_pos().x, self.screen.get_player_start_pos().y)
