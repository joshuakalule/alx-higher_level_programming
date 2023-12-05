#!/usr/bin/python3
"""
5. Save Object to a file
"""
import json


def save_to_json_file(my_obj, filename):
    """
    writes object to a text file using json
    """
    with open(filename, 'w') as fp:
        return json.dump(my_obj, fp)
