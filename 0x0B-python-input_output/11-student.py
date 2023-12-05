#!/usr/bin/python3
"""
11. Student to disk and reload
"""


class Student:
    """
    defines a student
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves dict representation """
        if isinstance(attrs, list):
            if all(map(lambda x: isinstance(x, str), attrs)):
                return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """ replace all attributes """
        if len(json) != 0:
            self.__init__(json.get("first_name"), json.get("last_name"),
                          json.get("age"))
