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
        pass

    def read(self):
        pass

    def write(self, data):
        pass

    def overwrite(self, data):
        pass

    def clear(self):
        pass
