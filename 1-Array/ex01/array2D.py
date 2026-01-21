import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slice a 2D array and display its shape.

    Args:
        family: A 2D list (list of lists with same length)
        start: Starting index for slicing
        end: Ending index for slicing

    Returns:
        Sliced 2D list

    Raises:
        TypeError: If start/end are not integers
        ValueError: If family is not a valid 2D array
    """

    if not isinstance(start, int) or not isinstance(end, int):
        raise TypeError("start and end must be integers")

    try:
        array = np.array(family)
    except (ValueError, TypeError) as e:
        raise ValueError("family must be a valid 2D array") from e

    if array.ndim != 2:
        raise ValueError("family must be a 2D array")

    print(f"My shape is : {array.shape}")

    new_array = array[start:end]

    print(f"My new shape is : {new_array.shape}")

    return new_array.tolist()
