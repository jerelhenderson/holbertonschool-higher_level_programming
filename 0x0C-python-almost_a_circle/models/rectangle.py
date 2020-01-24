#!/usr/bin/python3
"""
Module: Rectangle
rectangle.py - rectangle-specific that may be inherited by other classes
"""
from models.base import Base


class Rectangle(Base):
    """ Class 'Rectangle' inherits from Class 'Base' """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initialization method """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ 'widith' attribute getter """
        return self.__width

    @width.setter
    def width(self, value):
        """ 'width' attribute setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ 'height' attribute getter """
        return self.__height

    @height.setter
    def height(self, value):
        """ 'height' attribute setter """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ 'x' attribute getter """
        return self.__x

    @x.setter
    def x(self, value):
        """ 'x' attribute setter """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        """ 'y' attribute getter """
        return self.__y

    @y.setter
    def y(self, value):
        """ 'y' attribute getter """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        """ 'area' of Rectangle """
        return self.width * self.height

    def display(self):
        """ prints specified object """
        print("\n" * int(self.y), end="")
        for col in range(self.height):
            print(" " * int(self.x), end="")
            for row in range(self.width):
                print("#", end="")
            print("")

    def __str__(self):
        """ returns string repr. of object """
        t = "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"
        return t.format(self.id, self.__x, self.__y, self.__width, self.height)

    def update(self, *args, **kwargs):
        """ updates object attributes """
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
        """ returns dict repr. of object """
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
