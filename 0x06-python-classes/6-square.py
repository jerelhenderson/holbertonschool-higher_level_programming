#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
            return(self.__size)

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return(self.__position)

    @position.setter
    def position(self, value):
        if type(value) == tuple:
            if not value[0] < 0 or value[1] < 0:
                if len(value) == 2:
                    if type(value[0]) == int or type(value[1]) == int:
                        self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return(self.__size * self.__size)

    def my_print(self):
        if (self.__size == 0):
            print("")
            return

        for col in range(self.__position[1]):
            print(" ")
        for row in range(self.__size):
            for space in range(self.__position[0]):
                print(" ", end="")
            for col in range(self.__size):
                print("#", end="")
            print("")
