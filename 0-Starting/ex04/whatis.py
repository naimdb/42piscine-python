import sys

try:
    args = sys.argv[1:]
    
    if len(args) == 0:
        pass
    else:
        assert len(args) == 1, "more than one argument is provided"
        
        try:
            number = int(args[0])
        except ValueError:
            raise AssertionError("argument is not an integer")
        
        print("I'm Even." if number % 2 == 0 else "I'm Odd.")

except AssertionError as e:
    print(f"AssertionError: {e}")