from src.Figure import figure


class square(figure):
    Name = "Square"

    def __init__(self, a):
        self.a = a

    @property
    def perimetr(self):
        if self.a <= 0:
            return "raise ValueError"
        else:
            return self.a * 4

    @property
    def area(self):
        if self.a <= 0:
            return "raise ValueError"
        else:
            return self.a ** 2

    def add_area(self, figure_2):
        if self.area == "raise ValueError" or figure_2 == "raise ValueError":
            return "raise ValueError"
        else:
            return self.area + figure_2.area


# figure = square(5)
# figure_1 = square(4)
#
# print(figure.area + figure_1.area)
# print(figure.add_area(figure_1))
