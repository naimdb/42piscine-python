def square(x: int | float) -> int | float:
    """Returns the square of x."""
    return x * x


def pow(x: int | float) -> int | float:
    """Returns x to the power of itself."""
    return x ** x


def outer(x: int | float, function) -> object:
    """
    Returns a function that applies 'function' to 'x' repeatedly.
    Each call applies 'function' to the previous result and
    returns the new value.
    """

    def inner() -> float:
        nonlocal x
        x = function(x)
        return x

    return inner
