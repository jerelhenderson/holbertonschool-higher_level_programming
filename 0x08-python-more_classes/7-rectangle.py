#!/usr/bin/python3
class Rectangle:
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances = Rectangle.number_of_instances + 1

    @property
    def width(self):
        return(self.__width)
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return(self.__height)
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return(self.height * self.width)

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return(0)
        return(self.height + self.width) * (self.height + self.width)

    def __str__(self):
        new_string = ""

        if self.width == 0 or self.height == 0:
            return(new_string)
        for row in range(self.width):
            for col in range(self.height):
                new_string = new_string + ("{}".format(self.print_symbol))
            if row < self.height - 1:
                new_string = new_string + "\n"
        return(new_string)

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        Rectangle.number_of_instances = Rectangle.number_of_instances - 1
        print("Bye rectangle...")
