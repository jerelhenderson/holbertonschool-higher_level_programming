#!/usr/bin/python3
import json
from sys import argv

save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

json_list = load_from_json_file("add_item.json")

 
