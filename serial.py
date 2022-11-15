"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    
    def __init__(self, start=0):
        """Creates the Generator"""
        self.start = self.next = start
    def __repr__(self):
        """Describes the start and end of the generated numbers"""
        return f"<Serial generator start={self.start} next={self.next}>"
    def generate(self):
        """Returns the next serial"""
        self.next += 1
        return self.next -1
    def reset(self):
        """Sets serail back to start value"""
        self.next = self.start
