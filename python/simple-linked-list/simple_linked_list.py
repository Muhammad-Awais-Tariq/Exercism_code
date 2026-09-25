class EmptyListException(Exception):
    """Exception raised when an operation is performed on an empty list."""

class Node:
    """Represent a single node in a singly linked list."""

    def __init__(self, value):
        """Initialize a node with a value and no next node.

        Parameters:
            value: The value stored in the node.
        """
        self.data = value
        self.next_node = None

    def value(self):
        """Return the value stored in the node.

        Returns:
            The value stored in the node.
        """
        return self.data

    def next(self):
        """Return the next node in the linked list.

        Returns:
            Node: The next node, or None if this is the last node.
        """
        return self.next_node


class LinkedList:
    """Represent a singly linked list."""

    def __init__(self, values=None):
        """Initialize a linked list with optional values.

        Parameters:
            values: An optional iterable of values to add to the list.
        """
        self.length = 0
        self.head_node = None

        if values is not None:
            for value in values:
                self.push(value)

    def __iter__(self):
        """Iterate over the values in the linked list.

        Yields:
            The value stored in each node, starting from the head.
        """
        current_node = self.head_node

        while current_node is not None:
            yield current_node.data
            current_node = current_node.next_node

    def __len__(self):
        """Return the number of nodes in the linked list.

        Returns:
            int: The number of nodes in the list.
        """
        return self.length

    def head(self):
        """Return the first node in the linked list.

        Returns:
            Node: The head node of the list.

        Raises:
            EmptyListException: If the list is empty.
        """
        if self.length > 0:
            return self.head_node

        raise EmptyListException("The list is empty.")

    def push(self, value):
        """Add a new value to the beginning of the linked list.

        Parameters:
            value: The value to add to the list.
        """
        new_node = Node(value)
        new_node.next_node = self.head_node
        self.head_node = new_node
        self.length += 1

    def pop(self):
        """Remove and return the first value from the linked list.

        Returns:
            The value stored in the removed node.

        Raises:
            EmptyListException: If the list is empty.
        """
        if self.length <= 0:
            raise EmptyListException("The list is empty.")

        current_value = self.head_node.data
        self.head_node = self.head_node.next_node
        self.length -= 1

        return current_value

    def reversed(self):
        """Return a new linked list with the values in reverse order.

        Returns:
            LinkedList: A new linked list containing the values in reverse order.
        """
        all_values = list(self)
        new_list = LinkedList()

        for value in all_values:
            new_list.push(value)

        return new_list