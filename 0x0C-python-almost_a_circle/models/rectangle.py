#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        return self.width * self.height

    def display(self):
        print("\n" * int(self.y), end="")
        for col in range(self.height):
            print(" " * int(self.x), end="")
            for row in range(self.width):
                print("#", end="")
            print("")

    def __str__(self):
        t = "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"
        return t.format(self.id, self.__x, self.__y, self.__width, self.height)

    def update(self, *args, **kwargs):
        attrs = ["id", "width", "height", "x", "y"]

        for arg in range(len(args)):
            for attr in range(len(attrs)):
                setattr(self, attrs[attr], args[arg])

        if kwargs is None:
            pass
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
