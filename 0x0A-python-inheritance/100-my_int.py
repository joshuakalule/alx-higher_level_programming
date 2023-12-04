#!/usr/bin/python3
""" 12. My integer """


class MyInt(int):
    """
    class that inherits from int
    """
    def __eq__(self, other):
        return not super().__eq__(other)

    def __ne__(self, other):
        return not super().__ne__(other)
