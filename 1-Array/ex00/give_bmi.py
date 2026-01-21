def give_bmi(height: list[int | float], weight: list[int | float]
             ) -> list[int | float]:
    """
    Calculate BMI for given height and weight lists.
    Args:
        height: List of heights in meters
        weight: List of weights in kilograms
    Returns:
        List of BMI values
    """

    if len(height) != len(weight):
        raise ValueError("Height and weight lists must have the same length")

    if not all(isinstance(h, (int, float)) for h in height):
        raise TypeError("Height must contain only int or float")

    if not all(isinstance(w, (int, float)) for w in weight):
        raise TypeError("Weight must contain only int or float")

    if any(h <= 0 for h in height):
        raise ValueError("Height must be positive")

    return [w / (h * h) for h, w in zip(height, weight)]


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """
    Apply a limit to a list of BMI values.

    Args:
        bmi: List of BMI values
        limit: Limit value

    Returns:
        List of booleans indicating if each BMI exceeds the limit
    """

    if not all(isinstance(b, (int, float)) for b in bmi):
        raise TypeError("BMI must contain only int or float")

    if not isinstance(limit, int):
        raise TypeError("Limit must be an integer")

    return [b > limit for b in bmi]
