#!/usr/bin/python3
"""Defines two classes Node and SinlyLinkedList"""


class Node:
    """Defines a new node for singly linked list"""

    def __init__(self, data, next_node=None):
        """Initializes a new node

        Args:
            data (int): the new data to be inserted
            next_node (Node): the next node in the list
        """
        self.data = data
        self.next_node = next_node

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
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list data structure"""

    def __init__(self):
        """Initializes a new singly linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new node into the singly linked list

        The new node will be inserted at the
        correct position of increasingly sorted items

        Args:
            value (int): the new data to be inserted
        """
        new_node = Node(value)

        temp = self.__head
        if self.__head is None:
            self.__head = new_node
        elif temp.data >= value:
            self.__head = new_node
            new_node.next_node = temp
        else:
            while temp.next_node is not None:
                if temp.next_node.data >= value:
                    break
                temp = temp.next_node

            new_node.next_node = temp.next_node
            temp.next_node = new_node

    def __str__(self) -> str:
        """Makes a SinglyLinkedList object printable

        Prints the entire list in stdout, one node number by line

        Returns:
            the list items as strings
        """
        datas = []

        temp = self.__head
        while temp is not None:
            datas.append(str(temp.data))
            temp = temp.next_node

        return ('\n'.join(datas))
