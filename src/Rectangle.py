from src.Figure import figure


class rectangle(figure):
    Name = "Rectangle"

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def perimetr(self):
        if self.a <= 0 or self.b <= 0:
            return "raise ValueError"
        else:
            return self.a * 2 + self.b * 2

    @property
    def area(self):
        if self.a <= 0 or self.b <= 0:
            return "raise ValueError"
        else:
            return self.a * self.b

    def add_area(self, figure_2):
        if self.area == "raise ValueError" or figure_2 == "raise ValueError":
            return "raise ValueError"
        else:
            return self.area + figure_2.area


# figure = rectangle(3, 4)
# figure_1 = rectangle(2, 8)
#
# print(figure.area)
# print(figure_1.area)
# print(figure.add_area(figure_1))
