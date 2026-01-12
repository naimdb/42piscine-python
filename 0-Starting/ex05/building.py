import sys

def main():
    args = sys.argv[1:]

    if len(args) == 0:
        text = input("What is the text to count?\n")
    else:
        assert len(args) == 1, "more than one argument is provided"
        text = args[0]

    punctuation = '''!"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~'''

    total_chars = len(text)
    upper_count = sum(1 for c in text if c.isupper())
    lower_count = sum(1 for c in text if c.islower())
    punctuation_count = sum(1 for c in text if c in punctuation)
    space_count = sum(1 for c in text if c.isspace())
    digit_count = sum(1 for c in text if c.isdigit())

    print(f"""The text contains {total_chars} characters:
{upper_count} upper letters
{lower_count} lower letters
{punctuation_count} punctuation marks
{space_count} spaces
{digit_count} digits""")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
