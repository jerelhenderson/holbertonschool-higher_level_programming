#!/usr/bin/python3
class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if type(attrs) is not list:
            return(self.__dict__)

        new_dict = {}
        for name in attrs:
            if type(name) is not str:
                return self.__dict__
            try:
                new_dict[name] = getattr(self, name)
            except:
                pass

        return(new_dict)

    def reload_from_json(self, json):
        for key, value in json:
            setattr(self, key, value)
