class calculator:
    """A calculator class that performs operations on vectors with scalars."""

    def __init__(self, vector):
        """Initialize the calculator with a vector."""
        self.vector = vector

    def __add__(self, object) -> None:
        """Add a scalar to each element of the vector."""
        self.vector = [x + object for x in self.vector]
        print(self.vector)

    def __mul__(self, object) -> None:
        """Multiply each element of the vector by a scalar."""
        self.vector = [x * object for x in self.vector]
        print(self.vector)

    def __sub__(self, object) -> None:
        """Subtract a scalar from each element of the vector."""
        self.vector = [x - object for x in self.vector]
        print(self.vector)

    def __truediv__(self, object) -> None:
        """Divide each element of the vector by a scalar."""
        if object == 0:
            print("Error: Division by zero")
            return
        self.vector = [x / object for x in self.vector]
        print(self.vector)
