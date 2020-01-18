#!/usr/bin/python3
import json

def load_from_json_file(filename):
    with open(filename, "r", encoding="UTF8") as my_json:
        return(json.load(my_json))
