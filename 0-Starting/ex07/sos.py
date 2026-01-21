import sys


def get_morse_dict():
    """Return the Morse code dictionary."""
    return {
        " ": "/ ",
        "A": ".- ", "B": "-... ", "C": "-.-. ", "D": "-.. ",
        "E": ". ", "F": "..-. ", "G": "--. ", "H": ".... ",
        "I": ".. ", "J": ".--- ", "K": "-.- ", "L": ".-.. ",
        "M": "-- ", "N": "-. ", "O": "--- ", "P": ".--. ",
        "Q": "--.- ", "R": ".-. ", "S": "... ", "T": "- ",
        "U": "..- ", "V": "...- ", "W": ".-- ", "X": "-..- ",
        "Y": "-.-- ", "Z": "--.. ",
        "0": "----- ", "1": ".---- ", "2": "..--- ", "3": "...-- ",
        "4": "....- ", "5": "..... ", "6": "-.... ", "7": "--... ",
        "8": "---.. ", "9": "----. "
    }


def validate_input(text):
    """
    Validate that the input contains only alphanumeric characters and spaces.

    Args:
        text: String to validate

    Raises:
        AssertionError: If text contains invalid characters
    """
    for char in text:
        if not (char.isalnum() or char.isspace()):
            raise AssertionError("the arguments are bad")


def encode_to_morse(text):
    """
    Encode a text string into Morse code.

    Args:
        text: String to encode

    Returns:
        String containing the Morse code representation
    """
    morse_dict = get_morse_dict()
    morse_code = "".join(morse_dict[char] for char in text.upper())
    return morse_code.strip()


def main():
    """Encode a string into Morse Code."""
    try:
        args = sys.argv[1:]
        assert len(args) == 1, "the arguments are bad"

        text = args[0]
        validate_input(text)
        morse_result = encode_to_morse(text)
        print(morse_result)

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
