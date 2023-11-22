#!/usr/bin/python3
""" class implementation of a singly linked list """


class Node:
    """ defines a node of a singly linked list

    Attributes:
        data (str): data
        next_node (obj): next node
    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ defines a singly linked list

    Attributes:
        head : head of the list
    """
    def __init__(self):
        self.__head = None

    def __str__(self):
        if self.__head is None:
            return ""
        node = self.__head
        out_list = []
        while node:
            out_list.append("{:d}".format(node.data))
            node = node.next_node
        return "\n".join(out_list)

    def sorted_insert(self, value):
        """ insert node in a sorted manner """
        new = Node(value)
        parent = None
        node = self.__head
        while node:
            if node.data > value:
                break
            parent = node
            node = node.next_node

        if parent is None:
            self.__head = new
        else:
            parent.next_node = new
        new.next_node = node
