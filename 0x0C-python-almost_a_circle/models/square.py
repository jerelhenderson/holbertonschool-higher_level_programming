#!/usr/bin/python3
"""
Module: Square
square.py - inherits from Base->Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class 'Square' inherits from Class 'Rectangle' """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ returns string repr. of object """
        text = "[Square] ({:d}) {:d}/{:d} - {:d}"
        return text.format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ 'size' attribute getter """
        return self.width

    @size.setter
    def size(self, value):
        """ 'size' attribute setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ update object attributes """
        attrs = ["id", "width", "x", "y"]

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
        return ({"id": self.id, "size": self.size, "x": self.x, "y": self.y})
