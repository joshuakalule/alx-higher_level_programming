#!/usr/bin/python3
""" 4. From JSON string to Object """
import json


def from_json_string(my_str):
    """
    De-serialization of a str
    """
    return json.loads(my_str)
