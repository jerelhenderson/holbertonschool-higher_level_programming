#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    with open(filename, "w", encoding="UTF8") as my_json:
        json.dump(my_obj, my_json)
