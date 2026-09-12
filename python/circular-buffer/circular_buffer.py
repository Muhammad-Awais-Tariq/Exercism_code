class BufferFullException(BufferError):
    """Exception raised when the circular buffer is full."""

    def __init__(self, message):
        """Initialize the exception with an error message.

        Parameters:
            message (str): Explanation of the error.
        """
        
        self.message = message
        super().__init__(self.message)


class BufferEmptyException(BufferError):
    """Exception raised when the circular buffer is empty."""

    def __init__(self, message):
        """Initialize the exception with an error message.

        Parameters:
            message (str): Explanation of the error.
        """

        self.message = message
        super().__init__(self.message)


class CircularBuffer:
    """Represent a fixed-size circular buffer."""

    def __init__(self, capacity):
        """Initialize the circular buffer.

        Parameters:
            capacity (int): Maximum number of elements the buffer can hold.
        """

        self.buffer = [None for _ in range(capacity)]
        self.head = 0
        self.current = 0
        self.tail = 0

    def read(self):
        """Read and remove the oldest element from the buffer.

        Returns:
            object: The oldest element in the buffer.

        Raises:
            BufferEmptyException: If the buffer is empty.
        """

        if self.current == 0:
            raise BufferEmptyException("Circular buffer is empty")

        current_element = self.buffer[self.head]
        self.buffer[self.head] = None
        self.head += 1
        self.current -= 1

        if self.head == len(self.buffer):
            self.head = 0

        if self.current == 0:
            self.head = 0

        return current_element

    def write(self, data):
        """Write an element to the buffer.

        Parameters:
            data (object): The element to store in the buffer.

        Raises:
            BufferFullException: If the buffer is already full.
        """

        if self.current == len(self.buffer):
            raise BufferFullException("Circular buffer is full")

        self.buffer[self.tail] = data
        self.tail += 1
        self.current += 1

        if self.tail == len(self.buffer):
            self.tail = 0

    def overwrite(self, data):
        """Write an element, replacing the oldest element if full.

        Parameters:
            data (object): The element to store in the buffer.
        """

        if self.current == len(self.buffer):
            self.tail = self.head
            self.buffer[self.tail] = data

            if self.head + 1 == len(self.buffer):
                self.head = 0
            else:
                self.head += 1
        else:
            self.buffer[self.tail] = data
            self.tail += 1
            self.current += 1

            if self.tail == len(self.buffer):
                self.tail = 0

    def clear(self):
        """Remove all elements from the buffer and reset its state."""
        
        self.head = 0
        self.current = 0
        self.tail = 0
        self.buffer = [None for _ in range(len(self.buffer))]