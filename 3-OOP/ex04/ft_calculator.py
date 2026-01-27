class calculator:
    """
    A calculator class for performing vector operations.
    All methods are static and can be called without instantiating the class.
    """

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        Calculate and print the dot product of two vectors.
        The dot product is the sum of the products of corresponding elements.
        """
        result = sum(v1 * v2 for v1, v2 in zip(V1, V2))
        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        Calculate and print the element-wise addition of two vectors.
        """
        result = [float(v1 + v2) for v1, v2 in zip(V1, V2)]
        print(f"Add Vector is : {result}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        Calculate and print the element-wise subtraction of two vectors.
        """
        result = [float(v1 - v2) for v1, v2 in zip(V1, V2)]
        print(f"Sous Vector is: {result}")
