import math
from src.Figure import figure


class Circle(figure):
    NAME = "Circle"

    def __init__(self, r):
        self.r = r

    @property
    def perimetr(self):
        if self.r <= 0:
            return "raise ValueError"
        else:
            return self.r * 2 * math.pi

    @property
    def area(self):
        if self.r <= 0:
            return "raise ValueError"
        else:
            return self.r * 2 * math.pi

    def add_area(self, figure_2):
        if self.area == "raise ValueError" or figure_2 == "raise ValueError":
            return "raise ValueError"
        else:
            return self.area + figure_2.area


# b = Circle(0)
# a = Circle(4)
# print(a.area)
# print(b.area)
# print(b.perimetr)
