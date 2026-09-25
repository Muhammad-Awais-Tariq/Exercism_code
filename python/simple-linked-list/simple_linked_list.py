class EmptyListException(Exception):
    pass


class Node:
    """Represents a single node of the linked list"""
    def __init__(self, value):
        self.node_value = value
        self.next_node = None

    def value(self):
        return self.node_value 

    def next(self):
        return self.next_node


class LinkedList:
    def __init__(self, values=None):
        pass

    def __iter__(self):
        pass

    def __len__(self):
        pass

    def head(self):
        pass

    def push(self, value):
        pass

    def pop(self):
        pass

    def reversed(self):
        pass
