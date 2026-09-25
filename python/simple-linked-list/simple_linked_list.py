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
            self.len = 0
            self.node_head = None
            if values is not None:
                for value in values:
                    self.push(value)

    def __iter__(self):
        current_node = self.node_head

        while current_node != None:
            yield current_node.node_value
            current_node = current_node.next_node

    def __len__(self):
        return self.len

    def head(self):
        if self.len > 0:
            return self.node_head
        else:
            raise EmptyListException("The list is empty.")

    def push(self, value):
        new_node = Node(value)
        new_node.next_node = self.node_head
        self.node_head = new_node
        self.len += 1

    def pop(self):
        pass

    def reversed(self):
        pass
