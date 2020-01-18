#!/usr/bin/python3
class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def reload_from_json(self, json):
        for key, value in json:
            setattr(self, key, value)
