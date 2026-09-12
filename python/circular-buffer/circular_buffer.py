class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.

    """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class CircularBuffer:
    def __init__(self, capacity):
        self.buffer = [None for _ in range(capacity)]
        self.head = 0
        self.current = 0
        self.tail = 0

    def read(self):
        """
        Reads the element from the buffer.
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
        """
        Writes the element to the buffer.
        """

        if self.current == len(self.buffer):
            raise BufferFullException("Circular buffer is full")

        self.buffer[self.tail] = data
        self.tail += 1
        self.current += 1

        if self.tail == len(self.buffer):
            self.tail = 0


    def overwrite(self, data):
        pass

    def clear(self):
        """
        Clears the buffer.
        """

        self.head = 0
        self.current = 0
        self.tail = 0

        self.buffer = [None for _ in range(len(self.buffer))]
        
