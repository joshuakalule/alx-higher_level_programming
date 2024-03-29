#!/usr/bin/python3
"""Find peak in a list of numbers."""


def find_peak(array):
    """Find peak in array."""
    if not isinstance(array, list):
        return None
    if array is None or len(array) == 0:
        return None
    if len(array) == 1:
        return array[0]
    leng = len(array)
    mid = int(leng / 2)
    if len(array) == 2:
        if array[mid - 1] <= array[mid]:
            return array[mid]
        return array[mid - 1]
    if array[mid - 1] < array[mid] and\
       array[mid + 1] < array[mid]:
        return array[mid]
    if array[mid - 1] > array[mid]:
        left_list = []
        left_list = array[:mid]
        return find_peak(left_list)
    else:
        right_list = []
        right_list = array[mid:]
        return find_peak(right_list)
