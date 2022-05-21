from abc import ABC, ABCMeta, abstractmethod


class Shape(ABC):
    block = "\u00b7"

    @abstractmethod
    def draw(self):
        pass

    @property
    @abstractmethod
    def area(self):
        pass

    @classmethod
    @abstractmethod
    def sides(cls):
        raise NotImplementedError


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self):
        for _ in range(self.height):
            print(self.block * self.width)

    @property
    def area(self):
        return self.width * self.height

    @classmethod
    def sides(cls):
        return 4


rect = Rectangle(5, 4)
print(rect.sides())
print(rect.area)
rect.draw()
