import math
from src.Figure import figure


class triangle(figure):
    Name = "Triangle"

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @property
    def perimeter(self):
        if (self.a + self.b) < self.c or (self.a + self.c) < self.b or (
                self.c + self.b) < self.a or self.a <= 0 or self.b <= 0 or self.c <= 0:
            return "raise ValueError"
        else:
            return self.a + self.b + self.c

    @property
    def area(self):
        if (self.a + self.b) < self.c or (self.a + self.c) < self.b or (
                self.c + self.b) < self.a or self.a <= 0 or self.b <= 0 or self.c <= 0:
            return "raise ValueError"
        else:
            p_tr_2 = (self.a + self.b + self.c) / 2
            return math.sqrt(p_tr_2 * (p_tr_2 - self.a) * (p_tr_2 - self.b) * (p_tr_2 - self.c))

    def add_area(self, figure_2):
        if self.area == "raise ValueError" or figure_2 == "raise ValueError":
            return "raise ValueError"
        else:
            return self.area + figure_2.area


# figure = triangle(3, 4, 5)
# figure_1 = triangle(2, 8, 8)
#
# print(figure.area)
# print(figure_1.area)
# print(figure.add_area(figure_1))
