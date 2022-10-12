#!/usr/bin/python3
"""Defines two classes Node and SinlyLinkedList"""


class Node:
    """A singly node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """Initializes a new node

        Args:
            data (int): the new data to be inserted
            next_node (Node): the next node in the list
        """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """int: The data inside the node"""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """The next node in the list"""
        return self.__netx_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) or value != None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinlyLinkedList:
    """Defines a singly linked list data structure"""

    def __init__(self):
        """"""

    def sorted_insert(self, value):
        """"""
