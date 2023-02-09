from datetime import date


class Cell:
    def __init__(self, value: str) -> None:
        self.__value = value
        self.__color = 'white'

    def set_value(self, value):
        self.__value = str(value)

    def get_value(self):
        return self.__value

    def set_color(self, color):
        colors = {1: 'black', 2: 'red', 3: 'blue', 4: 'green', 5: 'yellow', 0: 'white'}
        if color in colors:
            self.__color = colors[color]
        else:
            print('Color not found')

    def get_color(self):
        return self.__color

    def to_int(self):
        return int(self.__value)

    def to_float(self):
        return float(self.__value)

    def to_date(self):
        try:
            date(int(self.__value[:4]), int(self.__value[5:7]), int(self.__value[8:]))
        except:
            print("It's not date")

    def reset(self):
        self.__value = ''
