def callLimit(limit: int):
    """Decorator that limits the number of times a function can be called."""

    def callLimiter(function):
        count = 0

        def limit_function(*args: any, **kwargs: any):
            nonlocal count
            if count < limit:
                count += 1
                return function(*args, **kwargs)
            else:
                print("Error: call too many times")

        return limit_function
    return callLimiter
