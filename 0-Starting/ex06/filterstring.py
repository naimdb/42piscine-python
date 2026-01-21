import sys
from ft_filter import ft_filter


def main():
    """
    Main function to filter words based on length from command line arguments.
    Expects two arguments: a string of text and an integer n.
    Prints words longer than n.
    """

    args = sys.argv[1:]

    assert (len(args) == 2 and
            not args[0].isdigit()
            and args[1].isdigit())

    text, n = args[0], args[1]

    print(ft_filter(lambda word: len(word) > int(n), text.split()))


if __name__ == "__main__":
    try:
        main()
    except AssertionError:
        print("AssertionError: the arguments are bad")
