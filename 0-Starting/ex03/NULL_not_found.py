def NULL_not_found(object: any) -> int:

    match object:
        case str() if not object:
            print(f"Empty: {object} {type(object)}")
        case float() if object != object:  # NaN trick: only value != itself
            print(f"Cheese: {object} {type(object)}")
        case bool() if object is False:
            print(f"Fake: {object} {type(object)}")
        case int() if object == 0:
            print(f"Zero: {object} {type(object)}")
        case None:
            print(f"Nothing: {object} {type(object)}")
        case _:
            print("Type not Found")
            return 1

    return 0
