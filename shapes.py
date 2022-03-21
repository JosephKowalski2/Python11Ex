class Rectangle:
    def __init__(self, length, width):
        self.width = width
        self.length = length

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return (2 * self.length) + (2 * self.width)


class Square(Rectangle):
    def __init__(self, side):
        self.length = side
        self.width = side



