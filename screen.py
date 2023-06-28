from pos import Pos


class Screen:
    def __init__(self, width, height, void_symbol, apple_symbol, human_symbol):
        self.width = int(width) if int(width) > 2 else 2
        self.height = int(height) if int(height) > 2 else 2

        self.void_symbol = str(void_symbol)
        self.apple_symbol = str(apple_symbol)
        self.human_symbol = str(human_symbol)

        self.screen_arr = []
        self.clear()

    def get_max_apples(self):
        return self.width*self.height-1

    def get_player_start_pos(self):
        return Pos(int(self.width/2), int(self.height/2))

    def clear(self):
        self.screen_arr = []
        screen_line = ""
        for i in range(self.width):
            screen_line += self.void_symbol[0]
        for i in range(self.height):
            self.screen_arr.append(screen_line)

    def display_prop(self, x, y, prop=0):
        # 0 - void; 1 - apple; 2 - human
        split_1 = self.screen_arr[y][0:x]
        split_2 = self.screen_arr[y][x+1:len(self.screen_arr[y])]
        self.screen_arr[y] = split_1
        match prop:
            case 0:
                self.screen_arr[y] += self.void_symbol[0]
            case 1:
                self.screen_arr[y] += self.apple_symbol[0]
            case 2:
                self.screen_arr[y] += self.human_symbol[0]
        self.screen_arr[y] += split_2

    def get_str(self):
        result = ""
        for i in range(len(self.screen_arr)):
            result += self.screen_arr[i]
            if i < len(self.screen_arr) - 1:
                result += "\n"
        return result