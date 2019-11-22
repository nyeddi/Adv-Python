class Shape(object):
    # this is an abstract class that is primarily used for inheritance defaults
    # here is where you would define classmethods that can be overridden by inherited classes
    @classmethod
    def from_square(cls, square):
        # return a default instance of cls
        return cls()

class Square(Shape):
    def __init__(self, side=10):
        self.side = side

    @classmethod
    def from_square(cls, square):
        return cls(side=square.side)


class Rectangle(Shape):
    def __init__(self, length=10, width=10):
        self.length = length
        self.width = width

    @classmethod
    def from_square(cls, square):
        return cls(length=square.side, width=square.side)


class RightTriangle(Shape):
    def __init__(self, a=10, b=10):
        self.a = a
        self.b = b
        self.c = ((a*a) + (b*b))**(.5)

    @classmethod
    def from_square(cls, square):
        return cls(a=square.side, b=square.side+2)


class Circle(Shape):
    def __init__(self, radius=10):
        self.radius = radius

    @classmethod
    def from_square(cls, square):
        return cls(radius=square.side/2)

class Circle1(Shape):
    def __init__(self, radius=10):
        self.radius = radius

    @staticmethod
    def from_square(square):
        return Circle1(radius=square.side/2)

class Hexagon(Shape):
    def __init__(self, side=10):
        self.side = side

#https://stackoverflow.com/questions/5738470/whats-an-example-use-case-for-a-python-classmethod
square = Square(3)
for polymorphic_class in (Square, Rectangle, RightTriangle, Circle, Hexagon):
    this_shape = polymorphic_class.from_square(square)
    print(this_shape.__class__)