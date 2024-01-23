#!/usr/bin/python3
"""
This module contains a Node class and a SinglyLinkedList class.
"""


class Node:
    """
    This class defines a node of a singly linked list.
    """

    def __init__(self, data, next_node=None):
        """
        Initialize the Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Get the data of the Node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set the data of the Node.
        """
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Get the next_node of the Node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the next_node of the Node.
        """
        if value is not None and type(value) is not Node:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    This class defines a singly linked list.
    """

    def __init__(self):
        """
        Initialize the SinglyLinkedList.
        """
        self.__head = None

    def __str__(self):
        """
        Print the entire list.
        """
        values = []
        node = self.__head
        while node is not None:
            values.append(str(node.data))
            node = node.next_node
        return "\n".join(values)

    def sorted_insert(self, value):
        """
        Insert a new Node into the correct sorted position in the list.
        """
        new_node = Node(value)
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            node = self.__head
            while node.next_node is not None and node.next_node.data < value:
                node = node.next_node
            new_node.next_node = node.next_node
            node.next_node = new_node
